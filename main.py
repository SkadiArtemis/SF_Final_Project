from aiohttp import web
from api.views import *
from settings import *

app = web.Application()
app.add_routes([web.get('/', healthcheck),
                web.get('/machinery/all', get_all_machineries),
                web.get('/machinery/{id}', get_machinery_by_id),
                web.post('/machinery', add_machinery),
                web.get('/maintenance/all', get_all_maintenances),
                web.get('/maintenance/{id}', get_maintenance_by_id),
                web.post('/maintenance', add_maintenance),
                web.get('/reclamation/all', get_all_reclamations),
                web.get('/reclamation/{id}', get_reclamation_by_id),
                web.post('/reclamation', add_reclamation)
                ])

web.run_app(app, host=HOST, port=PORT)

