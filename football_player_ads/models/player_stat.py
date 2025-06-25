from odoo import fields, models, api

class PlayerStat(models.Model):
    _name = 'football.player.stat'
    _description = 'Football Players Stat available'

    goal = fields.Integer(string="Goal")
    assist = fields.Integer(string="Assist")
    appearance = fields.Integer(string="Appearance")
    avg_rating = fields.Float(string="Average Rating")
    status = fields.Selection(
            [('available', 'Available'), ('unavailable', 'Unavailable')],
            string="Status")

    # for testing purposes, disregard this field
    partner_id = fields.Many2one('res.partner', string="Partner")

    player_id = fields.Many2one('football.player', string="Player") # unique identifier for player
    creation_date = fields.Date(string="Create Date")

    @api.depends('goal', 'assist', 'appearance', 'avg_rating')
    def _compute_personal_rating(self):
        for rec in self:
            goals = rec.goal or 0
            assists = rec.assist or 0
            appearances = rec.appearance or 1  # avoid division by zero
            avg_rating = rec.avg_rating or 0

            # Simple weighted formula
            rec.personal_rating = (
                (goals * 4 + assists * 3) / appearances
            ) + avg_rating

    personal_rating = fields.Float(string="Personal Rating", compute="_compute_personal_rating")

