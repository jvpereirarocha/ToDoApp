from os import getenv

from app.factory import create_app

ENV = getenv("FLASK_ENV")

if __name__ == "__main__":
    app = create_app(environment=ENV)

    debug = app.config.get("DEBUG")
    port = app.config.get("PORT")
    
    app.run(debug=debug, port=port)