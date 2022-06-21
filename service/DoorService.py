
import json as Json;

import util.AuthenticateUtil as AuthenticateUtil;
import util.AuthorizeUtil as AuthorizeUtil;

class Service:
    '''
        request data:
            hearder:
                "token": "xxx"
    '''
    def open(self, request):
        response = {};

        requestData = request.headers;
        if ("token" in requestData and
            requestData["token"] != None) :
            token = requestData["token"];
            if AuthenticateUtil.Util.authenticate(token) :
                if (AuthorizeUtil.Util.hasPermission(token,"admin") or
                    AuthorizeUtil.Util.hasPermission(token, "door")):
                    response["result"] = "success";
                else :
                    response["result"] = "failed";
                    response["reason"] = "unlimited";
            else :
                response["result"] = "failed";
                response["reason"] = "token invalid";

        return Json.dumps(response);
