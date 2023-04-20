# age = 19
# money = 50000
# chicken = 20000
# beer = 10000
# drink = 5000
# if money >= chicken:
#     print("치킨을 먹는다.")
# if money >= beer and age >= 20: 
#     print("맥주를 먹는다.")    
# if money >= drink:
#     print("음료수를 먹는다.")

# age = 19
# money = 20000
# chicken = 20000
# beer = 10000
# drink = 5000
# if money >= chicken:
#     print("치킨을 먹는다.")
# if money >= beer and age >= 20: 
#     print("맥주를 먹는다.")    
# if money >= drink:
#     print("음료수를 먹는다.")

# age = 19
# money = 25000
# chicken = 20000
# beer = 10000
# drink = 5000
# if money >= (chicken + drink):
#     print("치킨과 음료수 함께 먹는다")  
# elif money <= (chicken + drink) and money >= 20000:
#     print("치킨만 먹는다.")
# elif money <= (chicken + drink) and money < 20000 and money >=5000 :
#     print("음료수만 먹는다")
# elif money < 5000:
#     print("그냥 집에가자")

# age = 19
# money = 20000
# chicken = 20000
# beer = 10000
# drink = 5000
# if money >= chicken:
#     money = money - chicken
#     print("치킨을 먹는다.")
# if money >= beer and age >= 20: 
#     print("맥주를 먹는다.")
#     money = money - beer    
# if money >= drink:
#     print("음료수를 먹는다.")
#     money = money - chicken


#좋은예........................................................................
# age = 20
# money = 30000
# chicken = 20000
# beer = 10000
# drink = 5000
# if money >= chicken + beer + drink and age >= 20:
#     print("치킨, 맥주, 음료수 먹는다.")
# elif money >= chicken + beer and age >= 20:
#     print("치킨, 맥주 먹는다.")
# elif money >= chicken + drink:
#     print("치킨, 음료수 먹는다.")
# elif money >= chicken:
#     print("치킨 먹는다.")
# elif money >= beer + drink and age >= 20:
#     print("맥주, 음료수 먹는다.")
# elif money >= beer and age >= 20:
#     print("맥주 먹는다.")    
# elif money >= drink:
#     print("음료수 먹는다.")        

# #다른예............................................................................
# age = 20
# money = 10000
# chicken = 20000
# beer = 10000
# drink = 5000
# if money >= chicken:
#     print("치킨을 먹는다")
#     if money - chicken >= beer and age >= 20:
#         print("맥주를 먹는다.")
#         if money - chicken - beer >= drink:
#             print("음료수를 먹는다")
#     if money - chicken >= drink:
#         print("음료수를 먹는다")
# elif money >= beer and age >= 20:
#     print("맥주를 먹는다.")
#     if money - beer >= drink:
#         print("음료수를 먹는다")
# elif money >= drink:
#     print("음료수를 먹는다.")       


# input, int함수 응용
age = int(input("당신의 나이는?"))
money = int(input("얼마있어?"))
chicken = 20000
beer = 10000
drink = 5000
if money >= chicken + beer + drink and age >= 20:
    print("치킨, 맥주, 음료수 먹는다.")
elif money >= chicken + beer and age >= 20:
    print("치킨, 맥주 먹는다.")
elif money >= chicken + drink:
    print("치킨, 음료수 먹는다.")
elif money >= chicken:
    print("치킨 먹는다.")
elif money >= beer + drink and age >= 20:
    print("맥주, 음료수 먹는다.")
elif money >= beer and age >= 20:
    print("맥주 먹는다.")    
elif money >= drink:
    print("음료수 먹는다.")   