# -- coding: utf-8 --
# A_Jian

from dingtalkchatbot.chatbot import DingtalkChatbot

def send_data(message):
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=d6c6b417940c932c5cc43c7a0f75bb93ad3054ccc795edf6619c25f30ad9b828'

    xiaoding = DingtalkChatbot(webhook)

    xiaoding.send_text(msg=message,is_at_all= False)


def test():
    data = 'hello world' + 'price: "%s"' % '123'
    send_data(data)
    return 'ok'

test()