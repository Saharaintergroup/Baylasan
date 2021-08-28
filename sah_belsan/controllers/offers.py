from odoo.addons.portal.controllers.web import Home
from odoo import http
from odoo.http import request

from odoo.addons.http_routing.models.ir_http import slug


class WebsiteSort(Home):
    @http.route('/shop/offers')
    def index(self, **kw):

        Product = request.env['product.product'].with_context(bin_size=True)

        offers_products = Product.search([('discount', '>', 0.0)])
        # print(offers_products)
        if offers_products:
            url = "/shop/offers/%s" % slug(offers_products)
            current_products = offers_products
            while current_products.product_id:
                offers_products.append(current_products.product_id)
        print(offers_products)
        return request.render('sah_belsan.product_offers_page', {
            'offers_products': offers_products,
        })