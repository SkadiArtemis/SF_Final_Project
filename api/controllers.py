import asyncio
import random
import asyncpg

import models
import sql_requests
from settings import *


async def get_all_machineries():
    try:
        async with asyncpg.connect(database=DB_NAME, host=DB_HOST, port=DB_PORT) as conn:
            raw_result = await conn.execute(sql_requests.SELECT_ALL, "machineries")
            result = []
            for row in raw_result:
                result.append(models.Machinery._make(row))
    except Exception as error:
        result = error.__str__()
    return result


async def get_machinery_by_id(machinery_id: str):
    try:
        async with asyncpg.connect(database=DB_NAME, host=DB_HOST, port=DB_PORT) as conn:
            result = await conn.execute(sql_requests.SELECT_BY_ID, "machineries", machinery_id)
            return models.Machinery._make(result)
    except Exception as error:
        result = error.__str__()
    return result


async def add_machinery(machinery: models.Machinery):
    try:
        async with asyncpg.connect(database=DB_NAME, host=DB_HOST, port=DB_PORT) as conn:
            await conn.execute(sql_requests.INSERT_MACHINERY, machinery)
            result = "ok"
    except Exception as error:
        result = error.__str__()
    return {"result": result}


async def get_all_maintenances():
    try:
        async with asyncpg.connect(database=DB_NAME, host=DB_HOST, port=DB_PORT) as conn:
            raw_result = await conn.execute(sql_requests.SELECT_ALL, "maintenances")
            result = []
            for row in raw_result:
                result.append(models.Maintenance._make(row))
    except Exception as error:
        result = error.__str__()
    return result


async def get_maintenance_by_id(maintenance_id: str):
    try:
        async with asyncpg.connect(database=DB_NAME, host=DB_HOST, port=DB_PORT) as conn:
            result = await conn.execute(sql_requests.SELECT_BY_ID, "maintenances", maintenance_id)
            return models.Maintenance._make(result)
    except Exception as error:
        result = error.__str__()
    return result


async def add_maintenance(maintenance: models.Maintenance):
    try:
        async with asyncpg.connect(database=DB_NAME, host=DB_HOST, port=DB_PORT) as conn:
            await conn.execute(sql_requests.INSERT_MAINTENANCE, maintenance)
            result = "ok"
    except Exception as error:
        result = error.__str__()
    return {"result": result}


async def get_all_reclamations():
    try:
        async with asyncpg.connect(database=DB_NAME, host=DB_HOST, port=DB_PORT) as conn:
            raw_result = await conn.execute(sql_requests.SELECT_ALL, "reclamations")
            result = []
            for row in raw_result:
                result.append(models.Reclamation._make(row))
    except Exception as error:
        result = error.__str__()
    return result


async def get_reclamation_by_id(reclamation_id: str):
    try:
        async with asyncpg.connect(database=DB_NAME, host=DB_HOST, port=DB_PORT) as conn:
            result = await conn.execute(sql_requests.SELECT_BY_ID, "reclamations", reclamation_id)
            return models.Reclamation._make(result)
    except Exception as error:
        result = error.__str__()
    return result


async def add_reclamation(reclamation: models.Reclamation):
    try:
        async with asyncpg.connect(database=DB_NAME, host=DB_HOST, port=DB_PORT) as conn:
            await conn.execute(sql_requests.INSERT_RECLAMATION, reclamation)
            result = "ok"
    except Exception as error:
        result = error.__str__()
    return {"result": result}
