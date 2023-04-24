from flask_app.controllers import blogs_control
from flask_app import app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)