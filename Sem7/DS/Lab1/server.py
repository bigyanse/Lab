from xmlrpc.server import SimpleXMLRPCServer

users = {
        "admin": "12345"
}

class display:
    def show(self, name, roll):
        detail = f"My name is {name} and roll number is {roll}"
        return detail

    def register(self, email, password):
        if email in users:
            return "already registered"
        users[email] = password
        return "success"

    def login(self, email, password):
        if email in users:
            if users[email] == password:
                return "success"
            else:
                return "invalid email or password"
        else:
            return "invalid email or password"


server = SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(display())
server.serve_forever()
