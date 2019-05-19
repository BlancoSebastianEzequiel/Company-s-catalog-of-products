import os
import json
import json
from flask import Flask
from server.libs.mongo import JSONEncoder
from server.logger import logger

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

LOG = logger.get_root_logger(
    os.environ.get('ROOT_LOGGER', 'root'),
    filename=os.path.join(ROOT_PATH, 'output.log')
)


def post_admin_users(app):
    client = app.test_client()
    with open('server/admin.json', encoding='utf-8-sig') as json_file:
        text = json_file.read()
        admin_users = json.loads(text)
        for admin in admin_users:
            client.post(
                '/users/',
                data=json.dumps(admin),
                content_type='application/json'
            )


def create_app(conf='conf.local.Config'):
    LOG.info('running environment: %s', os.environ.get('ENV'))
    # Debug mode if development env
    app = Flask(__name__)

    app.config.from_object(conf)

    from server.libs.mongo import MONGO

    MONGO.init_app(app)

    from server.routes.root import EXAMPLE_BP
    from server.routes.ping import PING_BP
    from server.routes.users import USER_BP
    from server.routes.session import SESSION_BP

    app.register_blueprint(EXAMPLE_BP)
    app.register_blueprint(PING_BP)
    app.register_blueprint(USER_BP)
    app.register_blueprint(SESSION_BP)
    # use the modified encoder class to handle ObjectId and Datetime object
    # while jsonifying the response
    app.json_encoder = JSONEncoder

    post_admin_users(app)

    return app
