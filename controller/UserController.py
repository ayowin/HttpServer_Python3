

import flask;

import service.UserService as UserService;

class Controller:
    def __init__(self) :
        self.userService = UserService.Service();

    def register(self,request):
        response = self.userService.register(request);
        return response;

    def login(self,request):
        response = self.userService.login(request);
        return response;

    def logout(self,request):
        response = self.userService.logout(request);
        return response;

'''
    blueprint & route config
'''
blueprint = flask.Blueprint("userController",__name__);
__controller = Controller();
__urlPrefix = "/user";

@blueprint.route(__urlPrefix + "/register",methods=['POST'])
def __register():
    return __controller.register(flask.request);

@blueprint.route(__urlPrefix + "/login",methods=['POST'])
def __login():
    return __controller.login(flask.request);

@blueprint.route(__urlPrefix + "/logout",methods=['POST'])
def __logout():
    return __controller.logout(flask.request);
