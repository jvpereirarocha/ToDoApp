from flask import Flask

from app.apis import api_bp


def create_app(environment: str):
    app = Flask(__name__)
    app.config.from_object(
        f"app.configs.{environment}.{environment.capitalize()}Config"
    )
    app.register_blueprint(api_bp)

    return app
