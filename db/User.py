
import json as Json;

class User:
    __id = 0;
    __username = "";
    __password = "";

    def getId(self):
        return self.__id;

    def setId(self, id):
        self.__id = id;

    def getUsername(self):
        return self.__username;

    def setUsername(self, username):
        self.__username = username;

    def getPassword(self):
        return self.__password;

    def setPassword(self,password):
        self.__password = password;