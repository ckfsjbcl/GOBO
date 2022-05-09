# GOBO

## 入门配置

### 第一步：配置go-cqhttp

  ####1.打开go-cqhttp文件夹，找到config.yml配置文件
  ####2.修改account中的uin及password，具体参照注释

### 第二步：开始编写插件之路

  ####1.创建插件文件：在plugins文件夹中创建一个新的文件夹，名字为插件名
  ####2.创建目录如下
      |-插件名(文件夹)(以下名字皆固定)
          |-__init__.py(内容固定为:from . import *)
          |-func.py(函数主程序)
          |-README.md(插件介绍,不会写可以不写)
  ####3.func.pu内容:

```python
import HttpService
#以上为前置函数,接口皆封装于其中(未完全封装完成,基础功能以实现)
def start():
    #该函数用于测试函数是否合法并完成加载
    print("这里写插件名 is starting")
  
def function(GOBO):
    pass#写代码时记得把这个pass删了
    #该函数为主函数
    #这里添加函数主体
    """
    食用方法:
    GOBO为实例来调用各个属性
    属性调用方法:
        属性表:
        [私聊](https://docs.go-cqhttp.org/event/#%E7%A7%81%E8%81%8A%E6%B6%88%E6%81%AF)
        [群聊](https://docs.go-cqhttp.org/event/#%E7%BE%A4%E6%B6%88%E6%81%AF)
        访问以上网址以获得列表
        调用方法:
        用收到的信息举例
        字段名为’message‘
        调用方法GOBO.message
        示例:
            if GOBO.message == “balabala”:
                ...
    消息回送及其他api接口调用方法:
        调用:
            HttpService.这里填函数名
            示例:
                HttpService.send_private_msg(user_id=GOBO.user_id,message="abab")
                看不懂没关系,照着写就完事了:
                具体每个函数的名称与作业请参照(Function_others.py)
    最后一个简单的自动回复示例:
  
    import HttpService

    def start():
        print("TEST is starting")


    def function(GOBO):
        HttpService.send_private_msg(user_id=GOBO.user_id,message="早上好！")
    """
```

  ####4.配置plugins.json文件
  暂时不能自动化,抱歉
  请将倒数第二个大括号后添加一个逗号,然后换行(回车)
  然后再填充(中文部分)完下面一段话后复制上去:

```json
    "插件名":{
    "get_msg": "收到的消息",
    "msg_from": "消息接受情况:一模一样:exact,包含:include,模糊:mohu",
    "from": "消息来源:私聊:private,群聊:group,都可以:all(暂不支持)",
    "return_msg": "直接回复,若设置,在执行主函数前将先发送此处内容,可以在配置文件中禁用,若不执行则删去两边的双引号改为false:示例:  'return_msg':false  ",
    "open": true,
    "wait": false,
    "wait_config": {
      "waitformsg": false,
      "return_msg": false,
      "return_func": false
    }
  }
```

TO BE CONTINUE...
