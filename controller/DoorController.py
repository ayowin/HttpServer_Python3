
import flask;

import service.DoorService as DoorService;

class Controller:
    def __init__(self) :
        self.doorService = DoorService.Service();

    def open(self,request):
        response = self.doorService.open(request);
        return response;

'''
    blueprint & route config
'''
blueprint = flask.Blueprint("doorController",__name__);
__controller = Controller();
__urlPrefix = "/door";

@blueprint.route(__urlPrefix + "/open",methods=['POST'])
def __open():
    return __controller.open(flask.request);
