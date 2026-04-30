import http.server
import socketserver
import os
import socket

PORT = int(os.environ.get("PORT", "8000"))
HOSTNAME = socket.gethostname()
VERSION = os.environ.get("APP_VERSION", "v1")


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        body = (
            f"hello from {HOSTNAME} ({VERSION})\n"
            f"path: {self.path}\n"
        ).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        return


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"serving on :{PORT}", flush=True)
    httpd.serve_forever()
