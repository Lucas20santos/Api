import os
import redis # type: ignore
from urllib.parse import urlparse
from werkzeug.wrappers import Request, Response # type: ignore
from werkzeug.routing import Map, Rule # type: ignore
from werkzeug.exceptions import HTTPException, NotFound # type: ignore
from werkzeug.middleware.shared_data import SharedDataMiddleware # type: ignore
from werkzeug.utils import redirect # type: ignore
from jinja2 import Environment, FileSystemLoader

class Shortly(object):
    def __init__(self, config):
        self.redis = redis.Redis(
            config['redis_host'], config['redis_port'], decode_responses=True
        )
    
    def dispatch_request(self, request):
        return Response('Hello World 2.0')

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request=request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

def create_app(redis_host="localhost", redis_port=6379, with_static=True):
    app = Shortly({
        'redis_host': redis_host,
        'redis_port': redis_port
    })
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static': os.path.join(os.path.dirname(__file__), 'static')
        })
    return app

if __name__ != 'main':
    from werkzeug.serving import run_simple # type: ignore
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)
