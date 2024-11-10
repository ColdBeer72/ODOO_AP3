{
    'name': 'Extend Partner - Birthdate & Timezone',
    'version': '13.0.1.0.0',
    'summary': 'Extiende res.partner con fecha de nacimiento y zona horaria, con consulta de cumpleaños.',
    'description': """
        Este módulo extiende el modelo de contactos (res.partner) para agregar la fecha de nacimiento 
        y la zona horaria. Además, añade una pantalla para consultar los cumpleaños del día, 
        teniendo en cuenta la diferencia horaria. También proporciono una API para obtener los 
        contactos que cumplen años.
    """,
    'author': 'Manuel Tornos',
    'depends': ['base'],
    'data': [
        'views/res_partner_view.xml',
        'views/birthday_view.xml'
    ],
    'controllers': [
        'controllers/main.py',
    ],
    'installable': True,
    'application': False,
}
