
import  json as Json;

class DefaultController:
    def index(self):
        response = Json.loads("{}");
        response["content"] = "index";
        return Json.dumps(response);