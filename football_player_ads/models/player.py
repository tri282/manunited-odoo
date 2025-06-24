from odoo import fields, models

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

    # Further info
    player_type = fields.Selection([
        ('starter', 'Starter'),
        ('substitute', 'Substitute'),
        ('reserve', 'Reserve'),
        ('youth', 'Youth')
    ], string ='Player Type')

    # Stats
    goal = fields.Integer(string="Goals per Season")
    assist = fields.Integer(string="Assist per Season")
    avg_rating = fields.Float(string="Rating per Game")

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
