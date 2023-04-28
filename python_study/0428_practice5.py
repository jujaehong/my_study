# 거꾸로 배열해도 같은 단어 또는 문장이 되는
# 회문(palindrome)인지 판별하는 함수를 정의하세요.
# 함수에 문자열을 입력받고 회문이면 True
# 아니면 False를 반환하도록 정의하세요.
# 함수이름 : is_palindrome
# 반환 값 : True 또는 False

# '회문' 예제 ( 기러기, 토마토, 소주 만병만 주소 ... )

# 방법1
# word = input("문자를 입력하세요 ? ")
# def is_palindrome(word):
    
#     # 문자열을 뒤집어서 원래 문자열과 비교하여 같은지 확인
    
#     if word == word[::-1]: #방법2  if word == ''.join(reversed(word))
#        return True
#     else:
#        return False

# print(is_palindrome(word))

# 방법2
# word = input("문자를 입력하세요 ? ")
# def is_palindrome(word):
    
#     # 문자열을 뒤집어서 원래 문자열과 비교하여 같은지 확인
#     if word == ''.join(reversed(word)):
#        return True
#     else:
#        return False

# print(is_palindrome(word))

# 방법3 제일 안정적코드 

# def is_palindrome(input_string):
#     input_string = input_string.replace(" ", "") # 공배제거하는 소스
#     length = len(input_string)
#     for i in range(length//2):
#         if input_string[i] != input_string[length - 1 -i]:
#             return False
#     return True

# result = is_palindrome("다시 합창합시다")
# print(result)

