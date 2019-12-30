
import flask;

import controller.DefaultController as DefaultController;
import controller.UserController as UserController;

app = flask.Flask(__name__);

# init controllers
defaultController = DefaultController.DefaultController();
userController = UserController.UserController();

# config request mapper
@app.route("/",methods=['GET', 'POST'])
def index():
    return defaultController.index();

@app.route("/login",methods=['GET', 'POST'])
def login():
    return userController.login(flask.request);

@app.route("/users",methods=['GET', 'POST'])
def users():
    return userController.users();

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True);
