# # axis별로 apply를 적용가능
# import pandas as pd
# import numpy as np

# frame = pd.DataFrame(np.arange(12).reshape(3,4),
#                      columns = list('abcd'))
# print(frame)

# print(frame.apply(lambda x : x.max()-x.min())) #axis=0 : default
# #default : 별도 설정 하지 않은 '초기값' 즉,'기본 설정값'을 의미.
# print(frame.apply(lambda x : x.max()-x.min(),axis=1))

# # - applymap
#     # - 모든 우너소에 원소별로 함수에 적용.
# print(frame.applymap(lambda x: x**2))

# - drop
#  - row나 column에서 특정한 label을 삭제하는 함수.
# import pandas as pd
# import numpy as np

# frame = pd.DataFrame(np.arange(16).reshape(4,4),
#                      index = ['r1','r2','r3','r4'],
#                      columns = ['c1','c2','c3','c4'])
# print(frame)
# # print(frame.drop('r1'))
# # print(frame.drop('c1',axis=1)) #KeyError: "['c1'] not found in axis")
# # print(frame.drop('r1'.inplace=True))
# # print(frame.drop(columns=['c3','c4']))
# print(frame.drop('r2',inplace=True)) # r2 행 삭제
# print(frame)


# import pandas as pd
# import numpy as np
# s1 = pd.Series([100,200],index=['c','d'])
# s2 = pd.Series([300,300,300],index=['c','d','e'])
# s3 = pd.Series([500,600], index=['f','g'])

# print(s1,s2,s3, sep='\n\n')

# print(pd.concat([s1,s2,s3]))

# print(pd.concat([s1,s2],axis=1)) #SQL의 outer join(합집합)으로 돌아감.)


# import pandas as pd
# import numpy as np
# data1 = pd.DataFrame({'id':['01','02','03','04','05','06'],
#                       'col1':np.random.randint(0,50,6),
#                       'col2':np.random.randint(1000,2000,6)
#                       })
# print(data1)

# data2 = pd.DataFrame({'id':['04','05','06','07'],
                    #   'col1':np.random.randint(1000,5000,4)})
# print(data2)

#inner join(교집합)
# print(pd.merge(data1,data2,on='id')) #on은 기준

#how : 어떤 방식으로 병합할 것 인가?{inner,outer,left,right}
# print(pd.merge(data1,data2,on='id',how='left')) #on은 기준

#outuer join(합집합)
# print(pd.merge(data1,data2,on='id',how='outer')) #on은 기준



# - missing data
    # - dropna : 결측치가 있는 것을 삭제.

# import pandas as pd
# import numpy as np
# obj = pd.Series(['apple','mango',np.nan,None,'peach',1])
# print(obj)

# print(obj.dropna())

# import pandas as pd
# import numpy as np

# frame = pd.DataFrame([[np.nan,np.nan,np.nan,np.nan],[10,5,40,6],[5,2,30,8],[15,3,10,np.nan]],
#                      columns=['x1','x2','x3','x4'])
# print(frame)
# print(frame.dropna())
# print(frame.dropna(how = 'all'))
# print(frame.fillna(0)) #ffill, bill,backfill,'pad',None
# print(frame.fillna({'x1':10,'x3':3,'x4':8}))
# print(frame.isna().sum()) # NoN의 갯수 


# - 중복제거
#     - 1. duplicated() : 각 row가 중복인지(True) 아닌지(False) 알려주는 불리언 Series 변환.
#     - 2. drop_duplicates() : duplicated를 적용한 결과가 False인 것들만 모아서 dataframe 반환.

# import pandas as pd
# import numpy as np
# data = pd.DataFrame({'id':['0001','0002','0003','0001'],
#                      'name':['a','b','c','a']})
# print(data)
# print(data.duplicated()) # 중복 체크(True-> 중복이 되어있다.)
# print(data.drop_duplicates()) # 중복을 삭제. 


# cut

# import pandas as pd
# import numpy as np

# ages = [20,35,67,39,59,44,56,77,28,80,32,46,52,19,33,5,15,50,29,21,33,48,85,80,31,10]
# bins = [0,20,40,60,100]

# cuts = pd.cut(ages,bins)
# print(cuts)

