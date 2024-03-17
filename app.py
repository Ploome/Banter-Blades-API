from flask import Flask, jsonify, request
from flask_cors import CORS
from database import db
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, JWTManager


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\nickp\\OneDrive\\Documents\\API\\Banter-Blades-API\\app_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'NicksDickIsHuge'  # Set this to your JWT secret key

    # Initialize DB with app
    db.init_app(app)
    
    # Apply CORS to this app instance
    CORS(app)

    jwt = JWTManager(app)

    with app.app_context():
        db.create_all()

    # Assume the rest of your app routes and logic remain the same
    
    return app

# Use create_app to get the app instance
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)