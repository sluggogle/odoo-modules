from openerp import models, fields, api
from openerp.tools.translate import _
import os
import logging

_logger = logging.getLogger(__name__)


# Override Report
#   - _build_wkhtmltopdf_args
#
# Add --disable-smart_shrinking to wkhtmltopdf command

class LabelReport(models.Model):
    _inherit = 'report'

    def _build_wkhtmltopdf_args(self, paperformat, specific_paperformat_args=None):
        command_args = super(LabelReport, self)._build_wkhtmltopdf_args(paperformat, specific_paperformat_args)

        if paperformat.name == 'Label A4':
            command_args.extend(['--disable-smart-shrinking'])
        _logger.info('WKHTMLTOPDF: %s', command_args)

        return command_args
