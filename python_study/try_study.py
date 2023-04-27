# 예외 처리
# 오류 발생을 잡아내서 처리하는 것

# li = [1, 2, 3, 4, 5]
# li[100] # 인덱스 범위 초과 오류

# 100/0 # 0으로 나눌 수 없는 오류

# f = open("없는파일","r") # 파일이 없는 ㅇㅗ류

# 에러 발생 시 프로그램을 중단하고
# 에러 메세지를 보여준다.

# 예외 처리 구문
# try ~ except
# try 블록에는 오류가 발생할 수 있는 코드
# except 블록에는 오류가 발생했을 때 수행할 코드

# 실습

# try:
#     100 / 0
# except:
#     print("에러발생")

# print("에러 발생 후")

# try:
#     li = [1, 2, 3, 4, 5]
#     li[100]
# except:
#     print("에러가 또 발생")

# try:
#     f = open("없는파일","r")
# except:
#     print("에러가 또또또또 발생")

# try:
#     100 / 0
# except Exception as e:
#     print(e)

# try:
#     100 / 0
# except ZeroDivisionError as e:
#     print(e, "0으로 나눌 수 없습니다.")



# finally
# 예외 발생 여부와 상관 없이 항상 수행되는 코드
# try:
#     f = open("없는 파일", "r")
# except:
#     print("에러 발생")
# finally:
#     f.close()


# else
# 오류가 발생하지 않으면 실행되는 코드

# try:
#     age = int(input("나이"))

# except:
#     print("입력이 잘못 되었습니다.")
#     print("숫자를 입력해주세요.")

# else:
#     if age >= 20:
#         print("성인입니다.")
#     else:
#         print("미성년자입니다.")

# class Bird:
#     def fly(self):
#         raise NotImplementedError

# my_bird = Bird()
# my_bird.fly()



# max_limit_calculator.py 파일에 작성하세요.
# my_calculator 모듈의 MyCalculator 클래스를
# 상속받아서 MaxLimitCalculator 클래스를 정의하세요.
# add, sub, mul, div 메소드를 사용하여
# 더하기, 빼기, 곱하기, 나누기를 할 수 있다.
# 0으로 나눴을 때 엘가 발생하지 않도록 처리한다.
# 입력되는 정수가 1개라도 100보다 크면 계산하지 않고
# 100 이하의 값을 입력하도록 안내 메시지를 출력한다.
# 계산 결과가 100보다 크면 계산하지 않고 100 이하의
# 결과가 나오는 값을 입력하도록 안내 메시지를 출력한다.


# 방법1

# from my_calculator import MyCalculator 

# class MaxLimitCalculator(MyCalculator):

#     def add(self, n1, n2):
#         if n1 > 100:
#             print("100보다 작은수를 입력하세요.")
#         elif n2 > 100:
#             print("100보다 작은수를 입력하세요.")
#         else:
#             result = n1 + n2
#             if result > 100:
#                 print("계산결과가 100보다 작아야합니다.")      
#             else:
#                 print(f"{n1} + {n2} = {n1 + n2}")

#     def sub(self, n1, n2):
#         if n1 > 100:
#             print("100보다 작은수를 입력하세요.")
#         elif n2 > 100:
#             print("100보다 작은수를 입력하세요.")
#         else:
#             result = n1 - n2
#             if result > 100:
#                 print("계산결과가 100보다 작아야합니다.")      
#             else:
#                 print(f"{n1} - {n2} = {n1 - n2}")

#     def mul(self, n1, n2):
#         if n1 > 100:
#             print("100보다 작은수를 입력하세요.")
#         elif n2 > 100:
#             print("100보다 작은수를 입력하세요.")
#         else:
#             result = n1 * n2
#             if result > 100:
#                 print("계산결과가 100보다 작아야합니다.")      
#             else:
#                 print(f"{n1} * {n2} = {n1 * n2}")

#     def div(self, n1, n2):
#         if n1 > 100:
#             print("100보다 작은수를 입력하세요.")
#         elif n2 > 100:
#             print("100보다 작은수를 입력하세요.")
#         elif n2 == 0:
#             print("0으로 나눌 수 없습니다.")    
#         else:
#             result = n1 / n2
#             if result > 100:
#                 print("계산결과가 100보다 작아야합니다.")      
#             else:
#                 print(f"{n1} / {n2} = {n1 / n2}")

# my_max_limt_calculator = MaxLimitCalculator()
# my_max_limt_calculator.add(200,200)



# 방법2 (chat gpt 답)
# from my_calculator import MyCalculator 

# class MaxLimitCalculator(MyCalculator):
    
#     def add(self, num1, num2):
#         if num1 > 100 or num2 > 100:
#             print("100 이하의 값을 입력하세요.")
#             return None
#         result = super().add(num1, num2)
#         if result > 100:
#             print("100 이하의 결과를 얻을 수 있는 값을 입력하세요.")
#             return None
#         return result
    
#     def sub(self, num1, num2):
#         if num1 > 100 or num2 > 100:
#             print("100 이하의 값을 입력하세요.")
#             return None
#         result = super().sub(num1, num2)
#         if result > 100:
#             print("100 이하의 결과를 얻을 수 있는 값을 입력하세요.")
#             return None
#         return result
    
#     def mul(self, num1, num2):
#         if num1 > 100 or num2 > 100:
#             print("100 이하의 값을 입력하세요.")
#             return None
#         result = super().mul(num1, num2)
#         if result > 100:
#             print("100 이하의 결과를 얻을 수 있는 값을 입력하세요.")
#             return None
#         return result
    
#     def div(self, num1, num2):
#         if num1 > 100 or num2 > 100:
#             print("100 이하의 값을 입력하세요.")
#             return None
#         if num2 == 0:
#             print("0으로 나눌 수 없습니다.")
#             return None
#         result = super().div(num1, num2)
#         if result > 100:
#             print("100 이하의 결과를 얻을 수 있는 값을 입력하세요.")
#             return None
#         return result
# max_calc = MaxLimitCalculator()

# print(max_calc.div(100, 0))