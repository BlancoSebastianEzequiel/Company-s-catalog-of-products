import os

from server import create_app

# pylint: disable=C0103
env = os.environ.get('ENV', 'development')
conf = 'conf.prod.Config' if env == 'production' else 'conf.local.Config'
app = create_app(conf)
