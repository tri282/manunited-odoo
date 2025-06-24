{
    "name": "Football Transfer Market",
    "version": "1.0",
    "description": """
        Module to show available players on the summer transfer market
    """,
    "category": "Sales",
    "depends": [],
    "data": [
        'security/ir.model.access.csv',
        'views/player_view.xml',
        'views/menu_items.xml',
        'views/player_club_view.xml',
        'views/player_position_view.xml',
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}
