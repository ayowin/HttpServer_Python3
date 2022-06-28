
import time;
import os;
import json as Json;

import util.AuthenticateUtil as AuthenticateUtil;

class Service:
    def __init__(self):
        self.__id = 0;

    def upload(self,request):
        response = {};

        requestData = request.headers;
        if ("token" in requestData and
            requestData["token"] != None) :
            token = requestData["token"];
            if AuthenticateUtil.Util.authenticate(token) :
                files = request.files; # upload files dictionary
                fileKeys = files.keys();
                uploadPath = "./upload";
                if os.path.exists(uploadPath) == False :
                    os.makedirs(uploadPath);
                try :
                    for fileKey in fileKeys:
                        currentUsTimestamp = str(int(round(time.time() * 1000000)));
                        filePath = "{:s}/{:s}_{:s}".format(uploadPath,currentUsTimestamp,fileKey);
                        files[fileKey].save(filePath);
                    response["result"] = "success";
                except Exception as e:
                    response["result"] = "failed";
                    response["reason"] = "save exception by {:s}".format(str(e));
            else:
                response["result"] = "failed";
                response["reason"] = "token invalid";
        else:
            response["result"] = "failed";
            response["reason"] = "request data incorrect";

        return Json.dumps(response);
