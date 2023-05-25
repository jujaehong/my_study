# import matplotlib.pyplot as plt

# fig,axs = plt.subplots(1,3, figsize=(9,3)) #가로 : 9cm / 세로 : 3cm

# axs[1].set_xticks([0,2,4,6])
# axs[1].set_yticks([0,5,10])

# axs[2].set_xticklabels(['A','B','C','D','E'])
# axs[2].set_yticks([0,1,2])
# axs[2].set_yticklabels(['a','b','c'])

# plt.show()

# import matplotlib.pyplot as plt

# fig,axs = plt.subplots(1,3, figsize=(9,3)) #9cm / 3cm

# fig,axs = plt.subplots(1,3, figsize=(9,3)) #9cm / 3cm


# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# np.random.seed(0)
# # y=4X+6식을 근사(w1=4,w=0.6). random. 값은 noise를 위해 만듦.
# X = 2*np.random.rand(100,1)
# y = 6+4*X+np.random.randn(100,1)

# #X,y 데이터 셋 scatter plot으로 시각화
# plt.scatter(X,y)
# plt.show()

# #w1과 w0를 업데이트 할 w1_update, w0_update를 반환.
# def get_weight_updates(w1, w0, X,y,learning_rate=0.01):
#     N=len(y) #y = w_0+w1*x1
#     #먼저 w1_update,w0_update를 각각 w1, w0의 shape와 동일한 크기를 가진 0값으로 초기화
#     w1_update = np.zeros_like(w1) # 벡터크기에 따라서 0 mapping시켜줘.
#     w0_update = np.zeros_like(w0)
#     #예측 배열 계산하고 예측과 실제 값의 차이 계산.
#     y_pred = np.dot(X,w1.T) +w0 # np.matmul써도 되지만, 어차피 벡터 계산이기 때문에 dot를 씀
#     #y=ax+b -> np.dot(X,w1.T)
#     diff = y-y_pred # error function = (실제값-에측값)

#     #w0_update를 dot 행렬 연산으로 구하기 위해 모두 1값을 가진 행렬 생성.
#     w0_factors = np.ones((N,1)) #초기값 ones로 셋팅 N크기만큼 받아들이고,

#     # w1과 w0을 업데이트할 w1_update와 w0_update 계산
#     w1_update = -(2/N)*learning_rate*(np.dot(X.T, diff)) # error ftn : mse(mean square error)
#     #/summation_i^n (y-y_hat)(-x_i)
#     w0_update = -(2/N)*learning_rate*(np.dot(w0_factors.T, diff)) # summation_i^n (y-y_hat)(-x_1)
    
#     return w1_update, w0_update #W_0,W_1 update

# # 입력 인자 iters로 주어진 횟수만큼 반복적으로 w1과 w0를 업데이트 적용함.
# def gradient_descent_steps(X,y,iters=10000):
#     #w0와 w1을 모두 0으로 초기화.
#     w0 = np.zeros((1,1))
#     w1 = np.zeros((1,1))
#     #인자로 주어진 iters만큼 반복적으로 get_weight_updates() 호출하여 w1,w0 업데이트 수행.
#     for ind in range(iters):
#         w1_update, w0_update = get_weight_updates(w1,w0, X,y, learning_rate=0.01)
#         #learning_rate ->hyperparameter(사람이 정하는 파라미터, 정해져 있지 않음.)
#         # 보통 10^(-2) ~ 10^(-6) 절대적으로 정해져 있진 않음.
#         w1 = w1-w1_update #w1(왼쪽에 있는)->new, w1(오른쪽에 있는) ->old
#         #w1_update = gradient descent 방법
#         #new = old-update(update=0 -> new=old) #최적의 값을 찾음.
#         w0 = w0-w0_update
#     return w1,w0

# def get_cost(y, y_pred):
#     N=len(y)
#     cost = np.sum(np.square(y-y_pred))/N
#     print(cost)
#     return cost

# w1,w0 = gradient_descent_steps(X,y,iters=1000) #1000번을 반복
# #최적의 값을 뽑고 그때의 cost값을 출력
# print('w1:{0:.3f} w0:{1:.3f}'.format(w1[0,0],w0[0,0]))
# y_pred = w1[0,0] * X +w0
# print('Gradient Descent Total cost:{0:.4f}'.format(get_cost(y,y_pred)))

