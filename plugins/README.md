插件编写规范 |-插件名（需大写） |-__init__.py(导入包)
|-func.py（插件） |-func内容：

            def start():
                print("名字 is starting")
            def function(GOBO):
                if GOBO.BALABAL == "...":
                    pass
            #只加载function的内容，多余函数不会加载
            #若要加载其他函数请加入到config中
#前一种方法不支持，仅支持下一种（暂时）

也可以直接添加到main_json中的plugins_json中
规范请参考第一个TEST目录