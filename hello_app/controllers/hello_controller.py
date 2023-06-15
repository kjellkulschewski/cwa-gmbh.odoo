from odoo import http
from odoo.http import request

class HelloController(http.Controller):
    @http.route('/hello', auth='public', website=True)
    def hello(self, **kwargs):
        return request.render('hello_app.hello_view')
