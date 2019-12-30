
import  json as Json;

import service.UserService as UserService;

userService = UserService.UserService();

class UserController:
    def login(self,request):
        user = request.json;
        if user != None:
            userCorrect = userService.getUserByUsername(user["username"]);
            response = {};
            if userCorrect != None and \
                    user["password"] == userCorrect.getPassword() :
                response["result"] = "success";
            else:
                response["result"] = "failed";
            return Json.dumps(response);
        else:
            return "";

    def users(self):
        users = userService.allUsers();
        response = [];
        for user in users:
            userItem = {};
            userItem["id"] = user.getId();
            userItem["username"] = user.getUsername();
            userItem["password"] = user.getPassword();
            response.append(userItem);
        return Json.dumps(response);