# print(cuts.categories) #cut 메소드의 결과는 Categorical이라는 특수 객체에 존재.
# print(cuts.codes)

# #구간을 균등한 길이로 나눔.
# print(pd.cut(ages,4,precision=3).value_counts())
# #precision : 소수점 자릿수, 3이면 소수점 세번째에서 반올림.

# #구간을 균등한 길이로 나눔.
# print(pd.qcut(ages,4))


# get_dummies
# categorical variable(명목형 변수)를 one - hotencoding 해줌

# import pandas as pd
# import numpy as np

# df = pd.DataFrame({'col1':[10,20,30],
#                    'col2':['a','b','a']}) 
# print(df)
# print(pd.get_dummies(df))



# import pandas as pd


# kbo = pd.read_csv('https://raw.githubusercontent.com/Youngpyoryu/Lecture_Note/main/%ED%8C%8C%EC%9D%B4%EC%8D%AC/kbo.csv')
# print(kbo)
# print(kbo.shape)
# print(kbo.columns)
# print(kbo['팀'].unique())
# print(kbo.info())
# print(kbo.describe())
# print(kbo.isna().sum()) #kbo.isnul().sum()

#groupby를 하며 group으로 묶인 Groupby  객체를 반환.
#이 객체는 그룹 연산을 위해 필요한 모든 정보를 가지고 있음.
# print(kbo.groupby('팀'))

# print(kbo.groupby('팀').count())

# print(kbo.groupby(['연도','팀']).sum())

# print(kbo.groupby('팀')['승률'].max())

# print(kbo.groupby(['연도','팀'])['승률','순위'].max())

# grouped = kbo.groupby('팀')

# for name,group in grouped:
#     print(name)
#     print(group)

#     print('-'*50)



# 판다스 인 액션

# - 셜록 홈즈는 아서 코난 도일의 첫 번째 고전 단편 소설 <보헤미아 왕국의 스캔들>에서 조수인 존 왓슨에게 이렇게 조언합니다. **"데이터를 얻기 전에 이론부터 세우는 것은 중대한 실수입니다. 사실에 맞는 이론을 세우지 않고 이론에 맞게 사실을 왜곡하는 것은 아주 어리석은 일이죠."**

# - 이코노미스트(The Economist)는 2017년 의견서에 '세상에 가장 가치있는 자원은 더 이상 석유가 아니라 데이터'라고 언급하였습니다.

# - 데이터는 근거이며, 근거는 상호 연결된 세계에서 점점 더 복잡해지는 문제를 해결하는 기업, 정부, 기관과 개인에게 매우 중요합니다.

# - 유엔 사무총장 안토니오 구테흐스는 정확한 데이터를 '좋은 정책과 의사 결정의 생명선'이라고 표현
 
# - 데이터 랭글링 : 다양한 데이터 소스의 데이터를 통합하고 쉽게 액세스하고 분석할 수 있도록 정리하는 프로세스.

# - 파이썬의 창시자인 귀도 반 로섬은 "파이썬으로 코딩하는 즐거움은 적은 양의 명확한 코드로 많은 동작을 표현하는 짧고 간결하며 가독성 있는 자료구조 보는 데에 있습니다. 

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/paskhaver/pandas-in-action/master/chapter_01_introducing_pandas/movies.csv', index_col='Title')
# print(df)

# 객체는 데이터를 저장하는 컨테이너라고 생각하면 좋음.
# 서로 다른 객체는 서로 다른 유형의 데이터에 최적화되어 있으며 서로 다른 방식으로 상호작용함.
# 판다스는 한 가지 유형의 객체(DataFrame)를 사용하여 다중 열의 데이터셋을 저장하고 다른 유형의 객체(Series)를 사용하여 단일 열 데이터셋에 저장. DataFrame은 엑셀의 다중 열 테이블과 유사.

# Rank(순위), Title(제목), Stuido(제작사), Gross(총수익), Year(개봉연도)
# 두 번째 행에는 첫 번째 레코드 또는 첫 번째 영화의 데이터가 나열됨.

# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.size)
# print(df.dtypes) # dtypes 보다는 info()함수가 더 좋음.
# print(df.info())

# 500번째 영화 꺼내기
# print(df.iloc[499])

