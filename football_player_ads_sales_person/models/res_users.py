from odoo import models, fields, api

class Users(model.Model):
    _inherit = "res.users"

    player_ids = fields.One2many("football.player", "sales_id", string="Players")
    club_id = fields.Many2one('football.player.club', string="Player Club")
