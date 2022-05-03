import HttpService

def start():
    print("TEST is starting")


def function(GOBO):
    if GOBO.message == "TEST":
        return HttpService.send_private_msg(GOBO.user_id,"hhh")
