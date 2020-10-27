'''
타이타닉 생존자 예측하기
출처 : https://yeoulcoding.tistory.com/103
'''


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style

from sklearn.ensemble import RandomForestClassifier

# 데이터 베이스 얻어오기
train = pd.read_csv('./data/train.csv')
test = pd.read_csv('./data/test.csv')

# 데이터 모양 확인
# print(test.shape)
# print(train.shape)

# 유실데이터 확인
total = train.isnull().sum().sort_values(ascending=False)
ratio = (train.isnull().sum() / train.isnull().count() * 100).sort_values(ascending=False)

missing_data = pd.concat([total, ratio], axis=1, keys=['Total', 'Ratio'])
print(missing_data.head(3))

# 성별 생존율
sex_pivot = train.pivot_table(index="Sex", values="Survived")
# sex_pivot.plot.bar()
# plt.show()

# 나이에 따른 생존율
survived = train[train["Survived"]==1]
# survived["Age"].plot.hist(alpha=0.5, color='blue', bins=50)
# plt.show()


train_temp = train.drop(['PassengerId'], axis=1)

train_temp = train_temp.drop(['Cabin'], axis=1)
mean = train_temp['Age'].mean()
std = train_temp['Age'].std()
is_null_cnt = train_temp['Age'].isnull().sum()
rand_age = np.random.randint(mean-std, mean+std, size=is_null_cnt)

rand_temp = train_temp['Age'].copy()
rand_age = rand_temp[np.isnan(rand_temp)]
rand_temp = train_temp['Age']

common_value = 'S'
train_temp['Embarked'] = train_temp['Embarked'].fillna(common_value)

# train_temp.info()

train_temp['Fare'] = train_temp['Fare'].fillna(0).astype(int)

titles = {"Mr" : 1, "Miss" : 2, "Mrs" : 3, "Master" : 4, "Rare" : 5}
train_temp['Title'] = train_temp.Name.str.extract('([A-za-z]+)\.', expand=False)
train_temp['Title'] = train_temp['Title'].replace(['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir'])
train_temp['Title'] = train_temp['Title'].replace('Mlle', 'Miss')
train_temp['Title'] = train_temp['Title'].replace('Ms', 'Miss')
train_temp['Title'] = train_temp['Title'].replace('Mme', 'Mrs')

train_temp['Title'] = train_temp['Title'].map(titles)

train_temp['Title'] = train_temp['Title'].fillna(0)
train_temp = train_temp.drop(['Name'], axis=1)

genders = {"Male" : 0, "female" : 1}
train_temp["Sex"] = train_temp["Sex"].map(genders)

train_temp = train_temp.drop(['Ticket'], axis=1)

ports = {"S":0, "C":1, "Q":2}
train_temp["Embarked"] = train_temp["Embarked"].map(ports)
print("Done")

train_temp['Age'] = train_temp['Age'].astype(int)
train_temp.loc[train_temp['Age'] <= 11, 'Age'] = 0
train_temp.loc[(train_temp['Age'] > 11) & (train_temp['Age'] <= 18), 'Age' ] = 1
train_temp.loc[(train_temp['Age'] > 18) & (train_temp['Age'] <= 22), 'Age' ] = 2
train_temp.loc[(train_temp['Age'] > 22) & (train_temp['Age'] <= 27), 'Age' ] = 3
train_temp.loc[(train_temp['Age'] > 27) & (train_temp['Age'] <= 33), 'Age' ] = 4
train_temp.loc[(train_temp['Age'] > 33) & (train_temp['Age'] <= 40), 'Age' ] = 5
train_temp.loc[train_temp['Age'] > 40, 'Age'] = 6

train_temp['Age'].value_counts()


