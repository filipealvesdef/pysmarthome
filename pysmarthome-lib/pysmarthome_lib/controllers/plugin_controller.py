import importlib
from . import Controller
from ..models import PluginsModel

class PluginController(Controller):
    model_class = PluginsModel

    @property
    def device_controller_classes(self): return self.module.device_controllers


    @property
    def module_name(self): return self.model.module_name


    def __init__(self):
        self.module = None


    def on_load(self, module_name='', **data):
        self.module = importlib.import_module(module_name)
        if 'on_load' in list(self.module.__dict__.keys()):
            self.module.on_load(**data['config'])
