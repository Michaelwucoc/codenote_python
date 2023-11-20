import getpass #导入getpass函数包
from datetime import date #从datetime函数中导入date

username = getpass.getuser() #定义用户名的变量，使用getpass函数拿到用户名，储存在username 变量中
current_date = date.today() #使用date函数获得日期，储存在current_date里面


print("Hello,",username,",Today is:",current_date) #打印结果，不使用双引号代表打印变量。