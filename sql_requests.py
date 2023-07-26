SELECT_ALL = '''SELECT * FROM $1;'''
SELECT_BY_ID = '''SELECT * FROM $1 WHERE machinery_id=$2;'''
INSERT_MACHINERY = '''INSERT INTO machineries (
    machinery_id,
    machinery_model,
    engine_model,
    engine_id,
    transmission_model,
    transmission_id,
    drive_axle_model,
    drive_axle_id,
    steerable_axle_model,
    steerable_axle_id,
    contract_id,
    shipment_date,
    receiver_name,
    receiver_address,
    equipment,
    client,
    service_center
    ) VALUES(
    $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17);'''
INSERT_MAINTENANCE = '''INSERT INTO maintenances (
    maintenance_type,
    maintenance_date,
    operating_time,
    request_id,
    request_date,
    client,
    machinery_id,
    service_center,
    ) VALUES(
    $1, $2, $3, $4, $5, $6, $7, $8);'''
INSERT_RECLAMATION = '''INSERT INTO reclamations (
    reclamation_date,
    operating_time,
    failure_nodes,
    failure_description,
    restoration_method,
    spare_parts_used,
    restoration_date,
    downtime,
    machinery_id,
    service_center,
    ) VALUES(
    $1, $2, $3, $4, $5, $6, $7, $8, $9, $10);'''
