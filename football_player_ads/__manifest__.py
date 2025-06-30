{
    "name": "Football Transfer Market",
    "version": "1.0",
    "description": """
        Module to show available players on the summer transfer market
    """,
    "category": "Sales",
    "depends": ["base", "mail"],
    "data": [
        # groups
        'security/ir.model.access.csv',
        'security/res_groups.xml',
        'security/model_access.xml',
        'security/ir_rule.xml',

        # views
        'views/player_view.xml',
        'views/player_web_template.xml',
        'views/player_club_view.xml',
        'views/player_position_view.xml',
        'views/player_stat_view.xml',
        'views/menu_items.xml',

        # data Files
        'data/player_club.xml',
        'data/football.player.position.csv',
        #'data/mail_template.xml'
        
        # reports
        #'report/report_template.xml',
        #'report/player_report.xml',
    ],
    "demo": [
        "demo/football.player.stat.csv",
    ],

    # Syntax issue w Odoo version
    #'assets': {
    #    'web.assets_backend': [
    #        'football_player_ads/static/src/js/custom_tag.js',
    #        'football_player_ads/static/src/xml/custom_tag.xml',
    #    ]
    #},

    "installable": True,
    "application": True,
    "license": "LGPL-3"
}
