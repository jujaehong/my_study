import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# s = pd.Series([1,3,5,np.nan,6,8])
# print(s)

# 2020512부터 8개의 날짜를 생성
# dates = pd.date_range('20230512',periods = 6)
# print(dates)

# columns_df = list('abcdef')
# columns_dd = [col.center(6,' ') for col in columns_df] # 칼럼 가운데 정렬

# np.random.randn(8,6) 8은 dates의 수 , 10은 한행에 6개의 난수 , 'abcdefghij'는 각열이름
# df = pd.DataFrame(np.random.randn(6,6),index=dates,columns=columns_dd)

# print(df)

# df2 = pd.DataFrame({'a' :1.,
#                     'b' : pd.Timestamp('20230512'),
#                     'c' : pd.Series(1,index=list(range(4)),dtype='float32'),
#                     'd' : np.array([3] * 4,dtype='int32'),
#                     'e' : pd.Categorical(["test","train","test","train"]),
#                     'f' : 'foo'})
# print(df2)



# df3 = pd.DataFrame({'id' :[1001,1002,1003],
#                     '입사일' :[20230501,20230506,20230508],
#                     '퇴사일' :[20240501,2024506,2024508]})

# print(df3)       

# df4 = pd.DataFrame([[1001,20230501,20240501],
#                    [1002,20230506,20240506],
#                    [1003,20230508,20240508]],
#                     columns=["id","입사일","퇴사일"])    
# print(df4)  

column_df = ["id","입사일","퇴사일"]
df4 = pd.DataFrame([[1001,20230501,20240501],
                   [1002,20230506,20240506],
                   [1003,20230508,20240508],
                   [1004,20230512,20250601],
                   [1005,20230515,20260101],
                   [1006,20230612,20240306],
                   [1007,20230830,20240503],
                   [1008,20231130,20240503],
                   [1009,20231230,20240503]],
                    columns=column_df,
                    index = range(1,10),
                    dtype = int)    
print(df4)    

# print(df4.head())
# print(df4.tail())
# print(df4.info())
# print(df4.shape)
# print(df4.columns)
# print(df4.sample())
# print(df4.dtypes)
# print(df4.ndim)
# print(df4.shape)

# print(df4.isna())
# print(df4.isnull())
# print(df4.loc[1,3])

# print(df4.loc[2:4, ['입사일']])
# print(result)
print(df4.loc[2:5,['id','퇴사일']])