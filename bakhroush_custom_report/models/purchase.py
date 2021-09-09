# -*- coding: utf-8 -*-
from odoo import models, fields,api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    total_orders = fields.Float(string="Total Ordered",store=True, readonly=True, compute='_compute_qty',)
    total_received = fields.Float(string="Total Delivered" ,store=True, readonly=True, compute='_compute_qty')

    @api.depends('order_line','order_line.product_qty','order_line.qty_received')
    def _compute_qty(self):
        for order in self:
            qty_received = product_qty = 0.0
            for line in order.order_line:
                product_qty += line.product_qty
                qty_received += line.qty_received
            order.update({
                'total_orders': product_qty,
                'total_received': qty_received,
            })