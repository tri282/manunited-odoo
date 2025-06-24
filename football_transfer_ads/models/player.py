from odoo import fields, models

class Player(models.Model):
    _name = 'football.player'
    _description = 'Football Players on the Market'

    # Basic info
    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    club = fields.Char(string="Club")
    age = fields.Integer(string="Age")
    market_value = fields.Float(string="Market Value")
    contract_expire = fields.Date(string="Contract Expire")
    active = fields.Boolean(string="is Active", default=True)

    # Further info
    position = fields.Selection([
        ('gk', 'Goalkeeper'),
        ('df', 'Defender'),
        ('mf', 'Midfielder'),
        ('fw', 'Striker')
    ], string="Position")

    # Stats
    goal = fields.Integer(string="Goals per Season")
    assist = fields.Integer(string="Assist per Season")
    avg_rating = fields.Float(string="Rating per Game")

    # default hidden fields
    # id, create_date, write_date, create_uid, write_uid
