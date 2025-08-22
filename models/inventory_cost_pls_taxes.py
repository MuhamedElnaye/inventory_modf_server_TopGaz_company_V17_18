from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    cost_with_tax = fields.Float(
        string='Cost + Purchase Taxes',
        compute='_compute_cost_with_tax',
        store=False,
    )
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        compute='_compute_currency_id',
        store=False
    )

    @api.depends('standard_price', 'supplier_taxes_id')
    def _compute_cost_with_tax(self):
        for product in self:
            # ضرائب الشراء فقط (Purchase Taxes)
            purchase_taxes = product.supplier_taxes_id.filtered(
                lambda t: t.amount_type == 'percent' and t.type_tax_use == 'purchase'
            )
            if purchase_taxes:
                total_tax_percent = (sum(tax.amount for tax in purchase_taxes))-1
                product.cost_with_tax = product.standard_price * (1 + (total_tax_percent / 100))
            else:
                product.cost_with_tax = product.standard_price