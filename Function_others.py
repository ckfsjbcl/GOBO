import os
import time

import yaml
from colorama import init, Fore

import random
import HttpService


def time_get():
    # used to get time
    time_return = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return f"[{time_return}]"


class config_in():
    def __init__(self):  # 初始化配置文件
        # 获取当前文件的Realpath
        fileNamePath = os.path.split(os.path.realpath(__file__))[0]
        # 获取配置文件的路径
        yamlPath = os.path.join(fileNamePath, 'config.yml')
        with open(yamlPath, 'r', encoding='utf-8') as f:
            cont = f.read()
            data = yaml.load(cont, Loader=yaml.SafeLoader)

            self.HTTP_CONTROL = data["HTTP_CONTROL"]
            self.debugforhttphandle = self.HTTP_CONTROL["debugforhttphandle"]

            self.Plugins_in = data["Plugins_in"]
            self.Openpluginintroductionbroadcast = self.Plugins_in["Openpluginintroductionbroadcast"]
            self.Automaticreplytosubsequentfunctionexecution = self.Plugins_in["Automaticreplytosubsequentfunctionexecution"]

            # TODO TO BE CONTINUE

    def exam(self):
        pass
    # TODO to ensure the integrity of the configuration file


def sand_out(msg, type, GOBO, war_msg=''):  # type=warning or INFO
    if type == "INFO":
        if GOBO.message_type == "private":  # TODO 用户名称还是qq号？
            msg_out = f"[{time_get()}] [{type}] 收到一条来自用户{GOBO.user_id}的消息:{GOBO.message}"
            return_msg = HttpService.send_private_msg(GOBO.user_id, GOBO.message)
            return return_msg
        elif GOBO.message_type == "group":
            msg_out = f"[{time_get()}] [{type}] 收到一条来自群{GOBO.group_id}中用户{GOBO.user_id}的消息:{GOBO.message}"
            return_msg = HttpService.send_group_msg(GOBO.group_id, msg_out)
            return return_msg
    elif type == "WARNING":
        init()
        print("----------------")
        print(Fore.RED, 'WARNING:')
        print(war_msg)
        print("----------------")


#消息等待池
class msg_wait():
    def __init__(self):
        self.msg_pool={}
    def add_msg(self,get_msg,plugin_name,func_name='wait',type=0):
        self.msg_pool[plugin_name]=get_msg


#tag
class tag():
    def __init__(self):
        self.tag_pool=[]
    def add_tag(self,msg_in):
        self.tag_pool.append(msg_in)
    def show_tag(self):
        print(self.tag_pool)
    def del_tag(self,msg,num=None):
        if num is None:
            self.tag_pool.pop(msg)
        else:
            del self.tag_pool[num]
    #TODO ERROR

a=tag
a.add_tag("aaa")