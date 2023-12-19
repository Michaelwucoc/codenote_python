def access_control(visitor_identity, visit_time):
    # 判断访客身份是否是员工
    if visitor_identity == "员工":
        # 判断访问时间是否在工作时间范围内
        if 8 <= visit_time <= 18:
            return True
        else:
            return False
    # 判断访客身份是否是访客
    elif visitor_identity == "访客":
        # 判断访问时间是否在访客时间范围内
        if 9 <= visit_time <= 20:
            return True
        else:
            return False
    else:
        return False

# 使用函数，并输出相应的信息
visitor_identity = input("请输入访客身份（员工/访客）：")
visit_time = int(input("请输入访问时间（24小时制，例如：9代表上午9点）："))

if access_control(visitor_identity, visit_time):
    print("允许进入")
else:
    print("禁止进入")
