'''
    application test code:
        mysql test
        redis test
        verify code test
'''

import json as Json;

import db.MysqlPool as MysqlPool;
import db.RedisPool as RedisPool;
import util.VerifyCodeUtil as VerifyCodeUtil;

def mysqlTest():
    sql = "select * from user where id=1;";
    connection = MysqlPool.Pool.getConnection();
    cursor = connection.cursor();
    cursor.execute(sql);
    data = cursor.fetchone();
    print(data);

def redisTest():
    connection = RedisPool.Pool.getConnection();
    connection.set("test","redis test",ex=120);
    test = connection.get("test");
    print(test);

if __name__ == "__main__":
    # mysqlTest();
    # redisTest();
    print(Json.dumps(VerifyCodeUtil.Util.verifyCode(1,6,"D:/code.jpg")));
