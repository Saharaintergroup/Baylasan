from odoo.addons.portal.controllers.web import Home
from odoo import http
from odoo.http import request


class WebsiteSort(Home):
    @http.route('/')
    def index(self, **kw):
        super(WebsiteSort, self).index()

        Product = request.env['product.template'].with_context(bin_size=True)
        Category = request.env['product.public.category']
        brands = request.env['product.brand'].search([])
        new_products = Product.search([('is_published', '=', True)], order="create_date DESC", limit=8)
        # offers_products = Product.search([('is_published', '=', True), ('is_offers', '=', True)])
        # popular_products = Product.search([('is_published', '=', True), ('is_popular', '=', True)])
        categories = Category.search([('parent_id', '=', False)] + request.website.website_domain())
        # slider_home = request.env['slider.home'].search([])
        return request.render('sah_belsan.belsan_home_page', {
            'new_products': new_products,
            # 'offers_products': offers_products,
            # 'popular_products': popular_products,
            'categories': categories,
            'brands': brands,
            # 'slider_home': slider_home,
        })

# class AboutUs(http.Controller):
#     @http.route('/about_us',type='http', auth='public')
#     def about(self, **kw):
#
#         Product = request.env['product.template'].search_count([])
#         Brands = request.env['product.brand'].search_count([])
#         Company = request.env['res.company'].search([],limit=1)
#
#         return request.render('sah_belsan.belsan_about_us_page', {
#             'product': Product,
#             'brands': Brands,
#             'company': Company,
#
#         })