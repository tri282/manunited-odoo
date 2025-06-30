
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class FootballPlayer(model.Model):
    _inherit = "football.player"

    sales_id = fields.Many2one("res.users", required=True)

    @api.model_create_multi
    def create(self, vals_list):
        for val in vals_list:
            sales_person_player_ids = self.env[self.name].search_count([("sales_id", "=", val.get("sales_id"))])

            if sales_person_player_ids > 2:
                raise ValidationError("User has 2 players assigned already")

        return super(FootballPlayer, self).create(vals_list)
