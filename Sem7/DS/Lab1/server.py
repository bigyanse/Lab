from xmlrpc.server import SimpleXMLRPCServer

class display:
    def show(self, name, roll):
        detail = f"My name is {name} and roll number is {roll}"
        return detail


server = SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(display())
server.serve_forever()
