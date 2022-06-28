

import flask;

import service.FileService as FileService;

class Controller:
    def __init__(self) :
        self.fileService = FileService.Service();
        
    def upload(self,request):
        response = self.fileService.upload(request);
        return response;

'''
    blueprint & route config
'''
blueprint = flask.Blueprint("fileController",__name__);
__controller = Controller();
__urlPrefix = "/file";

@blueprint.route(__urlPrefix + "/upload",methods=['POST'])
def __upload():
    return __controller.upload(flask.request);
