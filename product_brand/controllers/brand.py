from werkzeug.exceptions import NotFound

from odoo import http, models, fields, _
from odoo.http import request
from odoo.addons.website.controllers.main import Website

class Website(Website):
    @http.route(auth='public')
    def index(self, page=0, **kw):
        """function home page"""
        super(Website, self).index(**kw)
        brands = request.env['product.brand']
        total_brand = brands.sudo().search([('is_published_brand', '=', 'True')])
        print(total_brand)

        return request.render('sah_belsan.belsan_home_page', {
            'total_brand': total_brand,
        })


