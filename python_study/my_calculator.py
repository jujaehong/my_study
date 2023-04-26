class MyCalculator:

    def __init__(self):
        pass

    def add(self, n1, n2):
        print(f"{n1} + {n2} = {n1 + n2}")

    def sub(self, n1, n2):
        print(f"{n1} - {n2} = {n1 - n2}")

    def mul(self, n1, n2):
        print(f"{n1} * {n2} = {n1 * n2}")

    def div(self, n1, n2):
        print(f"{n1} / {n2} = {n1 / n2}")

  
if __name__ == "__main__":

    my_calculator = MyCalculator()

    while True:
        print("""
        계산기
        1: +
        2: -
        3: *
        4: /
        q: 종료
        """)
        operator = input("원하는 계산을 입력하세요: ")
        if operator == "q":
            break
        n1 = int(input("숫자: "))
        n2 = int(input("숫자: "))
    
        if operator == "1":
           my_calculator.add(n1, n2)
        elif operator == "2":
            my_calculator.sub(n1, n2)
        elif operator == "3":
            my_calculator.mul(n1, n2)
        elif operator == "4":
            my_calculator.div(n1, n2)
        else:
            print("잘못 입력했습니다.")