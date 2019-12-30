
import pymysql;
import db.User as User;

# Connect to the database
# do not need to close , it alive all the lifecycle
connection = pymysql.connect(host="127.0.0.1",
                             user="root",
                             password="652719p",
                             db="python_httpdemo");
cursor = connection.cursor();

class UserService:
    def getUserByUsername(self,username):
        sql = "select * from user where username='{0}';".format(username);
        cursor.execute(sql);
        data = cursor.fetchone();
        if data != None:
            user = User.User();
            user.setId(data[0]);
            user.setUsername(data[1]);
            user.setPassword(data[2]);
            return user;
        else:
            return None;

    def allUsers(self):
        users = [];
        sql = "select * from user;";
        cursor.execute(sql);
        data = cursor.fetchone();
        while data != None:
            user = User.User();
            user.setId(data[0]);
            user.setUsername(data[1]);
            user.setPassword(data[2]);
            users.append(user);
            data = cursor.fetchone();
        return users;
