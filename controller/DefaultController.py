

import flask;

import service.DefaultService as DefaultService;

class Controller:
    def __init__(self) :
        self.defaultService = DefaultService.Service();
        
    def index(self):
        response = self.defaultService.index();
        return response;

    def verifyCode(self):
        response = self.defaultService.verifyCode();
        return response;

'''
    blueprint & route config
'''
blueprint = flask.Blueprint("defaultController",__name__);
__controller = Controller();
__urlPrefix = "/default";

@blueprint.route(__urlPrefix + "/index",methods=['GET', 'POST'])
def __index():
    return __controller.index();

@blueprint.route(__urlPrefix + "/verifyCode",methods=['GET', 'POST'])
def __verifyCode():
    return __controller.verifyCode();