# plt.scatter(X,y)
# plt.plot(X,y_pred)
# plt.show()


# pip uninstall scikit-learn #sklearn 삭제
# pip install scikit-learn==1.0.2 sklearn 1.0.2 재설치 (낮은버전)
# import sklearn
# print(sklearn.__version__) # sklearn 버전확인

# import numpy as np
# import pandas as pd
#Visualization Libraries
# import seaborn as sns
#seaborn : 그래프를 통계적으로 그리는 패키지.
# import matplotlib.pyplot as plt
# imoprt package
#->함수를 몽땅 가지고 오는 것,
#from package imoprt module
# 패키지안에서 특정함수를 딸랑만 가지고 오는것.
# from sklearn import datasets
# from sklearn.linear_model import LinearRegression
#from sklearn.-> .은 속성으로 들어가주세요!~
# from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.metrics import mean_squared_error
#To plot the graph embedded in the note book

#loading the dataset direclty from sklearn
# import sklearn
#boston = sklearn.datasets.load_boston()
# boston = datasets.load_boston()

# print(type(boston))
# print('\n') #엔터쳐주세요.
# print(boston.keys())
# print('\n')
# print(boston.data.shape)
# print('\n') #엔터키를 치시오. print('\t') -> tab으로 띄어주세요.
# print(boston.feature_names)

# bos = pd.DataFrame(boston.data, columns = boston.feature_names) 
# #행과 열을 접근하기 위해서
# bos['PRICE'] = boston.target
# print(bos.head()) #위애서 ()면, 갯수가 보임. default=다섯개
# print(bos.tail()) #밑에서 다섯개.

# print(bos.isnull().sum()) #결측치 확인
#bos.isna().sum()

# print(bos.describe()) #요약통계량
# print(bos.info())

# import seaborn as sns
# sns.set(rc={'figure.figsize' : (15,10)}) #Price에 대해 그림을 그림.
#figure.figsize : 크기를 어떻게 할꺼냐?
# plt.hist(bos['PRICE'],bins=30) # .hist -> 히스토그램을 하겠다. bins->막대가 몇 개냐?
# plt.xlabel('House Prcies in $1000') #x축
# plt.show() #그림을 그리시오.

#Created a dataframe without the price col, since we need to see the correlation between the variables
# bos_1 = pd.DataFrame(boston.data, columns = boston.feature_names)

# correlation_matrix = bos.corr().round(2) #상관계수를 계산해줘.

# sns.heatmap(data=correlation_matrix, annot=True) 
#heatmap 관계가 높다는 검은색, 밝은색 -> 진한 색깔이면 관계가 높다. 
#annot->계산한값을 그림에 그려줘.
#다중공산성 문제를 확인한것(왜냐하면 타겟은 빠져있기 때문에.)
# plt.show()

# print(bos.columns)

# plt.figure(figsize=(20,5))

# features = ['LSTAT','RM','DIS']
# target = bos['PRICE']

# for i,col in enumerate(features):
#     plt.subplot(1,len(features),i+1)
#     x = bos[col]
#     y = target
#     plt.scatter(x,y,marker='o', color='#e35f62')
#     plt.title('Variation in House prices')
#     plt.xlabel(col)
#     plt.ylabel('House prices in $1000')  
# plt.show()

# columns_sels = ['LSTAT','INDUS','NOX','PTRATIO','RM','TAX','DIS','AGE']
# x=bos.loc[:,columns_sels]
# y=bos['PRICE']

# fig,axes = plt.subplots(ncols=4,nrows=2,figsize=(20,10))
# index=0
# axes = axes.flatten()
# for i,k in enumerate(columns_sels):
#     sns.regplot(y=y, x=x[k], ax = axes[i])
# plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)
# plt.show()


# print(bos.RM.shape)
# print(bos.PRICE.shape)

# X_rooms = bos.RM
# y_price = bos.PRICE

# X_rooms = np.array(X_rooms).reshape(-1,1)
# y_price = np.array(y_price).reshape(-1,1)

# print(X_rooms.shape)
# print(y_price.shape)

