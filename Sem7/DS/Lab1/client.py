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
    else:
        print("Invalid operation")
        continue
    print(f"result: {result}")
