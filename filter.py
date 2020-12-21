import pandas as pd
import re 

df = pd.read_csv('http://bit.ly/imdbratings')


print(df[df.title.str.contains('Drac|Trai')])