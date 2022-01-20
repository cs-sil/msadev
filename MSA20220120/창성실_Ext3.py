# 프로젝트형 클라우드(MSA) 서비스 개발과정
# 2022-01-20 과제

# 1. 4명, 4개의 과목에 대해 개인 합계, 개인 평균, 전체 합계, 전체 평균 구하기

# 함수 이용
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

def personalSum(user):
    sum = 0
    for subject in user['과목']:
        sum += user['과목'][subject]
    return sum

def totalSum(users):
    totalSum = 0
    for user in users:
        totalSum += personalSum(user)
    return totalSum

tSum = 0
tAverage = 0

for user in users:
    pSum = personalSum(user)
    pAverage = float(pSum / len(user['과목']))
    print('{}의 개인 합계: {}, 개인 평균: {}'.format(user['이름'], pSum, pAverage))

tSum = totalSum(users)
tAverage = tSum / len(users)
print('전체 {}명의 합계: {}, 평균: {}'.format(len(users), tSum, tAverage))

temp = 0