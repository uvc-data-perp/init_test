import wandb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# WandB 초기화
wandb.init(project="data-eda-preprocessing", name="iris-dataset-analysis")

# 데이터 로드 (예: Iris 데이터셋)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
data = pd.read_csv(url, names=columns)

# 수치형 데이터만 선택
numeric_data = data.select_dtypes(include=[np.number])

# 기본 통계 로깅 (수치형 데이터만)
wandb.log({"data_shape": data.shape})
wandb.log({"numeric_data_description": wandb.Table(dataframe=numeric_data.describe())})

# 결측치 확인 및 로깅
missing_values = data.isnull().sum()
wandb.log({"missing_values": wandb.Table(dataframe=missing_values.to_frame())})

# 상관관계 분석 (수치형 데이터만)
corr = numeric_data.corr()

# 각 특성의 분포 시각화
for column in data.columns[:-1]:  # 마지막 'class' 열 제외
    plt.figure(figsize=(10,6))
    sns.histplot(data=data, x=column, hue='class', kde=True)
    plt.title(f"Distribution of {column}")
    wandb.log({f"{column}_distribution": wandb.Image(plt)})

# 간단한 전처리: 표준화 (수치형 데이터만)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_data)
scaled_df = pd.DataFrame(scaled_data, columns=numeric_data.columns)
scaled_df['class'] = data['class']

wandb.log({"scaled_data_sample": wandb.Table(dataframe=scaled_df.head())})



# 각 특성의 분포 시각화
for column in numeric_data.columns:
    plt.figure(figsize=(10,6))
    sns.histplot(data=data, x=column, hue='class', kde=True)
    plt.title(f"Distribution of {column}")
    wandb.log({f"{column}_distribution": wandb.Image(plt)})
wandb.finish()

####
# 상관관계 분석 및 시각화
corr = numeric_data.corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
wandb.log({"correlation_heatmap": wandb.Image(plt)})

# 공분산 행렬 계산 및 로깅
cov = numeric_data.cov()
wandb.log({"covariance_matrix": wandb.Table(dataframe=cov)})

# 산점도 행렬
plt.figure(figsize=(12,10))
sns.pairplot(data, hue='class')
wandb.log({"pairplot": wandb.Image(plt)})