import xmlrpc.client

client = xmlrpc.client.ServerProxy("http://localhost:8000/")

print("client ready, type and press enter key")

while True:
    print("enter operation to perform(display and exit)")
    operation = input().lower()
    if operation == "exit":
        break
    if operation == "display":
        param1 = input("Enter your name")
        param2 = input("Enter your address:")
        result = client.show(param1, param2)
        print(f"result {result}")
    elif operation == "login":
        email = input("Email: ")
        password = input("Password: ")
        status = client.login(email, password)
        if status == "success":
            print("logging in")
        else:
            print(status)
    elif operation == "register":
        email = input("Email: ")
        password = input("Password: ")
        status = client.register(email, password)
        if status == "success":
            print("registering user")
        else:
            print(status)
    else:
        print("Invalid operation")
        continue