# 모두가 사랑하는 눈물 없이 볼 수 없는 영화 포레스트 검프(Forrest Gump)의 행 값을 추출
# print(df.loc['Forrest Gump'])

# 인덱스 레이블에는 중복 항목이 있을 수 있음.
# print(df.loc['101 Dalmatians'])

# print(df.sort_values(by='Year', ascending=False).head())
# print(df.sort_values(by=['Studio','Year']).head())
# print(df.sort_index().head())

# 하나 이상의 기준으로 열 필터링.
# print(df['Studio'] =='Uninversal')
# print(df[df['Studio']=='Universal'])

# 2015년에 개봉한 영화를 필터링 할 수 있음.(Universal)
# print(df[ (df['Studio'] =='Universal') & (df['Year'] ==2015)])


# 인덱스에서 영화 제목을 소문자로 바꾸고 제목에 'dark'라는 단어가 있는 모든 영화를 찾는 예제.
# has_dark_in_title = df.index.str.lower().str.contains('dark')
# print(df[has_dark_in_title])


# 어떤 제작사가 제작한 영화의 총 수익이 가장 높은지를 알아보자

# df['Gross'].str.replace(
#     "$","", regex = False
# ).str.replace(",","", regex=False)
# print(df['Gross'])

# df['Gross'] = (
#     df['Gross']
#     .str.replace("$","", regex = False)
#     .str.replace(",","", regex=False)
#     .astype(float)
# )
# print(df['Gross'])
# print(df['Gross'].mean())

# 영화 제작사 당 총 흥행 수익을 계산하는 문제
# 먼저 제작사를 식별하고 각 제작사에 속한 영화(또는 행)을 버킷(bucket)으로 지정해야 함. 이 과정을 grouping이라고 함.

# studios = df.groupby('Studio')

# studios['Gross'].count().sort_values(ascending=False).head()
# studios['Gross'].sum().head()
# studios['Gross'].sum().sort_values(ascending=False).head()

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.arange(10)
# y = x+10

# plt.plot(x,y)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(10)
# y = x+10

# plt.xlim([0,10])
# plt.ylim([0,20])

# plt.plot(x,y)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(-np.pi,np.pi,0.02)
# y1 = np.sin(x)
# y2 = np.cos(x)

# plt.plot(x,y1,label='sin', color='b') #RGB
# plt.plot(x,y2,label='cos',color='#FFFF00')
# plt.legend()
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(-np.pi,np.pi,0.02) # pi : 파이(3.141592...)
# y1 = np.sin(x)
# y2 = np.cos(x)

# plt.plot([1,2,3,4],[2,3,5,10],'ro--') ##blue+ o 마크+ --이것으로 이어주세요.
# plt.xlabel('X-Axis') # 축이름
# plt.ylabel('Y-Axis') # 축이름
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(10)
# y1 = x
# y2 = x**2 -x

# fig,axs = plt.subplots(2,1) # 2행 1열로 그리겠습니다.
# fig.set_facecolor('#c79fef') # 뒤의 배경

# axs[0].plot(x,y1) # 첫번째 행
# axs[1].plot(x,y2) # 두번째 행

# axs[0].set_facecolor('pink') # 첫번째 행의 배경
# axs[1].set_facecolor('skyblue') # 두번째 행의 배경

# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(-5,5,0.5)
# y1 = x
# y2 = x**2
# y3 = np.sin(x)
# y4 = np.cos(x)

# plt.plot(x,y1)
# plt.plot(x,y2, marker='D')
# plt.plot(x,y3, color='r')
# plt.plot(x,y4, linestyle = 'dashed')
# plt.show()


# bar plot

# import matplotlib.pyplot as plt
# import numpy as np

# data = {'사과':21, '바나나':15, '배':5,'키위':20}
# names = list(data.keys())
# values = list(data.values())

# fig,ax = plt.subplots()
# ax.bar(names,values)
# plt.show()

# hist

# import matplotlib.pyplot as plt
# import numpy as np

# data = np.random.rand(10000)
# fix,ax = plt.subplots()
# ax.hist(data,bins=100,facecolor='r')
# plt.show()

# 2D Scatter plot
# import matplotlib.pyplot as plt
# import numpy as np

# n=50

# x = np.random.rand(n)
# y = np.random.rand(n)

# plt.scatter(x,y)
# plt.show()


