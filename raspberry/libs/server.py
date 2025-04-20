from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading

commands = []
mux = threading.Lock()

def complete_command():
    mux.acquire()
    commands.pop(0)
    commands.pop(0)
    mux.release()

def get_command():
    mux.acquire()
    if len(commands) != 0:
        command, time = commands[0], commands[1]
        mux.release()
        return command, float(time)
    mux.release()

class CommandHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        mux.acquire()
        commands.append(post_data.decode())
        mux.release()

        print(f"hello {commands}")
        
        self.send_response(200)
        self.send_header('Content-type', 'text')
        self.end_headers()
        response = commands[0]
        self.wfile.write(response.encode('utf-8'))

def run(ip = "0.0.0.0", port: int = 8080):
    server_address = (ip, port)
    httpd = HTTPServer(server_address, CommandHandler)

    print(f"Starting server on port {port}...")
    httpd.serve_forever()