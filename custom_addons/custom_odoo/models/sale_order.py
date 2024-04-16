from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # field
    customer_notes = fields.Text(string="Notes")
