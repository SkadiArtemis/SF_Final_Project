import json

import marshmallow
from aiohttp_apispec import request_schema
from aiohttp import web

import controllers
import models
import schemas


async def healthcheck(request):
    return web.Response(status=200, text="I'm alive, beatch")


async def get_all_machineries(request):
    data = await controllers.get_all_machineries()
    return web.Response(body=json.dumps(data))


async def get_all_maintenances(request):
    data = await controllers.get_all_maintenances()
    return web.Response(body=json.dumps(data))


async def get_all_reclamations(request):
    data = await controllers.get_all_reclamations()
    return web.Response(body=json.dumps(data))


async def get_machinery_by_id(request):
    machinery_id = request.match_info["id"]
    data = await controllers.get_machinery_by_id(machinery_id)
    return web.Response(body=json.dumps(data))


async def get_maintenance_by_id(request):
    maintenance_id = request.match_info["id"]
    data = await controllers.get_maintenance_by_id(maintenance_id)
    return web.Response(body=json.dumps(data))


async def get_reclamation_by_id(request):
    reclamation_id = request.match_info["id"]
    data = await controllers.get_reclamation_by_id(reclamation_id)
    return web.Response(body=json.dumps(data))


@request_schema(schemas.AddMachineryRequestSchema())
async def add_machinery(request):
    raw_data = await request.json()
    try:
        data = schemas.AddMachineryRequestSchema().load(raw_data)
    except marshmallow.exceptions.ValidationError as error:
        return web.Response(status=400, text=error.__str__())
    machinery = models.Machinery._make(data.values())
    data = await controllers.add_machinery(machinery)
    return web.Response(body=json.dumps(data))


@request_schema(schemas.AddMaintenanceRequestSchema())
async def add_maintenance(request):
    raw_data = await request.json()
    try:
        data = schemas.AddMaintenanceRequestSchema().load(raw_data)
    except marshmallow.exceptions.ValidationError as error:
        return web.Response(status=400, text=error.__str__())
    maintenance = models.Maintenance._make(data.values())
    data = await controllers.add_maintenance(maintenance)
    return web.Response(body=json.dumps(data))


@request_schema(schemas.AddReclamationRequestSchema())
async def add_reclamation(request):
    raw_data = await request.json()
    try:
        data = schemas.AddReclamationRequestSchema().load(raw_data)
    except marshmallow.exceptions.ValidationError as error:
        return web.Response(status=400, text=error.__str__())
    reclamation = models.Reclamation._make(data.values())
    data = await controllers.add_reclamation(reclamation)
    return web.Response(body=json.dumps(data))
