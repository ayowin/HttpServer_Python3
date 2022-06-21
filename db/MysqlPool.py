
import dbutils.pooled_db as DBUtilsPooledDB;
import pymysql;

'''
    1. config mysql connection parameters
    2. get connection by: Pool.getConnection()
'''
class Pool:
    __pool = None;

    @staticmethod
    def getConnection():
        if Pool.__pool == None :
            Pool.__pool = DBUtilsPooledDB.PooledDB(pymysql,
                                                    mincached=5,
                                                    maxcached=10,
                                                    maxshared=5,
                                                    maxconnections=20,
                                                    host="127.0.0.1",
                                                    port=3306,
                                                    user="root",
                                                    passwd="123456",
                                                    db="http_server_python3",
                                                    charset="utf8");
        connection = Pool.__pool.connection();
        return connection;
