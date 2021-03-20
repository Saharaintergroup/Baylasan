# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InheritProduct(models.Model):
    _inherit = 'product.template'

    old_products = fields.Boolean(compute="_get_old_compute",search="_get_old_products")

    def _get_old_compute(self):
        for product in self.search([('qty_available', '=', 0)]):
            if not self.env['stock.move'].search([('product_id', '=', product.id)]):
                product.old_products = True

    def _get_old_products(self, operator, value):

        products_ids = []
        for product in self.search([('qty_available', '=', 0)]):
            if not self.env['stock.move'].search([('product_id','=',product.id)]):
                products_ids.append(product.id)
        return [('id', 'in', products_ids)]

