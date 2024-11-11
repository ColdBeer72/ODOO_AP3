# Módulo Extend Partner para ODOO_AP3
Extendemos el modelo de contactos (res.partner) para añadir la fecha de nacimiento y la zona horaria. También añade una pantalla para consultar los cumpleaños del día, teniendo en cuenta la diferencia horaria.

Válido para **ODOO V13**


## Descripción
Este módulo extiende el modelo de contactos (`res.partner`) en Odoo, añadiendo los campos de **fecha de nacimiento** y **zona horaria**. Permite, a su vez, consultar los cumpleaños del día teniendo en cuenta la diferencia horaria, y mostrando quiénes están de cumpleaños en el momento actual. También proporciona una API pública para obtener los contactos que están de cumpleaños hoy.

## Funcionalidades
- Campo `birthdate`: Fecha de nacimiento del contacto.
- Campo `tz`: Zona horaria del contacto.
- Campo calculado `age`: Edad del contacto, calculada automáticamente en función de la fecha de nacimiento.
- Vista de contactos de cumpleaños del día.
- Endpoint API JSON en `/extend_partner/find` para obtener contactos de cumpleaños según la zona horaria.

## Uso de la API
La API proporciona una lista de contactos de cumpleaños para el día actual según la zona horaria del usuario. Los datos se devuelven en JSON.

**Endpoint**: `/extend_partner/find`

**Método**: GET

**Formato de respuesta**: JSON

### Ejemplo de Solicitud
```bash
curl -X GET http://localhost:8069/extend_partner/find \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer tu_token_de_api"
```

### Ejemplo de Respuesta
```html
{
    "status": 200,
    "message": "Cumpleaños encontrados",
    "data": [
        {
            "name": "Juan Pérez",
            "birthdate": "1985-10-24",
            "timezone": "America/Argentina/Buenos_Aires",
            "age": 39
        }
    ]
}
```

## Instalación
- Instalar el módulo en el directorio addons de su instancia de Odoo.
- Reiniciar el servidor de Odoo.
- Activar el modo de desarrollador e ir a Aplicaciones para instalar el módulo.
## Configuración
Para acceder a la API:
- Generar un token de autenticación desde el perfil de usuario en Odoo.
- Usar dicho token en el encabezado de autorización de las solicitudes.
## Requisitos
Odoo versión 13 o superior.
## Dependencias
`base`: módulo base de Odoo.
## Notas del desarrollo
La API usa la zona horaria del contacto para calcular su cumpleaños local, y requiere autenticación mediante token o sesión activa.