# 프로젝트형 클라우드(MSA) 서비스 과정
# 2022-01-19 과제

# 1. 딕셔너리를 이용해서 평균 점수 구하기
dictData1 = { '국어': 95, '영어': 90, '수학': 80, '과학': 50 }
sum = 0
for key in dictData1:
    sum += dictData1[key]
average = sum / len(dictData1)

# 2. 셋을 이용해서 1~100까지 숫자중에 3과 5의 공배수를 구하고, 합집합을 구하기
setData1 = set([i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0])

# 3. 리스트 데이터 : [7, 5, 3, 1, -1, -3, -5, -7] 출력
# range 함수를 활용해서
listData1 = list(range(7, -8, -2))
print(listData1)

# 4. 3의 결과를 튜플로 변경(형변환)
tupleData1 = tuple(listData1)

# 디버깅을 위한 변수
temp = 0