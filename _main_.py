import pandas as pd
import csv 
import plotly.express as px

df = pd.read_csv('data.csv')

student = df.loc[df['student_id']=='TRL_rst']
print(student.groupby('level')['attempt'].mean())

graph = px.bar(x=student.groupby('level')['attempt'].mean(),y=['Level 1','Level 2','Level 3','Level 4'],orientation='h')
graph.show()