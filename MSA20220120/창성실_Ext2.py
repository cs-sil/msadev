# 프로젝트형 클라우드(MSA) 서비스 개발과정
# 2022-01-20 과제

# 1. 4명, 4개의 과목에 대해 개인 합계, 개인 평균, 전체 합계, 전체 평균 구하기

# while문을 이용
users = [
    {
        '이름': '홍길동1',
        '과목': { '국어': 95, '영어': 90, '수학': 80, '과학': 50 }
    },
    {
        '이름': '홍길동2',
        '과목': { '국어': 100, '영어': 50, '수학': 90, '과학': 90 }
    },
    {
        '이름': '홍길동3',
        '과목': { '국어': 99, '영어': 60, '수학': 100, '과학': 40 }
    },
    {
        '이름': '홍길동4',
        '과목': { '국어': 55, '영어': 80, '수학': 80, '과학': 60 }
    },
]

totalSum = 0
totalAverage = 0

userCount = 0
while userCount < len(users):
    user = users[userCount]

    personalSum = 0
    personalAverage = 0
    subjectCount = 0
    subjectList = list(user['과목'].values())
    while subjectCount < len(subjectList):
        personalSum += subjectList[subjectCount]
        subjectCount += 1

    personalAverage = float(personalSum / len(user['과목']))
    print('{}의 개인 합계: {}, 개인 평균: {}'.format(user['이름'], personalSum, personalAverage))

    totalSum += personalSum
    userCount += 1

totalAverage = totalSum / len(users)

print('전체 {}명의 합계: {}, 평균: {}'.format(len(users), totalSum, totalAverage))

temp = 0