# TODO to input plugings
import importlib
import json
import os
import Function_others
import HttpService

# 加载配置文件
config = Function_others.config_in()
Openpluginintroductionbroadcast = config.Openpluginintroductionbroadcast
Automaticreplytosubsequentfunctionexecution=config.Automaticreplytosubsequentfunctionexecution



global bool_plugins_in
global plugins_list

class Plugins_in():
    def __init__(self):
        self.plugins_list = []
        plugins_list=self.plugins_list
        bool_plugins_in = True
        # 加载插件
        for root_1, dirs_1, files_1 in os.walk(os.path.join(os.path.dirname(__file__), 'plugins')):
            for dirs in dirs_1:
                if dirs == '__pycache__':
                    pass
                else:
                    for root_2, dirs_2, files_2 in os.walk(os.path.join(root_1, dirs)):
                        for file in files_2:
                            if file == '__init__.py':
                                pass
                            elif file == 'README.md':
                                if Openpluginintroductionbroadcast is True:
                                    with open(os.path.join(root_2, 'README.md'), 'r') as re:
                                        msg = re.read()
                                        print("----------------")
                                        print(f"HERE IS {file}")
                                        print(f"来自{dirs}")
                                        print(msg)
                                        print("----------------")
                                else:
                                    pass
                            elif file == '__pycache__':
                                pass
                            else:
                                model = importlib.import_module(f'plugins.{dirs}.func')
                                self.plugins_list.append(dirs)
                                if bool_plugins_in is True:
                                    model.start()
                                    bool_plugins_in = False
                                else:
                                    pass
        plugins_list = list(set(self.plugins_list))
        print(f"已加载列表:{plugins_list}")

def plugin_handle(GOBO):
    with open('json_main/plugins.json','r') as j:#打开配置文件
        plugins_json=json.load(j)#加载
        for keys in plugins_json:#获取单个插件
            if plugins_json[keys]["msg_from"] == 'exact':#精确
                if plugins_json[keys]["get_msg"] == GOBO.message and plugins_json[keys]["from"] == GOBO.message_type:#确认是否启动插件
                    try:
                        return_msg=plugins_json[keys]["return_msg"]#观察是否启动自动回复
                    except:
                        return_msg=False#如果不是则不加载
                    if return_msg:#判断是否自动回复
                        if plugins_json[keys]["from"] == "private":#私聊
                            return_msg=HttpService.send_private_msg(GOBO.user_id,return_msg)#发送消息
                        elif plugins_json[keys]["from"] == "group":#群聊
                            return_msg=HttpService.send_group_msg(GOBO.group_id,return_msg)#发送消息
                    if Automaticreplytosubsequentfunctionexecution is True:#是否继续执行后续函数
                        model=importlib.import_module(f'plugins.{keys}.func')
                        model.function(GOBO)
                        if plugins_json[keys]["wait"] is True:#是否开启等待模式
                            pass
                        else:
                            pass
                    else:
                        pass
                elif plugins_json[keys]["get_msg"] == 'include':#包含
                    if plugins_json[keys]["get_msg"] in GOBO.message and plugins_json[keys]["from"] == GOBO.message_type:  # 确认是否启动插件
                        try:
                            return_msg = plugins_json[keys]["return_msg"]  # 观察是否启动自动回复
                        except:
                            return_msg = False  # 如果不是则不加载
                        if return_msg:  # 判断是否自动回复
                            if plugins_json[keys]["from"] == "private":  # 私聊
                                return_msg = HttpService.send_private_msg(GOBO.user_id, return_msg)  # 发送消息
                            elif plugins_json[keys]["from"] == "group":  # 群聊
                                return_msg = HttpService.send_group_msg(GOBO.group_id, return_msg)  # 发送消息
                        if Automaticreplytosubsequentfunctionexecution is True:  # 是否继续执行后续函数
                            model = importlib.import_module(f'plugins.{keys}.func')
                            model.function(GOBO)
                            if plugins_json[keys]["wait"] is True:  # 是否开启等待模式
                                #TODO 等待模式
                                pass
                            else:
                                pass
                        else:
                            pass
                elif plugins_json[keys]["get_msg"] == 'mohu':
                    pass
                    #TODO 模糊化搜索
