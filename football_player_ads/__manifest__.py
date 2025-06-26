{
    "name": "Football Transfer Market",
    "version": "1.0",
    "description": """
        Module to show available players on the summer transfer market
    """,
    "category": "Sales",
    "depends": ["base"],
    "data": [
        'security/ir.model.access.csv',
        'views/player_view.xml',
        'views/player_club_view.xml',
        'views/player_position_view.xml',
        'views/menu_items.xml',

        # Data Files
        'data/player_club.xml',
        'data/football.player.position.csv',
    ],
    "demo": [
        "demo/football.player.stat.csv",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}
