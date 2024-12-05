from xmlrpc.server import SimpleXMLRPCServer
import math

host = "127.0.0.32"
port = 12345

with SimpleXMLRPCServer((host, port)) as server:

    def get_sqrt_of_discriminant(a, b, c):
        return math.sqrt(b * b - 4 * a * c)

    server.register_function(get_sqrt_of_discriminant)
    server.serve_forever()
