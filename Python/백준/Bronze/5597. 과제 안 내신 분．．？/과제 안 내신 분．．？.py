import sys
input = sys.stdin.readline

attendance_book = set() # 출석부
yes_task = set() # 과제를 낸 학생들


for i in range(1, 31): # 1부터 30명 까지
    attendance_book.add(i) # 출석부 집합에 저장

for j in range(1, 29): # 과제를 낸 학생 28명
    student = int(input().strip()) # 입력 받은 학생을 저장
    yes_task.add(student) # 과제를 낸 학생들 집합에 저장

not_task = list(attendance_book - yes_task) # 과제를 안 낸 학생들을 리스트로 변환해서 저장
not_task.sort() # 오름차순으로 정렬
print(*not_task, sep="\n") # 리스트의 요소를 줄별로 출력