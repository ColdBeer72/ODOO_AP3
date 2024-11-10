from odoo import models, fields, api
from pytz import timezone, UTC, all_timezones
from datetime import datetime

class ResPartner(models.Model):
    _inherit = 'res.partner'

    birthdate = fields.Date(string='Fecha de Nacimiento')
    tz = fields.Selection(
        selection='_tz_get', string='Zona Horaria',
        help='Zona horaria del contacto.'
    )
    age = fields.Integer(string='Edad', compute='_compute_age', store=True)

    def _tz_get(self):
        return [(tz, tz) for tz in all_timezones]

    @api.depends('birthdate')
    def _compute_age(self):
        """Calcula la edad en función de la fecha de nacimiento"""
        today = fields.Date.today()
        for partner in self:
            if partner.birthdate:
                birthdate = fields.Date.from_string(partner.birthdate)
                age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
                partner.age = age
            else:
                partner.age = 0

    @api.model
    def get_today_birthdays(self):
        """Retorna los contactos que cumplen años hoy según su zona horaria"""
        user_tz = self.env.user.tz or 'UTC'
        user_timezone = timezone(user_tz)
        current_time = datetime.now(UTC).astimezone(user_timezone)

        partners = self.search([('birthdate', '!=', False)])
        today_birthdays = []

        for partner in partners:
            partner_tz = timezone(partner.tz or 'UTC')
            partner_time = current_time.astimezone(partner_tz)
            if partner_time.strftime('%m-%d') == partner.birthdate.strftime('%m-%d'):
                today_birthdays.append(partner)

        return today_birthdays
