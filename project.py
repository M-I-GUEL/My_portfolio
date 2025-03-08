import streamlit as sl
import pandas
sl.set_page_config(layout='wide')
col1,col2= sl.columns(2)
with col1:
    sl.image('images/photo.png')
contents = '''
             Hi, i'm Joseph Anazodo. I am a dedicated Python developer specializing in automation and data science. 
             My passion lies in streamlining processes and extracting meaningful insights from complex datasets.
             My mission is to leverage Python's versatility to automate mundane tasks and harness data-driven decision-making, 
             thereby enhancing operational efficiency and strategic planning.
             Apart from coding, I enjoy mentoring aspiring developers and contributing to open-source projects, 
             believing in the power of community-driven growth.
           '''
with col2:
    sl.title('Anazodo Joseph')
    sl.info(contents)
sl.write("Below are some of the projecyts i've built. Feel free to contact me! https://www.udemy.com/course/the-python-mega-course/learn/lecture/34604130#overview")
col3,empty_col,col4 = sl.columns([1.5,0.5,1.5])

df =pandas.read_csv('data.csv',sep=';')
with col3:
    for index,row in df[:10].iterrows():
       sl.header(row['title'])
       sl.write(row['description'])
       sl.image(f'images/{row['image']}')
       sl.write(f'[Source Code]({row['url']})')

with col4:
    for index, rows in df[10:].iterrows():
        sl.header(rows['title'])
        sl.write(rows['description'])
        sl.image(f'images/{row['image']}')
        sl.write(f'[Source Code]({row['url']})')