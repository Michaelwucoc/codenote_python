import random #引入随机函数
x = random.randint(1,100) #使用随机函数来随机一个1-100之间的数字
i = 0 #验证
while i < 100: #验证
    y = input("Please enter the Number") #输入y
    if x == y: #判断x是否等于y
        print ("You are correct! Bingo!")
        break #结束程序
    elif y < x: #判断值
        print ("The number you guessed is too small! Try again")
    else:
        print ("The number you guessed is too big! Try again!")
