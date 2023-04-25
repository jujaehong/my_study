# 파일 입출력
# 파이썬에서 파일 생성, 수정

# open()
# 파이썬 내장함수
# 파일을 열고, 파일 객체를 리턴한다.
# open(파일 이름, 파일 열기 모드)

# f = open("D:/405/my_study/python_study/새파일.txt", 'w')
# f.close() # open을 하면 꼭 close를 해야한다.

# 파일의 경로
# 절대 경로 : c:/ d:/ 처럼 최상단 경로부터 나타낸 경로
# 상대 경로 : 현재 작업 위치부터 나타낸 경로

# 파일 열기 모드
# r : 읽기 모드, 파일을 읽기만 할 때 사용
# w : 쓰기 모드, 파일에 내용을 쓸 때 사용 (파일을 새로 만들거나...)
# w : 덮어쓰기 된다. ( 이전내용이 덮어쓰기 되기 때문에 주의해야 한다. )
# a : 추가 모드, 파일의 마지막에 새로운 내용을 추가할 때 사용

# w 모드 예제

# f = open("python_study/새파일.txt" , 'w', encoding="utf-8") 
# for i in range(1, 11):
#     print(i, "번째줄") # 터미널 화면에 출력
#     f.write(str(i)+"번째 줄\n")   # " \n 줄바꿈 " # 파일에 데이터 출력
# f.close()


# a 모드 예제

# f = open("python_study/새파일.txt" , 'a', encoding="utf-8") 
# for i in range(11, 21): # 11 ~ 20 까지
#     print(i, "번째줄") # 터미널 화면에 출력
#     f.write(str(i)+"번째 줄\n")   # " \n 줄바꿈 " # 파일에 데이터 출력
# f.close()

# f = open("python_study/새파일.txt" , 'r', encoding="utf-8")

# readline()함수

# 첫번째 줄부터 1줄 읽어온다. (한줄 수행하면 한줄읽고 또 수행하면 그다음줄 읽어오고 한다.)
# 커서가 이동하는 것처럼 읽어옴.

# 처음부터 끝까지 읽어오는 코딩

# f = open("python_study/새파일.txt" , 'r', encoding="utf-8")
# while True:
#     line = f.readline()
#     if line == "": 
#         break      
#     print(line)
# f.close() 

# readlines() 함수

# 파일의 모든 줄을 읽어서 대괄호로 감싸진 리스트로 반환

# f = open("python_study/새파일.txt" , 'r', encoding="utf-8")
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close() 


# read() 함수
# 파일 내용 전체를 문자열로 리턴한다.

# f = open("python_study/새파일.txt" , 'r', encoding="utf-8")
# data = f.read()
# print(data)
# f.close()

# data = f.read()
# print([data])
# f.close()

# for문으로 읽기

# f = open("python_study/새파일.txt" , 'r', encoding="utf-8")
# for line in f:
#     print(line)
# f.close

# with문
# open - close를 자동으로 해준다
# with open("python_study/새파일.txt" , 'a', encoding="utf-8") as f: # ( with~  as~ )
#     f.write("end of file")
#     f.write("2")
#     f.write("3")
#     f.write("4")

# csv(comma separated values) - 문자로 되어있는 파일이다.
# , 로 구분되는 값을 모아놓은 파일 (용량을 최대한 줄이려고 쉼표(탭)을 써서 표를 만드는것)

# with open("python_study/data.csv" , 'w', encoding="utf-8") as f:
#     f.write("날짜,날씨,기온\n")
#     f.write("20230424,맑음,10\n")
#     f.write("20230425,비,9\n")

# with open("python_study/data.csv" , 'r', encoding="utf-8") as f:
#     data = f.readlines()
#     print(data)


# 계산기 결과 저장 함수
# 정수 2개를 입력받고
# 두 수를 더한 결과를
# add_result.txt 파일에
# 저장하는 함수를 정의하세요.
# 함수 이름 : add_write


# def add_write(a, b):
#     # a + b --> write
#     result = a + b
#     with open("add_result.txt" , 'w', encoding="utf-8") as f:
#         f.write(str(result))
# add_write(1, 2)


# 텍스트 파일에 적힌 정수 2개를 
# 읽어와서 더하는 함수를 정의하세요
# 텍스트 파일 이름 : add_number.txt
# 경로 : python_study/add_number.txt
# 정수 2개를 더한 결과를 print 하세요.
# 함수 이름 : read_add_print

# def read_add_print():
#     with open("python_study/add_number.txt" , 'r', encoding="utf-8") as f:
#         data = f.read()
#         a = int(data[0])
#         b = int(data[2])
#         print(a + b)

# read_add_print()


# 계산기 만들기
# 기능 : 두 정수의 사칙연산(+, - , * , /)
# add(), sum(), mul(), div() 함수 정의
# input() 함수를 활용하여
# 정수 2개, 사칙연산 선택을 입력받은 후
# 계산 결과를 print함다.
# 계산식과 결과를
# calculator_result.txt파일에 기록한다.
# 사용자가 'q'를 입력하면 종료한다.



def add(a, b):
    result = str(a)+" + "+str(b)+" = "+str(a+b)
    print(result)
    with open("python_study/calculator_result.txt" , "a", encoding="utf-8") as f:
        f.write(result)

def sub(a, b):
    result = str(a)+" - "+str(b)+" = "+str(a-b)
    print(result)
    with open("python_study/calculator_result.txt" , "a", encoding="utf-8") as f:
        f.write(result)    

def mul(a, b):
    result = str(a)+" * "+str(b)+" = "+str(a*b)
    print(result)
    with open("python_study/calculator_result.txt" , "a", encoding="utf-8") as f:
        f.write(result)
def dic(a, b):
    result = str(a)+" / "+str(b)+" = "+str(a/b)
    print(result)
    with open("python_study/calculator_result.txt" , "a", encoding="utf-8") as f:
        f.write(result)

while True:
    print("""
    계산기
    1: +
    2: -
    3: *
    4: /
    q:종료
    """)
    operator = input("원하는 계산을 입력하세요")
    if operator == 'q':
        break
    a = int(input("정수 1: "))
    b = int(input("정수 2: "))
    if operator == "1":
        add(a, b)
        
    elif operator == "2":
        sub(a, b)
        
    elif operator == "3":
        mul(a, b)
        
    elif operator == "4":
        dic(a, b)

