
import json as Json;

import db.RedisPool as RedisPool;

class Util:
    '''
        check token valid and renew expire
        @token: request token
    '''
    @staticmethod
    def authenticate(token):
        connection = RedisPool.Pool.getConnection();
        valid = connection.expire(token,30*60);
        return valid;
