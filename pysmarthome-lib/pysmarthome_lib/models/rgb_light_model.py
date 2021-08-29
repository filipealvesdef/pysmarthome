from .device_model import DevicesModel, DeviceStatesModel
from vesla_pymvc import clone


class RgbLampStatesModel(DeviceStatesModel):
    schema = clone(DeviceStatesModel.schema)
    schema['state']['schema'] |= {
        'color': { 'type': 'string', 'default': '#ffffff' },
        'brightness': { 'type': 'number', 'default': 0 },
    }


class RgbLampsModel(DevicesModel):
    schema = clone(DevicesModel.schema)
    children_model_classes = clone(DevicesModel.children_model_classes)
    children_model_classes |= { 'state': { 'class': RgbLampStatesModel } }