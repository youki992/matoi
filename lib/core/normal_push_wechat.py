import requests
import json

class WeWork_Send_Msg():

    # 文本类型消息
    def send_txt():
        headers = {"Content-Type": "text/plain"}
        #测试企业微信
        send_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=73e78092-77c3-4d1d-86d0-d057f5bbd14d"
        send_data = {
            "msgtype": "text",  # 消息类型
            "text": {
                "content": "检测到自定义POC - OA产品漏洞，请及时检查",  # 文本内容，最长不超过2048个字节，必须是utf8编码
                "mentioned_list": ["@all"],
                # userid的列表，提醒群中的指定成员(@某个成员)，@all表示提醒所有人，如果开发者获取不到userid，可以使用mentioned_mobile_list
            }
        }

        res = requests.post(url=send_url, headers=headers, json=send_data)
        #print(res.text)

if __name__ == '__main__':
    WeWork_Send_Msg.send_txt()