from odoo import fields, models, api

class Player(models.Model):
    _name = 'football.player'
    _description = 'Football Players on the Market'

    # Basic info
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    # may change to many2one: club = fields.Char(string="Club")
    age = fields.Integer(string="Age")
    market_value = fields.Float(string="Market Value")
    contract_expire = fields.Date(string="Contract Expire")
    active = fields.Boolean(string="is Active", default=True)

    # Since there can be way too many clubs in football nowadays
    # its best not make it a selection field
    # RM may need an referee club in their pos_id 
    
    # Many players can belong to 1 club
    club_id = fields.Many2one('football.player.club', string="Player Club")

    # Many players can play many positions
    position_ids = fields.Many2many('football.player.position', string="Player Position")

    # One player can have many stats
    stat_ids = fields.One2many('football.player.stat', 'player_id', string="Stat")

    # Further info
    player_type = fields.Selection([
        ('starter', 'Starter'),
        ('substitute', 'Substitute'),
        ('reserve', 'Reserve'),
        ('youth', 'Youth')
    ], string ='Player Type')
    sales_id = fields.Many2one('res.users', string="Salesman")
    buyer_id = fields.Many2one('res.partner', string="Buyer")

    # Computed fields
    @api.depends('age', 'player_type', 'market_value')
    def _compute_suggested_value(self):
        for rec in self:
            if rec.age is not None:
                if rec.age <= 21:
                    age_factor = 1.2
                elif 22 <= rec.age <= 28:
                    age_factor = 1.0
                elif 29 <= rec.age <= 32:
                    age_factor = 0.8
                else:
                    age_factor = 0.6
            else:
                age_factor = 1.0  # fallback if age is missing

            type_multipliers = {
                'starter': 1.5,
                'substitute': 1.2,
                'reserve': 1.0,
                'youth': 1.1,
            }
            type_multiplier = type_multipliers.get(rec.player_type, 1.0)

            rec.suggested_value = (rec.market_value or 0.0) * age_factor * type_multiplier


    suggested_value = fields.Float(string="Suggested Value", compute=_compute_suggested_value)

    # default hidden fields
    # id, create_date, write_date, create_uid, write_uid


class PlayerClub(models.Model):
    _name = 'football.player.club'
    _description = 'Clubs that a player can play'
    
    name = fields.Char(string="Name", required=True)


class PlayerPosition(models.Model):
    _name = 'football.player.position'
    _description = 'Positions that a player can play'
    
    name = fields.Char(string="Name", required=True)
