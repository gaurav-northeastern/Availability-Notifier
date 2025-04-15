from flask import Flask
from flask_cors import CORS
from controller import register_routes

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})  # ← this is the fix
    register_routes(app)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
