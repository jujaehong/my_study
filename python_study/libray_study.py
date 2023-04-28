# 표준 라이브러리
# 파이썬에서 지원하는 표준 라이브러리
# 파이썬을 설치할 때 자동으로 함께 설치
# 따로 설치하지 않고 import 명령어로 불러옴

# datetime 라이브러리
# 날짜 관련 라이브러리
# datetime의 date 객체 사용

# import datetime
# day1 = datetime.date(2023,4,17)
# day_end = datetime.date(2023,9,18)
# diff = day_end - day1
# print(diff.days) # 결과 154


# 2018년 8월 6일 무슨 무슨요일일까요?
# weekday() ->> 0:월요일 1:화요일~~ 6:일요일
# import datetime
# day = datetime.date(2018,8,6)
# print(day.weekday()) # 결과 0
# weekdays = ["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]
# print(weekdays[day.weekday()]) # 결과 월요일

# datetime의 포맷팅 코드
# 날짜랑 시간 표시하는 방법
# 년/월/일
# 월/일/년
# 일/월/년
# 2023년 4월 27일
# 2023-04-27
# 23년 4월 27일

# import datetime
# today = datetime.datetime.today()
# print(today)

# strfrime()
# print(today.strftime("%Y년 %m월 %d일"))
# %Y 년도 4자리
# %y 년도 2자리
# %m 월 ( 소문자 m )
# %d 일
# %H 시간 (24시간)
# %I 시간 (12시간)
# %M 분   ( 대문자 M )      
# %S 초
# %A 요일

# print(today.strftime("%A"))

# time 라이브러리
# 시간관련
# import time
# time_now = time.time()
# print(time_now)
# print(time.strftime("%H:%M:%S", time.localtime(time_now)))

# time.sleep() # 지연시간을 주며 출력을 해준다.
# import time
# print("before")
# time.sleep(1)
# print("after")

# for i in range(10):
#     print(i)
#     time.sleep(2)

# math
# 수학관련

# import math
# result = math.ceil(1.1) # 올림
# print(result)

# import math
# result = math.floor(1.9) # 내림
# print(result)

# import math
# print(math.pi)  # 파이

# random
# 난수 관련
# import random
# random_value = random.random()
# 0.0 ~ 1.0 사이의 실수중 난수의 값
# print(random_value)

# random.randint(시작, 끝)
# 시작 ~ 끝 사이의 정수 중 난수 값
# import random
# random_value = random.randint(1, 10)
# print(random_value)

# random.choice(리스트)
# 리스트의 요소 중 무작위로 하나를 리턴
# import random
# foods = ["서브웨이", "맥도널드", "짜장면", "국밥", "김치찌개"]
# food = random.choice(foods)
# print(food)


# random.shuffle(리스트)
# 리스트의 순서가 랜덤하게 바뀐다.
# import random
# li = [1, 2, 3, 4, 5]
# random.shuffle(li)
# print(li)
# random.shuffle(li)
# print(li)
# random.shuffle(li)
# print(li)



# 로또번호 추출 코딩

# import random
# lotto_numbers = list(range(1, 46))
# my_lotto = []
# for i in range(6):
#     random_value = random.choice(lotto_numbers)
#     if random_value not in my_lotto:
#         my_lotto.append(random_value)
# print(my_lotto)        


# in 연산자
# a in b
# a가 b에 포함되어 있으면 Ture
# a가 b에 포함되어 있지 않으면 False

# not in 연산자
# a not in b
# a가 b에 포함되어 있지 않으면 Ture
# a가 b에 포함되어 있으면 False

# random.shuffle 이용한 로또번호 추출
# import random
# lotto_number= list(range(1,46))
# random.shuffle(lotto_number)
# my_lotto = lotto_number[:6]
# print(my_lotto)


# 실습

# 색 이름과 음식 이름을 합치면 멋진
# 밴드 이름이 된다고 합니다.
# 색 이름과 음식 이름을 무작위로 뽑아
# 밴드 이름을 추천하는 프로그램을 만들어보세요

"""
베이비 블랙 블로 회색 청색 파란 핑크 그린
쭈꾸미 요거트 오란다 와플 아이스티 떡볶이 커피

"""

# 방법1

# import random

# li_1 = ["베이비", "블랙", "블루", "회색", "청색", "파란", "핑크", "그린"]
# li_2 = ["쭈꾸미", "요거트", "오란다", "와플", "아이스티", "떡볶이", "커피"]

# band_name = random.choice(li_1) + random.choice(li_2)
# print(band_name)


# 방법2

# import random
# colors = ["베이비", "블랙", "블루", "회색", "청색", "파란", "핑크", "그린"]
# foods = ["쭈꾸미", "요거트", "오란다", "와플", "아이스티", "떡볶이", "커피"]

# color = random.choice(colors)
# food = random.choice(foods)
# print(f"{color}{food}")


# 실습

