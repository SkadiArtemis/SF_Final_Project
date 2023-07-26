from marshmallow import Schema, fields


class AddMachineryRequestSchema(Schema):
    machinery_id = fields.Str(description='Зав. № машины', required=True)
    machinery_model = fields.Str(description='Модель техники', required=True)

    engine_model = fields.Str(description='Модель двигателя', required=True)
    engine_id = fields.Str(description='Зав. № двигателя', required=True)

    transmission_model = fields.Str(description='Модель трансмиссии', required=True)
    transmission_id = fields.Str(description='Зав. № трансмиссии', required=True)

    drive_axle_model = fields.Str(description='Модель ведущего моста', required=True)
    drive_axle_id = fields.Str(description='Зав. № ведущего моста', required=True)

    steerable_axle_model = fields.Str(description='Модель управляемого моста', required=True)
    steerable_axle_id = fields.Str(description='Зав. № управляемого моста', required=True)

    contract_id = fields.Str(description='Договор поставки №, дата', required=True)
    shipment_date = fields.Str(description='Дата отгрузки с завода', required=True)
    receiver_name = fields.Str(description='Грузополучатель (конечный потребитель)', required=True)
    receiver_address = fields.Str(description='Адрес поставки (эксплуатации)', required=True)
    equipment = fields.Str(description='Комплектация (доп. опции)', required=True)
    client = fields.Str(description='Клиент', required=True)
    service_center = fields.Str(description='Сервисная компания', required=True)


class AddMaintenanceRequestSchema(Schema):
    maintenance_type = fields.Str(description='Вид ТО', required=True)
    maintenance_date = fields.Str(description='Дата проведения ТО', required=True)
    operating_time = fields.Int(description='Наработка, м/час', required=True)
    request_id = fields.Str(description='№ заказ-наряда', required=True)
    request_date = fields.Str(description='Дата заказ-наряда', required=True)
    client = fields.Str(description='Организация, проводившая ТО', required=True)
    machinery_id = fields.Str(description='Машина', required=True)
    service_center = fields.Str(description='Сервисная компания', required=True)


class AddReclamationRequestSchema(Schema):
    maintenance_date = fields.Str(description='Дата отказа', required=True)
    operating_time = fields.Int(description='Наработка, м/час', required=True)
    failure_nodes = fields.Str(description='Узел отказа', required=True)
    failure_description = fields.Str(description='Описание отказа', required=True)
    restoration_method = fields.Str(description='Способ восстановления', required=True)
    spare_parts_used = fields.Str(description='Используемые запасные части', required=True)
    restoration_date = fields.Str(description='Дата восстановления', required=True)
    downtime = fields.Int(description='Время простоя техники', required=True)
    machinery_id = fields.Str(description='Машина', required=True)
    service_center = fields.Str(description='Сервисная компания', required=True)


