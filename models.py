from collections import namedtuple
from datetime import datetime

Machinery = namedtuple('Machinery', [
    'machinery_id', 'machinery_model',
    'engine_model', 'engine_id',
    'transmission_model', 'transmission_id',
    'drive_axle_model', 'drive_axle_id',
    'steerable_axle_model', 'steerable_axle_id',
    'contract_id',
    'shipment_date',
    'receiver_name', 'receiver_address',
    'equipment',
    'client',
    'service_center',
])


Maintenance = namedtuple('Maintenance', [
    'maintenance_type',
    'maintenance_date',
    'operating_time',
    'request_id',
    'request_date',
    'client',
    'machinery_id',
    'service_center',
])


MaintenanceFull = namedtuple('Maintenance', [
    'maintenance_type',
    'maintenance_type_description',
    'maintenance_date',
    'operating_time',
    'request_id',
    'request_date',
    'client',
    'machinery_id',
    'service_center',
    'service_center_description'
])


Reclamation = namedtuple('Reclamation', [
    'reclamation_date',
    'operating_time',
    'failure_nodes',
    'failure_description',
    'restoration_method',
    'spare_parts_used',
    'restoration_date',
    'downtime',
    'machinery_id',
    'service_center',
])