# 숫자야구게임

# 1. 정답을 정한다. 정답은 4자리 숫자(랜덤)
# 2. 게임유저가 정답을 입력한다.
# 3. 정답과 비교해서 S / B / OUT 개수 알려준다.
# 4. 정답을 맞추거나, 종료를 입력하면 끝낸다.
# 5. 답을 맞췄을 때 -> 한번 더 하시겠습니까?


# 방법1

# import random
# numbers = list(range(10))
# random.shuffle(numbers)
# answer = numbers[1:5] if numbers[0] == 0 else numbers[:4]
# print(answer)
# while True:

#     user_input = input("정답은? ")

    
#     if user_input == "종료":
#         print("종료합니다.")
#         break

#     # 만약 숫자가 아닌 값이 입력되면
#     # 다시입력하게 한다. ----> 처음으로 간다. ---> continue
#     # isdigit() 숫자로만 이루어진 문자열인지 확인한다.
#     # 숫자로만 이루어져있으면 Ture 아니면 False
    
#     elif not user_input.isdigit():
#         print("다시 입력하세요")
#         continue

#     # 만약 4자리 숫자가 아니면 다시 입력하게 한다.
#     # --- > 처음으로 간다. ---> continu
    
#     # elif len(set(user_input)) < len(user_input):
#     #     print("에러: 중복된 숫자가 있습니다.")
#     #     continue
        
#     elif len(user_input) != 4:
#         print("다시 입력하세요")
#         continue
    
#     duplicate = False
#     for i in range(3):
#         if user_input[i] in user_input[i+1:]:
#             duplicate = True
#             break

#     if duplicate:
#         print("중복된 숫자가 없게 입력하세요")
#         continue


#     strike = 0
#     ball = 0
#     out = 0

#     for i in range(4):
#         input_value = int(user_input[i])
#         if input_value not in answer:
#             out += 1
#         elif input_value == answer[i]:
#             strike += 1
#         else:
#             ball += 1

#     print(f"strike: {strike}, ball: {ball}, out: {out}")

#     if strike == 4:
#         print("정답")
#         user_input = input("한번 더 하시겠습니끼?[y/n]")    
        
#         if  user_input == "y":
#             numbers = list(range(10))
#             random.shuffle(numbers)
#             answer = numbers[1:5] if numbers[0] == 0 else numbers[:4]
#             print(answer)
#         else:
#             break    


# 삼항 연산자
# 참일때값 if 조건 else 거짓일때값
# result = "참" if True else "거짓"
# result = "참" if False else "거짓"
# print(result)

# def is_odd_number(n):
#     return "홀수" if n % 2 ==1 else "짝수"
# print(is_odd_number(4))





# os
# os자원을 제어

# import os
# os.environ
# 시스템의 환경 변수 값을 리턴한다.
# print(os.environ)

# import os
# os.getced()
# get current working directory
# print(os.getcwd()) # 현재 작업위치를 절대경로로 알려준다.

# import os
# os.mkdir(디렉터리)
# # 디렉터리(폴더)를 만든다
# os.mkdir("폴더1")

# import os
# os.rename(원래이름,바꿀이름)
# os.rename("파일1","파일2")

# import os
# os.rmdir(디렉터리)
# 디렉터리 (폴더)를 지운다.
# 폴더 안에 아무것도 없어야함(비어있어야 함)
# os.rmdir("폴더1")

# import os
# os.unlink(파일)
# 파일을 지운다.
# os.unlink("파일2")

# import os
# # os.path
# # os.path.exists("경로") 
# if not os.path.exists("없는파일"):
#      f = open("없는파일","w")
#      f.close()
     
# f = open("없는파일","r")
 
# import os
# # os.path.join("경로","경로","경로")
# cwd = os.getcwd()
# my_folder = "python_study"
# file_name = "test_file.txt"
# file_path = os.path.join(cwd, my_folder, file_name)
# with open(file_path, "w", encoding="utf-8") as f:
#     f.write("테스트 파일을 작성합니다.") # 새파일이 생기고 텍스트가 적힘

# 외부 라이브러리
# 파이썬 표준 라이브러리가 아닌 라이브러리
# pip 를 사용해서 설치한다.

# pip
# package installer for python
# 파이썬 모듈, 패키지 설치하는 도구
# numpy, pandas, matplotlib, scikit_learn, keras, Tensorflow, opencv 등등 이아이들은 표준라이브러리가 아니다.
# pyoi(Python Package Index) 파이썬 소프트웨어 저장 공간

# pip install 패키지이름 ( 패키지 최신버전 설치 )
# pip uninstall 패키지이름 ( 패키지 삭제 )

# pip install 패키지이름==1.0.5 (처럼 버전을 명시해서 설치할 수 있다.)

# pip install --upgrade 패키지이름 ( 최신 버전으로 업그레이드 명령 )

# 설치된 패키지 리스트 확인
# pip list

