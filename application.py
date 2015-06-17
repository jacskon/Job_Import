'''
Created on Mar 26, 2012

@author: Steve Cassidy
'''

from wsgiref import simple_server
import cgi

import templating
import xml_dump

def application(environ, start_response):
    """Top level WSGI application entry point for the login
    web application. Dispatches to another WSGI application
    based on the URL in PATH_INFO"""

    #LOGIN PAGE
    #Define the format for the standard page
    headers = [('content-type', 'text/html')]
    content = {'content': templating.XML_THROW}
    #grab the values from the form
    form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
    excel = form.getvalue("excel", "")
    if form.has_key('excel'):
        excel_string = form.getvalue("excel", "")
        xml_dump.xml_build(excel_string)
        result = xml_dump.xml_build(excel_string)
        print result
        #Redirect to the home page and provide a link to download the XML
        content = {'content': templating.XML_RETURN}
        start_response('200 OK', headers)
        return [templating.generate_page("Your XML file is ready", content, templating.PAGE_TEMPLATE)]
    #Return the basic Login Page while no data is submitted
    else:
        start_response('200 OK', headers)
        return [templating.generate_page("Upload your excel excerpt", content, templating.PAGE_TEMPLATE)]


if __name__ == '__main__':

    server = simple_server.make_server('localhost', 8080, application)
    print "Listening on http://localhost:8080/"
    server.serve_forever()
