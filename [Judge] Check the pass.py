i = 0 #进入循环
x = 12345678 #密码
while i == 0:
    y = int (input("Please enter the password. \n")) #要求用户输入
    if x == y: #判断
        print ("Logged in to the server.") #成功输出
        break #退出程序
    else:
        print ("Password incorrect. Please try again.") 
