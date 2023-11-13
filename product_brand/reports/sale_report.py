# Copyright 2018 Tecnativa - David Vidal
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    product_brand_id = fields.Many2one(
        comodel_name='product.brand',
        string='Brand',
    )

    # def _query(self, with_clause='', fields=None, groupby='', from_clause=''):
    #     fields = fields or {}
    #     fields['product_brand_id'] = ", t.product_brand_id as product_brand_id"
    #     groupby += ', t.product_brand_id'
    #     return super(SaleReport, self)._query(
    #         with_clause, fields, groupby, from_clause
    #     )

    # def _query(self):
    #     res = super()._query()
    #     return res + f"""UNION ALL (
    #         SELECT {self._select_pos() + ', t.product_brand_id as product_brand_id'}
    #         FROM {self._from_pos()}
    #         WHERE {self._where_pos()}
    #         GROUP BY {self._group_by_pos() + ', t.product_brand_id'}
    #         )
    #     """

    # def _select_sale(self):
    #     res = super()._select_sale() + ', t.product_brand_id as product_brand_id'
    #     return res
    #
    # def _group_by_pos(self):
    #     res = super()._group_by_pos() + ', t.product_brand_id'
    #     return res
