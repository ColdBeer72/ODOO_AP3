from odoo import http
from odoo.http import request
from datetime import datetime
from pytz import timezone, UTC

class ExtendPartnerController(http.Controller):

    @http.route('/extend_partner/find', type='json', auth='public', methods=['GET'])
    def find_today_birthdays(self):
        """
        Endpoint de API que devuelve los contactos que cumplen años a lo largo del día de hoy.

        Respuesta:
            - status (int): Código de estado HTTP (200: éxito).
            - message (str): Mensaje de éxito.
            - data (list): Lista de diccionarios con los datos de contactos que cumplen años.
        
        Parámetros:
            Ninguno.

        Autenticación:
            Requiere token de autenticación o sesión activa.
        """
        partners = request.env['res.partner'].sudo().search([('birthdate', '!=', False)])
        user_tz = request.env.user.tz or 'UTC'
        user_timezone = timezone(user_tz)
        current_time = datetime.now(UTC).astimezone(user_timezone)
        
        today_birthdays = []
        for partner in partners:
            partner_tz = timezone(partner.tz or 'UTC')
            partner_time = current_time.astimezone(partner_tz)
            # Verificamos si hoy es el cumpleaños según la zona horaria del contacto
            if partner_time.strftime('%m-%d') == partner.birthdate.strftime('%m-%d'):
                today_birthdays.append({
                    'name': partner.name,
                    'birthdate': partner.birthdate,
                    'timezone': partner.tz,
                    'age': partner.age
                })

        return {
            'status': 200,
            'message': 'Cumpleaños encontrados',
            'data': today_birthdays
        }
