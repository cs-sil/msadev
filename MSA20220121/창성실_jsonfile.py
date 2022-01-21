# 프로젝트형 클라우드(MSA) 서비스 개발과정
# 2022-01-21 과제

# jsonlab06.py 파일의 with로 코딩한 부분은 try ~ except 식으로 변경하기

import json

# with open("datalab\\mydata.json", "r") as jsonFile:
#     tempData = json.load(jsonFile)
#     #tempData = json.loads(jsonFile)#오류
#     reusltData1 = tempData["name"]
#     reusltData2 = tempData["age"]
#     reusltData3 = tempData["address"]
#     reusltData4 = tempData["email"]
#     reusltData5 = tempData["empcheck"]

try:
    jsonFile = open("datalab\\mydata.json", "r")
    tempData = json.load(jsonFile)
    #tempData = json.loads(jsonFile)#오류
    reusltData1 = tempData["name"]
    reusltData2 = tempData["age"]
    reusltData3 = tempData["address"]
    reusltData4 = tempData["email"]
    reusltData5 = tempData["empcheck"]
except:
    print('Error')
else:
    jsonFile.close()

# --------------------------------------------------

jsonData1 = {
        "empid": 12345678,
        "name" : "홍길동",
        "info" : [
            {"date1": "2022-01-21", "home": "서울시"},
            {"dep": "개발", "email": "aaa@aaa.co.kr"}
        ]
    }

# --------------------------------------------------
# with open("datalab\\mydata2.json", "w") as writeFile:
#     json.dump(jsonData1, writeFile) # 옵션으로 indent=숫자   #한글이 이상함
try:
    writeFile = open("datalab\\mydata2.json", "w")
    json.dump(jsonData1, writeFile)
except:
    print('Error')
else:
    writeFile.close()

# --------------------------------------------------
# with open("datalab\\mydata3.json", "w", encoding="utf-8") as writeFile:
#     json.dump(jsonData1, writeFile, ensure_ascii=False) # 옵션으로 indent=숫자 , 한글을 완벽히 처리  
try:
    writeFile = open("datalab\\mydata3.json", "w", encoding="utf-8")
    json.dump(jsonData1, writeFile, ensure_ascii=False)
except:
    print('Error')
else:
    writeFile.close()

# --------------------------------------------------
# with open("datalab\\mydata4.json", "w") as writeFile:
#     json.dump(jsonData1, writeFile, ensure_ascii=False, indent=4) # 옵션으로 indent=숫자    
#     # 한글이 문제가 있음
try:
    writeFile = open("datalab\\mydata4.json", "w")
    json.dump(jsonData1, writeFile, ensure_ascii=False, indent=4)
except:
    print('Error')
else:
    writeFile.close()

# --------------------------------------------------
# with open("datalab\\mydata5.json", "w", encoding="utf-8") as writeFile:
#     json.dump(jsonData1, writeFile, ensure_ascii=False, indent=4) # 옵션으로 indent=숫자 , 한글을 완벽히 처리  
try:
    writeFile = open("datalab\\mydata5.json", "w", encoding="utf-8")
    json.dump(jsonData1, writeFile, ensure_ascii=False, indent=4)
except:
    print('Error')
else:
    writeFile.close()

#디버깅 변수 선언함(임시)
temp = 0