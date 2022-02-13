import logging
import logging.config
import time
import io

from pyms.flask.app import Microservice
from flask import Flask, jsonify, request
from flask_restful import Resource
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask import send_file

app = Flask(__name__)

logging.basicConfig(filename='E:/Ertino/logs/demo.log', level=logging.DEBUG)
logger = logging.getLogger("myapp.sqltime")


@event.listens_for(Engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement, parameters, *args, **kwargs):
    conn.info.setdefault('query_start_time', []).append(time.time())
    logger.debug("Start Query: %s, %s [%s]", statement, parameters, cursor)


@event.listens_for(Engine, "after_cursor_execute")
def after_cursor_execute(conn, *args, **kwargs):
    total = time.time() - conn.info['query_start_time'].pop(-1)
    logger.debug("Query Complete!")
    logger.debug("Total Time: %f", total)


class MyMicroservice(Microservice):
    def init_libs(self):
        db.init_app(self.application)
        with self.application.test_request_context():
            db.create_all()

    def init_logger(self) -> None:
        if not self.application.config["DEBUG"]:
            super()
        else:
            level = "DEBUG"
            LOGGING = {
                'version': 1,
                'disable_existing_loggers': False,
                'handlers': {
                    'console': {
                        'level': level,
                        'class': 'logging.StreamHandler',
                    },
                },
                'loggers': {
                    '': {
                        'handlers': ['console'],
                        'level': level,
                        'propagate': True,
                    },
                    'anyconfig': {
                        'handlers': ['console'],
                        'level': level,
                        'propagate': True,
                    },
                    'pyms': {
                        'handlers': ['console'],
                        'level': "WARNING",
                        'propagate': True,
                    },
                    'root': {
                        'handlers': ['console'],
                        'level': level,
                        'propagate': True,
                    },
                }
            }

            logging.config.dictConfig(LOGGING)


def create_app():
    """Initialize the Flask app, register blueprints and intialize all libraries like Swagger, database, the trace system...
    return the app and the database objects.
    :return:
    """
    ms = MyMicroservice(service="ms", path=__file__)
    return ms.create_app()

@app.route('/ml/process', methods=['POST'])
def process():
    inputimagedir = request.form.get('inputimagedir')
    
    return inputimagedir


# driver function
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)