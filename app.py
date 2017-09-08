# PEP 3333 -- Python Web Server Gateway Interface v1.0.1 | Python.org
# https://www.python.org/dev/peps/pep-3333/
def application(environ, start_response):
  status = '200 OK'
  headers = [('Content-type', 'text/plain; charset=utf-8')]
  body = 'hello, world'.encode('utf-8')
  start_response(status, headers)
  return [body]

# 21.4. wsgiref — WSGI Utilities and Reference Implementation — Python 3.6.2 documentation
# https://docs.python.org/3/library/wsgiref.html
from wsgiref import simple_server
if __name__ == '__main__':
  host = ''
  port = 8000
  app = application
  server = simple_server.make_server(host, port, app)
  server.serve_forever()

