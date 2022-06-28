
import flask;
import flask_cors;

import controller.DefaultController as DefaultController;
import controller.UserController as UserController;
import controller.DoorController as DoorController;
import controller.FileController as FileController;

app = flask.Flask(__name__);
flask_cors.CORS(app,supports_credentials=True);
app.register_blueprint(DefaultController.blueprint);
app.register_blueprint(UserController.blueprint);
app.register_blueprint(DoorController.blueprint);
app.register_blueprint(FileController.blueprint);

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True);
