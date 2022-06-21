
import hashlib;
import json as Json
import time;
import uuid;

import db.MysqlPool as MysqlPool;
import db.RedisPool as RedisPool;

class Service:
    '''
        request data:
            {
                "username": "xxx",
                "password": "xxx",
                "verify_code_id": "xxx",
                "verify_code_result": "xxx"
            }
    '''
    def register(self,request):
        response = {};
        
        requestData = request.json;
        if ("username" in requestData and
            "password" in requestData and
            "verify_code_id" in requestData and
            "verify_code_result" in requestData) :
            # verify code check
            redisConnection = RedisPool.Pool.getConnection();
            key = "verifyCode_" + str(requestData["verify_code_id"]);
            value = redisConnection.get(key);
            if (value != None and
                value == requestData["verify_code_result"]) :
                redisConnection.delete(key);

                username = requestData["username"];
                password = requestData["password"];
                password = bytes(password,"UTF-8");
                password = hashlib.md5(password).hexdigest();
                password = password[5:len(password)-5];

                mysqlConnection = MysqlPool.Pool.getConnection();
                cursor = mysqlConnection.cursor();
                sql = "insert into user (`username`,`password`) value ('{:s}','{:s}');".format(username,password);
                try :
                    cursor.execute(sql);
                    response["result"] = "success";
                except Exception as e :
                    response["result"] = "failed";
                    response["reason"] = "insert exception";

            else :
                response["result"] = "failed";
                response["reason"] = "invalid verify code";
        else :
            response["result"] = "failed";
            response["reason"] = "request data incorrect";

        return response;

    '''
        request data:
            {
                "username": "xxx",
                "password": "xxx",
                "verify_code_id": "xxx",
                "verify_code_result": "xxx"
            }
    '''
    def login(self,request):
        response = {};

        requestData = request.json;
        if ("username" in requestData and
            "password" in requestData and
            "verify_code_id" in requestData and
            "verify_code_result" in requestData) :
            # verify code check
            redisConnection = RedisPool.Pool.getConnection();
            key = "verifyCode_" + str(requestData["verify_code_id"]);
            value = redisConnection.get(key);
            if (value != None and
                value == requestData["verify_code_result"]) :
                redisConnection.delete(key);

                username = requestData["username"];
                password = requestData["password"];
                password = bytes(password, "UTF-8");
                password = hashlib.md5(password).hexdigest();
                password = password[5:len(password) - 5];

                mysqlConnection = MysqlPool.Pool.getConnection();
                cursor = mysqlConnection.cursor();
                sql = "select * from user where `username`='{:s}' and `password`='{:s}';".format(username,password);
                cursor.execute(sql);
                data = cursor.fetchone(); # [id,username,password,role_id,upadte_time]
                # login success
                if data != None :
                    # generate token
                    token = uuid.uuid3(uuid.NAMESPACE_URL,username + str(time.time()));
                    token = str(token);

                    # construct user for redis
                    user = {};
                    user["id"] = data[0];
                    user["username"] = data[1];
                    user["role"] = [];
                    user["permission"] = [];

                    # permission id set
                    permissionIdSet = set();
                    # select roles
                    roleId = data[3];
                    if roleId != None :
                        roleId = roleId.split(",");
                        sql = "select `role`,`permission_id` from `role` where ";
                        for id in roleId :
                            if id == roleId[len(roleId)-1] :
                                sql += "id={:s}".format(id);
                            else:
                                sql += "id={:s} or ".format(id);
                        cursor.execute(sql);
                        item = cursor.fetchone(); # [role,permission_id]
                        while item != None :
                            user["role"].append(item[0]);
                            permissionId = item[1].split(",");
                            for id in permissionId :
                                permissionIdSet.add(id);
                            item = cursor.fetchone();

                    # select permissions
                    if len(permissionIdSet) > 0 :
                        sql = "select `permission` from `permission` where ";
                        while len(permissionIdSet) > 0 :
                            id = permissionIdSet.pop();
                            if len(permissionIdSet) > 0 :
                                sql += "id={:s} or ".format(id);
                            else:
                                sql += "id={:s}".format(id);
                            permissionIdSet.discard(id);
                        cursor.execute(sql);
                        item = cursor.fetchone();  # [role,permission_id]
                        while item != None:
                            user["permission"].append(item[0]);
                            item = cursor.fetchone();

                    user = Json.dumps(user);
                    redisConnection.set(token,user,30*60);

                    response["result"] = "success";
                    response["token"] = token;
                else :
                    response["result"] = "failed";
                    response["reason"] = "username or password incorrect";
            else :
                response["result"] = "failed";
                response["reason"] = "invalid verify code";
        else :
            response["result"] = "failed";
            response["reason"] = "request data incorrect";
        
        return Json.dumps(response);

    '''
        request data:
            hearder:
                "token": "xxx"
    '''
    def logout(self, request):
        response = {};

        requestData = request.headers;
        if ("token" in requestData and
            requestData["token"] != None) :
            redisConnection = RedisPool.Pool.getConnection();
            key = requestData["token"];
            redisConnection.delete(key);

        response["result"] = "success";

        return Json.dumps(response);
