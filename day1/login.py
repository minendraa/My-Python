username="admin"
password="1234"
print("-----Login Sytem------")
inputusername=input("Enter the username: ")
inputpassword=input("enter the password: ")

if(inputusername==username and inputpassword==password):
    print("Access Granted")
else:
    print("Invalid username or password.")