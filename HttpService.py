import requests

import Function_others

# 加载配置文件
config = Function_others.config_in()
debugforhttphandle = config.debugforhttphandle

"""
FIRST PART:
    used to post http requests
"""


# 发送私聊信息
def send_private_msg(user_id, message, group_id='', auto_escape='False'):
    user_id = str(user_id)
    message = str(message)
    group_id = str(group_id)
    if group_id == '':  # 私聊
        sand_message_user = "http://127.0.0.1:5700/" + "send_private_msg?" + "user_id=" + user_id + "&" + "message=" + message + "&" + "auto_ecscape=" + auto_escape
        return_user = requests.post(sand_message_user)
    else:  # 通过群发
        sand_message_user = "http://127.0.0.1:5700/" + "send_private_msg?" + "user_id=" + user_id + "&" + "group_id=" + group_id + "&" + "message=" + message + "&" + "auto_ecscape=" + auto_escape
        return_user = requests.post(sand_message_user)
    return return_user


# 发送群信息
def send_group_msg(group_id, message, auto_escape=''):
    group_id = str(group_id)
    message = str(message)
    sand_message_user = "http://127.0.0.1:5700/" + "send_group_msg?" + "group_id=" + group_id + "&" + "message=" + message + "&" + "auto_ecscape=" + auto_escape
    return_user = requests.post(sand_message_user)
    return return_user


# 发送合并转发 ( 群 )
def send_group_forward_msg(group_id, messages):
    sand_message_user = "http://127.0.0.1:5700/" + "send_group_forward_msg?" + "group_id=" + str(
        group_id) + "&" + "message=" + str(messages)
    return_user = requests.post(sand_message_user)
    return return_user


# 发送消息
# 此模式不常用,请尽量不要引用
def send_msg(message, user_id='', group_id='', message_type='', auto_escape=''):
    if group_id == '':  # 私聊
        sand_message_user = "http://127.0.0.1:5700/" + "send_private_msg?" + "user_id=" + str(
            user_id) + "&" + "message=" + str(message) + "&" + "auto_ecscape=" + str(auto_escape)
        return_user = requests.post(sand_message_user)
    else:  # 通过群发
        sand_message_user = "http://127.0.0.1:5700/" + "send_private_msg?" + "user_id=" + str(
            user_id) + "&" + "group_id=" + str(group_id) + "&" + "message=" + str(
            message) + "&" + "auto_ecscape=" + str(auto_escape)
        return_user = requests.post(sand_message_user)
    return return_user


# 撤回消息
def delete_msg(message_id):
    message_id = str(message_id)
    sand_message_user = "http://127.0.0.1:5700/" + "delete_msg?" + "message_id=" + message_id
    return_user = requests.post(sand_message_user)
    return return_user


# 获取消息
def get_msg(message_id):
    message_id = str(message_id)
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_kick?" + "message_id=" + message_id
    return_user = requests.post(sand_message_user)
    return return_user
    # 这里是json信息，需要解析


"""
响应数据
字段	类型	说明
message_id	int32	消息id
real_id	int32	消息真实id
sender	object	发送者
time	int32	发送时间
message	message	消息内容
raw_message	message	原始消息内容
"""


# 获取合并转发内容
def get_forward_msg(message_id):
    message_id = str(message_id)
    sand_message_user = "http://127.0.0.1:5700/" + "get_forward_msg?" + "message_id=" + message_id
    return_user = requests.post(sand_message_user)
    return return_user
    # 此处同上


# 获取图片信息
def get_image(file):
    file = str(file)
    sand_message_user = "http://127.0.0.1:5700/" + "get_image?" + "file=" + file
    return_user = requests.post(sand_message_user)
    return return_user


# 群组踢人
def set_group_kick(group_id, user_id, reject_add_request='false'):
    group_id = str(group_id)
    user_id = str(user_id)
    reject_add_request = str(reject_add_request)
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_kick?" + "group_if=" + group_id + "&" + "user_id=" + user_id + "&" + "reject_add_request=" + reject_add_request
    return_user = requests.post(sand_message_user)
    return return_user


# 群组单人禁言
def set_group_ban(group_id, user_id, duration='30 * 60'):  # 最后一个参数为禁言时间，单位s，0秒表示取消禁言
    group_id = str(group_id)
    user_id = str(user_id)
    duration = str(duration)
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_ban?" + "group_id=" + group_id + "&" + "user_id=" + user_id + "&" + "duration=" + duration
    return_user = requests.post(sand_message_user)
    return return_user
    # 无响应数据


# 群组匿名用户禁言
def set_group_anonymous_ban(group_id, duration='', anonymous='30 * 60', flag='',
                            anonymous_flag=''):  # anonymous，anonymous_flag或flag效果相同，只需择其一即可,若都传入,则使用 anonymous,推荐使用anonymous,禁言时长单位秒
    group_id = str(group_id)
    try:
        duration = str(duration)
    except:
        pass
    try:
        duration = str(flag)
    except:
        pass
    try:
        duration = str(anonymous_flag)
    except:
        pass
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_anonymous_ban?" + "group_id=" + group_id + "&" + "anonymous=" + anonymous + "&" + "duration=" + duration
    return_user = requests.post(sand_message_user)
    return return_user
    # 无响应数据


