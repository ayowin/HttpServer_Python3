
import json as Json;

import db.RedisPool as RedisPool;
import util.VerifyCodeUtil as VerifyCodeUtil;

class Service:
    def __init__(self):
        self.__id = 0;

    def index(self):
        response = {};
        response["content"] = "index";
        return Json.dumps(response);

    def verifyCode(self):
        response = {};

        self.__id = self.__id + 1;
        code = VerifyCodeUtil.Util.verifyCode(self.__id,6);

        # redis storage
        connection = RedisPool.Pool.getConnection();
        key = "verifyCode_" + str(code["id"]);
        value = code["result"];
        expire = 180;
        connection.set(key,value,ex=expire);

        response["id"] = code["id"];
        response["base64"] = code["base64"];
        return Json.dumps(response);
