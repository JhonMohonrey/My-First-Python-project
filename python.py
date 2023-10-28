print("Welcome")

status = "running"
loginSection = "1"
adminUserName = "user"
adminUserPass = "admin"
LoopCount = "False"

while status != "2" :
    print("---------(Home Page)---------")
    print("1: Login")
    print("2: Exit")
    print("Please Enter")
    user = input("")
    exitCode = "2"

    if user == exitCode :
        print("Exit Successful")
        newStatus = "2"
        status = newStatus

    if user != "1" :
        print("Invalid key: " + user)

    while user == loginSection : 
        isLogin = "True"

        if isLogin == "True": 
            print("Login your account")
            print("username:")
            username = input("")
            print("password")
            password = input("")

            if username == adminUserName and password == adminUserPass :
                print("Login Successful")
                updateStatus = "Main"
                isLogin = updateStatus

            else :
                print("Try again")
                print("username or password incorrect")
                updateStatus = "True"
                isLogin = updateStatus
        
            while isLogin == "Main" :
                print("welcome Main Page")
                print("1: Chat")
                print("2: upload")
                print("3: exit")
                loginUser = input("")
                Data = loginUser
                
                while Data != "3":
                    print("Invalid Try again")
                    break
                while Data == "3" :
                    isLogin = "userExit"
                    user = "none"
                    break
        else :
            isLogin = "True"