import http.server
import socketserver
import os
import io
import thread
import time

def main(): #Main function, starts web server on localhost
    PORT = 80

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print ("serving at port: ", PORT)

        httpd.serve_forever()

main()
