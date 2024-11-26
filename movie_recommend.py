import pandas as pd
import numpy as np
df=pd.read_csv(r'clean_movie.csv')

from nltk.corpus import stopwords
stop_words=set(stopwords.words('english'))
df['tags']=df['tags'].apply(lambda x:[word for word in ast.literal_eval(x) if word not in stop_words])

from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
df['tags']=df['tags'].apply(lambda x:[stemmer.stem(word) for word in x])
df['tags']=df['tags'].apply(lambda x:' '.join(x))

from sklearn.feature_extraction.text import TfidfVectorizer
vc=TfidfVectorizer(max_features=3000)
vector=vc.fit_transform(df['tags']).toarray()


from sklearn.metrics.pairwise import cosine_similarity
similarity=cosine_similarity(vector)
df[df['title']=='Spectre'].index[0]
list(enumerate(similarity[3]))
similar=sorted(list(enumerate(similarity[1])),reverse=True,key=lambda x:x[1])


def recommend(movie):
    index=df[df['title']==movie].index[0]
    similar=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
    for i in similar[1:6]:
        print(df.iloc[i[0]].title)

recommend('Undiscovered')