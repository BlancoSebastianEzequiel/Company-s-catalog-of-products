import json
import os
from flask import Flask
from server.libs.mongo import JSONEncoder
from server.logger import logger

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

LOG = logger.get_root_logger(
    os.environ.get('ROOT_LOGGER', 'root'),
    filename=os.path.join(ROOT_PATH, 'output.log')
)


def post_admin_users():
    from server.controller.users import UsersController
    if not UsersController.is_empty():
        return
    with open('server/admin.json', encoding='utf-8-sig') as json_file:
        text = json_file.read()
        admin_users = json.loads(text)
        for admin in admin_users:
            UsersController.post(admin)


def post_company_data():
    from server.controller.company_data import CompanyDataController
    if not CompanyDataController.is_empty():
        return
    with open('server/company_data.json', encoding='utf-8-sig') as json_file:
        text = json_file.read()
        data = json.loads(text)
        CompanyDataController.post(data)


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
    from server.routes.active_principle import ACTIVE_PRINCIPLE_BP
    from server.routes.pasword_recovery import PASSWORD_RECOVERY_BP
    from server.routes.products import PRODUCTS_BP
    from server.routes.company_data import COMPANY_DATA_BP
    from server.routes.help_module import HELP_MODULE_BP
    from server.routes.contact_us import CONTACT_US_BP

    app.register_blueprint(EXAMPLE_BP)
    app.register_blueprint(PING_BP)
    app.register_blueprint(USER_BP)
    app.register_blueprint(SESSION_BP)
    app.register_blueprint(ACTIVE_PRINCIPLE_BP)
    app.register_blueprint(PASSWORD_RECOVERY_BP)
    app.register_blueprint(PRODUCTS_BP)
    app.register_blueprint(COMPANY_DATA_BP)
    app.register_blueprint(HELP_MODULE_BP)
    app.register_blueprint(CONTACT_US_BP)
    # use the modified encoder class to handle ObjectId and Datetime object
    # while jsonifying the response
    app.json_encoder = JSONEncoder

    post_admin_users()
    post_company_data()

    return app
