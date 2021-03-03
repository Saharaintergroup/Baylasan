# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InheritProduct(models.Model):
    _inherit = 'product.template'

    discount = fields.Float("Discount (%)")

    @api.onchange('discount')
    def _value_sale_price(self):
        for rec in self:
            rec.list_price = (rec.list_price - rec.discount /100 * rec.list_price)