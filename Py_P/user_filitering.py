import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def make_topics(list):
    for i in range(len(list)):
        temp = list[i].split(" ")
        for j in range(len(temp)):
            if temp[j] not in topics:
                topics.append(temp[j])

data = [
    '물리 양자역학 역학적에너지 퍼텐션에너지',
    '물리 수학 인공지능 python',
    '물리 양자역학 상대성이론 아인슈타인',
    '물리 양자역학 상대성이론 뉴턴',
    '물리 수학 삼각함수 뉴턴'
]
topics = []

make_topics(data)

df = pd.DataFrame(data, columns=['문서'])

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['문서'])

cosine_sim = cosine_similarity(X, X)

topic_indices = {topic: index for index, topic in enumerate(topics)}