# 群组全员禁言
def set_group_whole_ban(group_id, enable='true'):
    group_id = str(group_id)
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_whole_ban?" + "group_id=" + group_id + "&" + "enable=" + enable
    return_user = requests.post(sand_message_user)
    return return_user
    # 无响应数据


# 群组设置管理员
def set_group_admin(group_id, user_id, enable='true'):
    group_id = str(group_id)
    user_id = str(user_id)
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_admin?" + "group_id=" + group_id + "&" + "user_id=" + user_id + "&" + "enable=" + enable
    return_user = requests.post(sand_message_user)
    return return_user
    # 无响应数据


# 群组匿名
"""暂不支持"""


def set_group_anonymous(group_id, enable='true'):
    group_id = str(group_id)
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_anonymous?" + "group_id=" + group_id + "&" + "enable=" + enable
    return_user = requests.post(sand_message_user)
    return return_user
    # 无响应数据


# 设置群名片 ( 群备注 )
def set_group_card(group_id, user_id, card=''):  # card群名片内容, 不填或空字符串表示删除群名片
    group_id = str(group_id)
    user_id = str(user_id)
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_card?" + "group_id=" + group_id + "&" + "user_id=" + user_id + "&" + "card=" + card
    return_user = requests.post(sand_message_user)
    return return_user
    # 无响应数据


# 设置群名
def set_group_name(group_id, group_name):
    group_id = str(group_id)
    group_name = str(group_name)
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_name?" + "group_id=" + group_id + "&" + "group_name=" + group_name
    return_user = requests.post(sand_message_user)
    return return_user
    # 无响应数据


# 退出群组
def set_group_leave(group_id, is_dismiss='false'):
    group_id = str(group_id)
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_name?" + "group_id=" + group_id + "&" + "is_dismiss=" + is_dismiss
    return_user = requests.post(sand_message_user)
    return return_user
    # 无响应数据


"""
SECONDE PART:
    used to handle http_get
"""

global msg_in


# 实例化对象
class HTTP_CONTROL():
    def __init__(self, msg_in):
        if msg_in["message_type"] == "private":
            self.init_handle_private(msg_in)
        elif msg_in["message_type"] == "group":
            self.init_handle_group(msg_in)

    def init_handle_private(self, msg_in):  # 初始化处理，方便调用
        try:
            self.time = msg_in["time"]
        except:
            pass
        try:
            self.self_id = msg_in["self_id"]
        except:
            pass
        try:
            self.post_type = msg_in["post_type"]
        except:
            pass
        try:
            self.message_type = msg_in["message_type"]
        except:
            pass
        try:
            self.sub_type = msg_in["sub_type"]
        except:
            pass
        try:
            self.temp_source = msg_in["temp_source"]
        except:
            pass
        try:
            self.message_id = msg_in["message_id"]
        except:
            pass
        try:
            self.user_id = msg_in["user_id"]
        except:
            pass
        try:
            self.message = msg_in["message"]
        except:
            pass
        try:
            self.font = msg_in["font"]
        except:
            pass
        try:
            self.sender = msg_in["sender"]
        except:
            pass
        try:
            self.nickname = self.sender["nickname"]
            self.sex = self.sender["sex"]
            self.age = self.sender["age"]
        except:
            if debugforhttphandle is True:
                print('FAIL TO INIT_HANDLE THE SENDER')
            else:
                pass

    def init_handle_group(self, msg_in):
        try:
            self.time = msg_in["time"]
        except:
            pass
        try:
            self.self_id = msg_in["self_id"]
        except:
            pass
        try:
            self.post_type = msg_in["post_type"]
        except:
            pass
        try:
            self.message_type = msg_in["message_type"]
        except:
            pass
        try:
            self.sub_type = msg_in["sub_type"]
        except:
            pass
        try:
            self.message_id = msg_in["message_id"]
        except:
            pass
        try:            
            self.group_id = msg_in["group_id"]
        except:
            pass
        try:
            self.user_id = msg_in["user_id"]
        except:
            pass
        try:
            self.anonymous = msg_in["anonymous"]
        except:
            pass
        try:  
            self.message = msg_in["message"]
        except:
            pass
        try:
            self.raw_message = msg_in["raw_message"]
        except:
            pass
        try:
            self.font = msg_in["font"]
        except:
            pass
        try:
            self.sender = msg_in["sender"]
        except:
            pass
        try:
            self.anonymous_id = self.anonymous["id"]
            self.anonymous_name = self.anonymous["name"]
            self.anonymous_name = self.anonymous["name"]

            self.nickname = self.sender["nickname"]
            self.card = self.sender["card"]
            self.sex = self.sender["sex"]
            self.age = self.sender["age"]
            self.area = self.sender["area"]
            self.level = self.sender["level"]
            self.role = self.sender["role"]
            self.title = self.sender["title"]
        except:
            if debugforhttphandle is True:
                print('FAIL TO INIT_HANDLE THE SENDER')
            else:
                pass
