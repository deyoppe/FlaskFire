from os import path

class __CONST():
    # Directory names
    CONTROLLERS_DIRNAME = 'controllers'
    MODELS_DIRNAME = 'models'
    SETTINGS_DIRNAME = 'settings'
    
    # Directory paths
    APP_PATH = 'app'
    CONTROLLERS_PATH = path.join(APP_PATH, CONTROLLERS_DIRNAME)
    MODELS_PATH = path.join(APP_PATH, MODELS_DIRNAME)
    SETTINGS_PATH = path.join(APP_PATH, SETTINGS_DIRNAME)
    
constants = __CONST()