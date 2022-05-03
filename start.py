import HttpService
import plugins_in


def open():
    plugin = plugins_in.Plugins_in()


def run(msg_in):
    GOBO = HttpService.HTTP_CONTROL(msg_in)
    plugins_in.plugin_handle(GOBO)
