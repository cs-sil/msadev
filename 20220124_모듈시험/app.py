# 프로젝트형 클라우드(MSA) 서비스 과정
# 2022-01-24 과제

# 공공데이터포털에 있는 오픈 API 활용하기
# 1. 공공데이터포털 회원가입
# 2. 공공데이터를 가져와서 JSON 형식으로 저장하기
#   - 코로나 관련 데이터 아래 중 하나 선택
#       - 공공데이터활용지원센터_코로나19 예방접종 위탁의료기관 조회서비스
#       - 공공데이터활용지원센터_코로나19 예방접종센터 조회서비스

from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def FlaskLab():
    # 인증키
    keyValue = '인증키'

    # Request URL 만들기
    dataURL = 'https://api.odcloud.kr/api/apnmOrg/v1/list'
    dataURL += '?page=' + str(1)
    dataURL += '&perPage=' + str(10)
    dataURL += '&cond%5BorgZipaddr%3A%3ALIKE%5D=' + '%EB%A7%88%ED%8F%AC%EA%B5%AC'
    dataURL += '&serviceKey=' + keyValue

    # API 데이터 요청하기
    dataResult = requests.get(dataURL)

    # JSON 데이터
    jsonData = json.loads(dataResult.text)

    # JSON 파일로 저장
    with open('data.json', 'w', encoding='utf-8') as writeFile:
        json.dump(jsonData, writeFile, ensure_ascii=False, indent=4)

    return jsonData

    