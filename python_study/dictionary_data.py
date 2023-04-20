# dictionary(딕셔너리) 자료형
# key-value 형태
# key: value 
# {"이름": "홍길동", "나이":18, "점수": [80, 90, 100], 1: "ㅎㅎ"}
# {"이름": "홍길동", "나이":18, "점수": 80} # key값으로 찾는다.

# person = {"이름": "홍길동", "나이":18, "점수": {"영어": 80,"국어": 90,"수학": 100},1: "ㅎㅎ"}
# print(person["나이"])
# print(person["점수"]["영어"])

# dict_1 = {1: 'a'}
# dict_1['b'] = 2 # 'b':2 key-value 쌍 추가
# dict_1[1] = 'c'
# del dict_1[1]
# print(dict_1)

# dict_2 = {1:'a', 2:'b', 3:'c'}
# keys()
# 딕셔너리에서 key값만 리스트 형태로 돌려준다.
# dict_keys = dict_2.keys() # key만 가져오기
# print(dict_keys)

# dict_values = dict_2.values() #value만 가져오기
# print(dict_values)

# items()
# 딕셔너리에서 key-value 쌍을 튜플로 묶은 값을 리스트 형태로 돌려준다.
# dict_items = dict_2.items()
# print(dict_items)

# get()
# key값이 존재하지 않으면 None을 돌려준다.
# dict_2["나이"] #KeyError: '나이' 라고 뜸 , 에러
# print(dict_2.get("나이")) # None 라고 뜸. 데이터가 있는데 "나이"라는 데이터는 없다.
# print(dict_2.get("나이", "나이불명")) # 데이터에 "나이"가 없어서 None 인데 쉼표하고 "나이불명"을 입력하면 "나이 불명" 이출력된다.

# clear()
# dict_2.clear()
# print(dict_2)