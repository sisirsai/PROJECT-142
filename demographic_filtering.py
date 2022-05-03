import numpy as np
import pandas as pd

df = pd.read_csv('articles.csv')
df = df.sort_values('total events',ascending = False)

output = df[['title','text','url','lang','contentType','total events']].head(20).values.tolist()