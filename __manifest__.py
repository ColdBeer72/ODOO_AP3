{
    'name': 'Extend Partner - Cumpleaños y Zona Horaria',
    'version': '13.0',
    'summary': 'Extiende res.partner con fecha de nacimiento y zona horaria, y una consulta de cumpleaños.',
    'description': """
        Extendemos el modelo de contactos (res.partner) para añadir la fecha de nacimiento 
        y la zona horaria. También añade una pantalla para consultar los cumpleaños del día, 
        teniendo en cuenta la diferencia horaria.
    """,
    'author': 'Manuel Tornos',
    'depends': ['base'],
    'data': [
        'views/res_partner_view.xml',
        'views/birthday_view.xml',
    ],
    'installable': True,
    'application': False,
}
