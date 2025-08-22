
from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    customer_ref = fields.Char(string='Customer Ref')