from odoo import http
from odoo.http import request

class PlayerController(http.Controller):

    @http.route(['/players'], type='http', website=True, auth="public")
    def show_players(self):
        player_ids = request.env['football.player'].sudo().search([])
        print(player_ids)

        return request.render("football_player_ads.player_list", {"player_ids": player_ids})
