from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

docs = [
    '호날두는 가장 위대한 축구 선수',
    '오타니는 가장 위대한 야구 선수',
    '메시는 축구를 잘한다',
    '마이클 조던은 농구를 잘한다'
]

user_search = '물리'

# CountVectorizer로 문서를 벡터화
vect = CountVectorizer()
countvect = vect.fit_transform(docs)

# 단어 사전 출력
print("단어 사전:")
print(sorted(vect.vocabulary_.items()))

# CountVectorizer로 변환한 데이터를 DataFrame으로 변환
countvect_df = pd.DataFrame(countvect.toarray(), columns=sorted(vect.vocabulary_))
countvect_df.index = ['문서1', '문서2', '문서3', '문서4']
print("\nCountVectorizer로 변환한 데이터프레임:")
print(countvect_df)

# 문서 간 코사인 유사도 계산
cos_similarity = cosine_similarity(countvect_df, countvect_df)

# 데이터프레임 형태로 유사도 행렬 출력
df_similarity = pd.DataFrame(cos_similarity, index=countvect_df.index, columns=countvect_df.index)

# 대각선 원소(같은 문서의 유사도)를 0으로 설정
np.fill_diagonal(df_similarity.values, 0)

print("\n문서 간 코사인 유사도:")
print(df_similarity)

# 시각화
plt.figure(figsize=(8, 6))
ax = sns.heatmap(df_similarity, annot=True, annot_kws=dict(color='w'), cmap='Greens')
plt.title('문서 간 코사인 유사도')
plt.show()
