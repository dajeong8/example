import http.client
import json

# 본인의 토큰 값을 입력하시오
MY_TOKEN = '5208134316:AAHOWf-qhewb6yHxrhpA5Edu_-sgxUdfCsE'


# 본인의 채팅 아이디를 입력하시오
myChatId = 5362954869

# 보내고 싶은 메세지를 적어보세요
myText = '컴퓨터야 내 메세지 텔레에 보내봐'

def tele(MY_TOKEN,myChatId,myText):
    TELEGRAM_API_HOST = 'api.telegram.org'
    connection = http.client.HTTPSConnection(TELEGRAM_API_HOST)

    # 토큰과 메서명 지정
    url = f"/bot{MY_TOKEN}/sendMessage"

    # HTTP 헤더
    headers = {'content-type': "application/json"}

    # 파라미터
    param = {
        'chat_id': myChatId,
        'text': myText
    }

    # Http 요청
    connection.request("POST", url, json.dumps(param), headers)

    # 응답
    res = connection.getresponse()

    # Response body 출력
    # print(json.dumps(json.loads(res.read().decode()), indent=4))
    # print('응답코드 : ', res.status)
    # print('메시지 : ', res.msg)

    # 연결 끊기
    connection.close()

if __name__=='__main__':
    tele(MY_TOKEN,myChatId,myText)


