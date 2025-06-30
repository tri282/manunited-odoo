from odoo import fields, models, api
from datetime import timedelta
from odoo.exceptions import ValidationError

class AbstractStat(models.AbstractModel):
    _name = 'abstract.model.stat'

    partner_email = fields.Char(string="Email")
    partner_phone = fields.Char(string="Phone Number")

class PlayerStat(models.Model):
    _name = 'football.player.stat'
    _description = 'Football Players Stat available'
    _inherit = ['abstract.model.stat']

    name = fields.Char(string="Name")
    goal = fields.Integer(string="Goal")
    assist = fields.Integer(string="Assist")
    appearance = fields.Integer(string="Appearance")
    validity = fields.Integer(string="Validity")
    avg_rating = fields.Float(string="Average Rating")
    status = fields.Selection(
            [('available', 'Available'), ('unavailable', 'Unavailable')],
            string="Status")
    active = fields.Boolean(string='Active', default=True)


    # for testing purposes, disregard this field
    partner_id = fields.Many2one('res.partner', string="Partner")

    player_id = fields.Many2one('football.player', string="Player") # unique identifier for player

    '''
    # MODEL
    # Usage: set as an extra param in field definition
    # For isntance, creation_date = fields.Date(string="Create Date", default=_set_creation_date)
    @api.model
    def _set_creation_date(self):
        return fields.Date.today()
    '''

    creation_date = fields.Date(string="Create Date")
    deadline = fields.Date(string="Deadline")

    '''
    # AUTOVACUUM
    # Usage: evoke the daily vacuum cron job that collects the garbage
    # Details can be found inside the Scheduled Actions module
    @api.autovacuum
    def _clean_stats(self):
        self.search([('active', '=', False)]).unlink() # clean/delete stats where active is False
        # applicable for different data types, string, ints, etc
    '''

    # MODEL_CREATE_MULTI
    # Usage: update values before it is created
    @api.model_create_multi
    def create(self, vals_list):
        for rec in vals_list:
            # Set creation date if not provided
            if not rec.get('creation_date'):
                rec['creation_date'] = fields.Date.today()
            
            if not rec.get('deadline'):
                rec['deadline'] = fields.Date.today()
           
            # IMPORTANT
            # There is distinction between:
            # if not rec.get('param') and if 'param' not in rec
            # In the case where goal = 0 is valid, we should use the second since the first checks for "faulty" values
            # like NULL, 0, False

            if not rec.get('goal'):
                rec['goal'] = 0
            
            if not rec.get('assist'):
                rec['assist'] = 0
            
            if not rec.get('appearance'):
                rec['appearance'] = 0
            
            if not rec.get('validity'):
                rec['validity'] = 0
            
            if not rec.get('avg_rating'):
                rec['avg_rating'] = 0

        return super(PlayerStat, self).create(vals_list)
    
    '''
    CONSTRAINS
    # Usage: like a Java's exception check
    @api.constrains('goals')
    def _check_goals(self):
        for rec in self:
            if rec.goals < 0:
                raise ValidationError(_("Goals must not be less than 0"))
    ''' 

    # SQL CONSTRAINTS
    # Usage: similar but space-saving for constrains
    _sql_constraints = [
        ('check_goal', 'CHECK(goal >= 0)', 'Goal must not be less than 0'),
        # in other words, we are creating a constrains called check_goal that check the condition if goal is greater than or equal to 0
        # if not satisfy, print the error message
        # consider reinstall the module for it to work
        ('check_assist', 'CHECK(assist >= 0)', 'Assist must not be less than 0'),
        ('check_appearance', 'CHECK(appearance >= 0)', 'Appearance must not be less than 0'),
        ('check_appearance', 'CHECK(validity >= 0)', 'Validity must not be less than 0'),
        ('check_avg_rating', 'CHECK(avg_rating >= 0 AND avg_rating <= 10)', 'Average rating must be between 0 and 10')
    ]

    @api.depends('goal', 'assist', 'appearance', 'avg_rating')
    # DEPENDS.CONTEXT
    # @api.depends.context()
    def _compute_personal_rating(self):
        # print(self.env.context)
        # print(self._context) # same stuff as above
        for rec in self:
            goals = rec.goal or 0
            assists = rec.assist or 1
            appearances = rec.appearance or 1  # avoid division by zero
            avg_rating = rec.avg_rating or 0

            # Simple weighted formula
            rec.personal_rating = (
                (goals * 4 + assists * 3) / appearances
            ) + avg_rating

    personal_rating = fields.Float(string="Personal Rating", compute="_compute_personal_rating")

    def extend_stat_deadline(self):
        activ_ids = self._context.get('active_ids', [])

        if activ_ids:
            stat_ids = self.env['football.player.stat'].browse(activ_ids)

            for stat in stat_ids:
                stat.validity = 10

    # needs to be defined as api model for a cron job
    @api.model
    def _extend_stat_deadline(self):
        stat_ids = self.env['football.player.stat'].search([]) # cron job active for all stats
        
        for stat in stat_ids:
            stat.validity = stat.validity + 1


    # WRITE orm command
    '''
    def write(self, vals_list):
        # print(vals)
        # self.env('res.partner').browse(1) ==> # res.partner(1)

        # SEARCH orm command
        res_partner_ids self.env(['res.partner'].search([
           ('is_company', '=', True),
           ('name', '=', vals_list.get('name')),
           )])
        # print(res_partner_ids.name)

        return super(PlayerStat, self).write(vals_list)

    '''

    # UNLINK orm command
    '''
    Reasons to overwrite unlink: resolve dependent/associated records before removing anything
    def unlink(self):
    '''

    # MAPPED orm command
    '''
    Use to link fields from a different class
    For instance:
        res_partner_ids self.env(['res.partner'].search([
           ('is_company', '=', True),
           ('name', '=', vals_list.get('name')),
           )]).mapped('phone')
    # will print the phone number in the res_partner_ids returned by from the search
    '''

    # FILTERED orm command
    '''
    Filtered filter
        res_partner_ids self.env(['res.partner'].search([
           ('is_company', '=', True),
           ('name', '=', vals_list.get('name')),
           )]).filter(lambda x: x.phone == '123-456-7890')
    '''


