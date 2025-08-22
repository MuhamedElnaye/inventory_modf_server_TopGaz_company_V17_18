# inventory_modf_server_TopGaz_company_V17_18
 Odoo Module: Product Cost with Purchase Taxes

## Overview
This custom Odoo module extends the **Product Template** model (`product.template`) by adding a computed field that shows the product's **cost including purchase taxes**.

- New Field: **Cost + Purchase Taxes**
- Dynamically computed based on `standard_price` and `supplier_taxes_id`.

## Features
- Automatically calculates the cost including **purchase percentage taxes**.
- Works only with **purchase taxes** (type: `purchase`).
- Non-stored computed field (always up-to-date).

## Code Explanation
The module adds two fields:
1. `cost_with_tax`: Float – The standard price including purchase taxes.
2. `currency_id`: Many2one – Shows the related currency.

The calculation:
```python
purchase_taxes = product.supplier_taxes_id.filtered(
    lambda t: t.amount_type == 'percent' and t.type_tax_use == 'purchase'
)
if purchase_taxes:
    total_tax_percent = (sum(tax.amount for tax in purchase_taxes)) - 1
    product.cost_with_tax = product.standard_price * (1 + (total_tax_percent / 100))
else:
    product.cost_with_tax = product.standard_price
