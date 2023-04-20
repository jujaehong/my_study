# weadther = "비" # weather 변수에 값 할당
# print("비가 오나요?", weadther == "비") # 비가 오나요? True 출력
# if weadther == "비": # weadther의 값이 "비"와 같으면 조건식이 True이므로 안쪽 코드 블록 실행
#     print("우산을 가져간다.")  
# else:
#     print("우산을 가져가지 않는다.")

weadther = "맑음" 
print("비가 오나요?", weadther == "비") 
if weadther == "비":
    print("우산을 가져간다.")
elif weadther == "맑음":
    print("날씨가 좋다.")    
else: #조건식이 False이면 실행
    print("우산을 가져가지 않는다.")