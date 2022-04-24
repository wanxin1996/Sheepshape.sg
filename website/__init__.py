from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['secret_key'] = 'wxyz'

    # register the views into the app, so when run app, main know run views to display the website
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app