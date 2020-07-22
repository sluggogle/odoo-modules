# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

ADDRESS_FIELDS = ('street', 'street2', 'zip', 'city')

class Bank(models.Model):
    _inherit = 'res.bank'

    @api.model
    def _address_fields(self):
        """Returns the list of address fields that are synced from the parent."""
        return list(ADDRESS_FIELDS)

    @api.model
    def _formatting_address_fields(self):
        """Returns the list of address fields usable to format addresses."""
        return self._address_fields()

    @api.model
    def _get_default_address_format(self):
        return "%(street)s %(street2)s\n%(zip)s %(city)s"
    
    def get_address(self, inline=False):
        address_format = self._get_default_address_format()
        if inline:
            address_format.replace('\n', ' - ')

        addr = {}
        for field in self._formatting_address_fields():
            addr[field] = getattr(self, field) or ''

        return address_format % addr
