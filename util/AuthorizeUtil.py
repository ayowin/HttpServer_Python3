
import json as Json;

import db.RedisPool as RedisPool;

class Util:
    '''
        if user has role
        @token: request token
        @role: role string
        @return: True for existed, False for not existed
    '''
    @staticmethod
    def hasRole(token,role):
        exist = False;

        connection = RedisPool.Pool.getConnection();
        userJson = connection.get(token);
        user = Json.loads(userJson);
        roles = user["role"];
        for item in roles :
            if item == role :
                exist = True
                break;

        return exist;

    '''
        if user has permission
        @token: request token
        @permission: permission string
        @return: True for existed, False for not existed
    '''
    @staticmethod
    def hasPermission(token, permission):
        exist = False;

        connection = RedisPool.Pool.getConnection();
        userJson = connection.get(token);
        if userJson != None :
            user = Json.loads(userJson);
            permissions = user["permission"];
            for item in permissions:
                if item == permission:
                    exist = True
                    break;

        return exist;
