## http://docs.python.org/library/wsgiref.html
"""Works with
  * CPython 2.7, 3.6.1, and 3.8.10
  * Jython 2.7.0 and 2.5.1
"""

try:
    # Python 3.8 and later
    # py3
    from html import escape as escape_html
except ImportError:
    # py2
    from cgi import escape as escape_html

import os
import sys
from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

#from remote_pdb import RemotePdb  # https://github.com/ionelmc/python-remote-pdb


def cutoff(s, n=100):
    if len(s) > n: return s[:n]+ '.. cut ..'
    return s


# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
def simple_app(environ, start_response):
    #RemotePdb('127.0.0.1', 4444).set_trace()
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]

    start_response(status, headers)

    ret = []
    ret += [('Python %s on %s\n\n' % (sys.version, sys.platform)).encode('utf-8')]
    ret += ['web environ\n'.encode('utf-8')]
    ret += ["<table border='1'>".encode('utf-8')]
    ret += [("<tr><td>%s</td><td>%s</td></tr>\n" % (key, escape_html(cutoff(str(value))))).encode("utf-8")
           for key, value in environ.items()]
    ret += ["</table>".encode('utf-8')]

    ret += ['\n'.encode('utf-8')]
    ret += ['\n'.encode('utf-8')]
    ret += ['os environ\n'.encode('utf-8')]
    ret += ["<table border='1'>".encode('utf-8')]
    ret += [("<tr><td>%s</td><td>%s</td></tr>\n" % (key, escape_html(cutoff(str(value))))).encode("utf-8")
           for key, value in os.environ.items()]
    ret += ["</table>".encode('utf-8')]
    return ret


def main(argv=None):
    if argv is None:
        argv = sys.argv

    print('Python %s on %s' % (sys.version, sys.platform))
    server_port = int(os.environ.get('PORT', 8000))

    httpd = make_server('', server_port, simple_app)
    print("Serving on http://localhost:%d" % server_port)
    print("should be accessible externally, not only on localhost interface")
    httpd.serve_forever()
    return 0

if __name__ == "__main__":
    sys.exit(main())
