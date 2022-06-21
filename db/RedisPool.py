
import redis;

'''
    1. config redis connection parameters
    2. get connection by: Pool.getConnection()
'''
class Pool:
    __pool = None;

    @staticmethod
    def getConnection():
        if Pool.__pool == None :
            '''
                decode redis response bytes to string:
                    decode_responses=True 
            '''
            Pool.__pool = redis.ConnectionPool(host='127.0.0.1', 
                                            port=6379, 
                                            decode_responses=True);
        connection = redis.Redis(connection_pool = Pool.__pool);
        return connection;
