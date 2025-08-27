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

@view_config(route_name='temp1', renderer='template/first.jinja2')
def template1(request):
    return {}

@view_config(route_name='temp2', renderer='template/second.jinja2')
def template2(request):
    return {}

c = Configurator()
c.include('pyramid_jinja2')
c.add_route('first','/')
c.add_route('second', '/sec')
c.add_route('temp1','t1')
c.add_route('temp2','t2')

c.scan()
app = c.make_wsgi_app()
s = make_server('localhost',6543,app)
s.serve_forever()
