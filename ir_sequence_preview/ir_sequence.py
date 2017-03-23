# -*- coding: utf-8 -*-

from openerp.osv import osv, fields
from openerp.tools.translate import _
import logging

_logger = logging.getLogger(__name__)

class ir_sequence(osv.osv):
    _inherit = 'ir.sequence'

    def _preview_next(self, cr, uid, seq_ids, context=None):
        if not seq_ids:
            return False
        if context is None:
            context = {}
        force_company = context.get('force_company')
        if not force_company:
            force_company = self.pool.get('res.users').browse(cr, uid, uid).company_id.id

        sequences = self.read(cr, uid, seq_ids, ['name','company_id','implementation','number_next','prefix',
                                                 'suffix','padding', 'number_increment', 'auto_reset',
                                                 'reset_period', 'reset_time', 'reset_init_number'])

        preferred_sequences = [s for s in sequences if s['company_id'] and s['company_id'][0] == force_company ]
        seq = preferred_sequences[0] if preferred_sequences else sequences[0]
        
        # Reset sequence if period expired
        if seq['implementation'] == 'standard':
            current_time =':'.join([seq['reset_period'], self._interpolation_dict().get(seq['reset_period'])])
            if seq['auto_reset'] and current_time != seq['reset_time']:
                cr.execute("UPDATE ir_sequence SET reset_time=%s WHERE id=%s ", (current_time,seq['id']))
                self._alter_sequence(cr, seq['id'], seq['number_increment'], seq['reset_init_number'])
                cr.commit()

        # Getting next value
        cr.execute("SELECT last_value, increment_by, is_called FROM ir_sequence_%03d" % seq['id'])
        (last_value, increment_by, is_called) = cr.fetchone()
        if is_called:
            seq['number_next'] = last_value + increment_by
        else:
            seq['number_next'] = last_value

        d = self._interpolation_dict()
        
        try:
            interpolated_prefix = self._interpolate(seq['prefix'], d)
            interpolated_suffix = self._interpolate(seq['suffix'], d)
        except ValueError:
            raise osv.except_osv(_('Warning'), _('Invalid prefix or suffix for sequence \'%s\'') % (seq.get('name')))
        return interpolated_prefix + '%%0%sd' % seq['padding'] % seq['number_next'] + interpolated_suffix

    def preview_next_by_id(self, cr, uid, sequence_id, context=None):
        """ Draw an interpolated string using the specified sequence."""
        self.check_access_rights(cr, uid, 'read')
        company_ids = self.pool.get('res.company').search(cr, uid, [], context=context) + [False]
        ids = self.search(cr, uid, ['&',('id','=', sequence_id),('company_id','in',company_ids)])
        return self._preview_next(cr, uid, ids, context)