# from sklearn.model_selection import train_test_split
# X_train,X_test,y_train,y_test = train_test_split(X_rooms,y_price, test_size=0.2, 
#                                                  random_state=5)
# print(X_train.shape)
# print(y_train.shape)
# print(X_test.shape)
# print(y_test.shape)

# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error
# #Train에 대한 평가
# reg_1 = LinearRegression()
# reg_1.fit(X_train,y_train)

# y_train_predict = reg_1.predict(X_train)
# rmse = (np.sqrt(mean_squared_error(y_train,y_train_predict)))
# r2 = round(reg_1.score(X_train,y_train),2)

# print('The model performance for training set')
# print('--------------------------------------')
# print('RMSE is {}'.format(rmse))
# print('R2 score is {}'.format(r2))
# print('\n')

# model evaluation for test set
# y_pred = reg_1.predict(X_test)
# rmse = (np.sqrt(mean_squared_error(y_test,y_pred)))
# r2 = round(reg_1.score(X_test,y_test),2)

# print('The model performance for training set')
# print('--------------------------------------')
# print('RMSE is {}'.format(rmse))
# print('R2 score is {}'.format(r2))
# print('\n')

# prediction_space = np.linspace(min(X_rooms),max(X_rooms)).reshape(-1,1)
# plt.scatter(X_rooms,y_price)
# plt.plot(prediction_space, reg_1.predict(prediction_space),color='black',
#          linewidth=3)
# plt.ylabel('value of house/1000($)')
# plt.xlabel('number of rooms')
# plt.show()






# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns
# from scipy import stats
# from sklearn.datasets import load_boston


# boston 데이타셋 로드
# boston = load_boston()

#boston 데이터셋 DataFrame변환
# bostonDF = pd.DataFrame(boston.data, columns = boston.feature_names)

#boston dataset의 target array는 주택 가격
#이를 컬럼 PRICE 컬럼으로 DataFrame에 추가함.
# bostonDF['PRICE'] = boston.target
# print('Boston 데이터셋 크기:', bostonDF.shape)
# bostonDF

# fig,axs = plt.subplots(figsize=(16,8), ncols=4,nrows=2)
# lm_features = ['RM','ZN','INDUS','NOX','AGE','PTRATIO','LSTAT','RAD']
# for i,feature in enumerate(lm_features):
#     row = int(i/4)
#     col = i%4
    #seaborn의 regplot을 이용해 산점도와 선형 회귀 직성을 함께 표현
    # sns.regplot(x=feature, y='PRICE', data= bostonDF,ax = axs[row][col])
# plt.show()

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score


# y_target = bostonDF['PRICE']
# X_data = bostonDF.drop(['PRICE'],axis=1,inplace=False)

# X_train,X_test,y_train,y_test = train_test_split(X_data,y_target,test_size=0.3,
#                                                  random_state=156)

#linear Regression OLS(ordinary Least Square(OLS) method)
#error function을 gradient method로 학습/예측/평가 수행.
# lr = LinearRegression()
# lr.fit(X_train,y_train)
# y_preds = lr.predict(X_test)
# mse = mean_squared_error(y_test, y_preds)  
# rmse = np.sqrt(mse)

# print('MSE : {0:.3f} , RMSE : {1:.3F}'.format(mse , rmse))
# print('Variance score : {0:.3f}'.format(r2_score(y_test, y_preds)))

# print('절편 값:', lr.intercept_)
# print('회귀 계수 값:',np.round(lr.coef_,1))

# 회귀 계수를 큰 값 순으로 정렬하기 위해 Series로 생성. index가 컬럼명에 유의
# coeff = pd.Series(data=np.round(lr.coef_, 1), index=X_data.columns )
# print(coeff.sort_values(ascending=False))


# import numpy as np
# import pandas as pd
# # import matplotlib.pyplot as plt

# train = pd.read_csv('D:/류영표강사20230501/titanic/train.csv') # 주피터에서는 로컬로 읽어야 함. 경로 붙여넣기 하고, 백스래시를 슬래시로 변경해주어야 함
# test = pd.read_csv('D:/류영표강사20230501/titanic/test.csv') # 주피터에서는 로컬로 읽어야 함. 경로 붙여넣기 하고, 백스래시를 슬래시로 변경해주어야 함
# print(train)
# print(test)

