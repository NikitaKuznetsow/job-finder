import pandas as pd
from models.Indexer import BaselineIndexer
from models.Embedder import TfidfEmbedder

df = pd.read_csv('ods_jobs.csv')
df_texts = df['text'].fillna('')
df_texts_and_date = pd.concat([df_texts, df['ts']], axis=1)
indexer = BaselineIndexer(TfidfEmbedder())
indexer.build(df_texts_and_date['text'].values.tolist())


def get_answer(text: str, k: int = 3):
    indexes = indexer.get_nearest_k(text, k)
    return df_texts_and_date['text'].loc[indexes].values.tolist(), df_texts_and_date['ts'].values.tolist()
