import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pylab

#читаем файл с данными
db = pd.read_excel('books_data.xlsx')
#создаем виджет с таблицей
st.write(db)

#создаем и выводим виджет с графиком
x = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
y = [9700, 19100, 13500, 19500, 9700, 13700, 19725, 148400, 134716, 273017, 111000]
plt.bar(x, y, label='Кол-во книг')
y = [0, 0, 0, 0, 3000, 3000, 0, 3000, 41000, 158000, 73000]
plt.bar(x, y, label='Кол-во книг, Эксмо')
y = [0, 0, 0, 0, 0, 0, 0, 18000, 58500, 71500, 33000]
plt.bar(x, y, label='Кол-во книг, АСТ')
plt.xlabel('Год')
plt.ylabel('Кол-во книг')
plt.title('Публикации художественной китайской литературы в России 2015-2025 гг.')
plt.legend()
st.pyplot(plt.gcf())

#создаем виджет с выпадающим списком
options1 = st.multiselect('Книги какого года вас интересуют?', db['Год издания'].unique())
st.write('Вы выбрали: ', options1)
#создаем и выводим новую таблицу, сформированную по выбранным данным
new_db1 = db[(db['Год издания'].isin(options1))]
st.write(new_db1)

#создаем виджет с выпадающим списком
options2 = st.multiselect('Книги какого автора вас интересуют?', db['Автор'].unique())
st.write('Вы выбрали: ', options2)
#создаем и выводим новую таблицу, сформированную по выбранным данным
new_db2 = db[(db['Автор'].isin(options2))]
st.write(new_db2)

#создаем виджет с выпадающим списком
options3 = st.multiselect('Книги какого издательства вас интересуют?', db['Издательство'].unique())
st.write('Вы выбрали: ', options3)
#создаем и выводим новую таблицу, сформированную по выбранным данным
new_db3 = db[(db['Издательство'].isin(options3))]
st.write(new_db3)

