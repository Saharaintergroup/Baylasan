# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InheritProduct(models.Model):
    _inherit = 'product.template'

    discount = fields.Float("Discount (%)")
    # old_products = fields.Char()

    @api.onchange('discount')
    def _value_sale_price(self):
        for rec in self:
            rec.list_price = (rec.list_price - rec.discount /100 * rec.list_price)

class ResCompany(models.Model):
    _inherit = 'res.company'

    snapchat = fields.Char("SnapChat Account")
    branches_no = fields.Integer("No of Branches")

class Website(models.Model):
    _inherit = 'website'

    def _default_social_snapchat(self):
        return self.env.ref('base.main_company').snapchat

    snapchat = fields.Char("SnapChat Account",default=_default_social_snapchat)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    snapchat = fields.Char(related='website_id.snapchat', readonly=False)

    @api.depends('website_id', 'social_twitter', 'social_facebook', 'social_github', 'social_linkedin',
                 'social_youtube', 'social_googleplus', 'social_instagram','snapchat')
    def has_social_network(self):
        self.has_social_network = self.social_twitter or self.social_facebook or self.social_github \
                                  or self.social_linkedin or self.social_youtube or self.social_googleplus or self.social_instagram or self.snapchat

    def inverse_has_social_network(self):
        if not self.has_social_network:
            self.social_twitter = ''
            self.social_facebook = ''
            self.social_github = ''
            self.social_linkedin = ''
            self.social_youtube = ''
            self.social_googleplus = ''
            self.social_instagram = ''
            self.snapchat = ''

    has_social_network = fields.Boolean("Configure Social Network", compute=has_social_network,
                                        inverse=inverse_has_social_network)
