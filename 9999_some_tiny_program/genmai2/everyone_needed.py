"""
写一些总是要用到的方法
"""

"""
用户名需要经过判断存入数据库，why？
因为用户名往往是明文存的，why？
因为你总不能在页面上显示用户名的时候，是一串你也不认识用户也不认识的加密之后的乱码吧？
这是也为什么密码不需要处理的原因。
密码往往是通过加密之后保存进数据库的，一般不会出现注入的情况。
"""
# ^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[.])(?=.*[@])).*$
# 判断字符串是否带有特殊参数，防止注入
import re



def test_inject_sql_username_string(username):
    # 这个正则意味着这个字符串中只有大写字母、小写字母、数字、点、下划线、@ ，五种类型的字符串
    partten = '^[a-zA-Z0-9_.@]*$'
    if re.match(partten, username) == None:
        # 当match返回到None的时候，说明不符合这个正则，也就是说有其他的特殊字符
        # 返回True，告诉调用的，这是一个不应该被信任的字符串
        return True
    else:
        # 有匹配到，说明这个字符串只有上面说的五种字符，返回False，说明这个字符串可以被相信
        return False
