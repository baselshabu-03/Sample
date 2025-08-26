from wsgiref.simple_server import make_server
from pyramid.response import Response
from pyramid.config import Configurator
from pyramid.view import view_config

@view_config(route_name='first')
def display(request):
    return Response("Welcome to Sector - 6174")

@view_config(route_name='second')
def show(request):
    return Response("Welcome to Sector - 1111")

c = Configurator()
c.add_route('first','/')
c.add_route('second', '/sec')

c.scan()
app = c.make_wsgi_app()
s = make_server('localhost',6543,app)
s.serve_forever()
