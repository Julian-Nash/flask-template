from app import create_app
import os

flask_env = os.getenv("FLASK_ENV")
app = create_app(flask_env)

if __name__ == "__main__":
    app.run()