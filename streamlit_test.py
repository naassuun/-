import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pylab

#читаем файл с данными
db = pd.read_excel('books_data.xlsx')
#создаем виджет с таблицей
st.write(db)

plt.figure(figuresize=(12, 7))
#создаем и выводим виджет с графиком
plt.subplot(1, 3, 1)
x = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
y = [9700, 19100, 13500, 19500, 9700, 13700, 19725, 148400, 134716, 273017, 111000]
plt.bar(x, y, label='Кол-во книг')
plt.xlabel('Год')
plt.ylabel('Кол-во книг')
plt.title('Публикации художественной китайской литературы в России 2015-2025 гг.')
plt.legend()
st.pyplot(plt.gcf())
#создаем и выводим график с информацией по АСТ
plt.subplot(1, 3, 2)
x1 = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
y1 = [0, 0, 0, 0, 0, 0, 0, 18000, 58500, 71500, 33000]
plt.bar(x1, y1, label='Кол-во книг')
plt.xlabel('Год')
plt.ylabel('Кол-во книг')
plt.title('Публикации художественной китайской литературы издательством АСТ 2015-2025 гг.')
plt.legend()
st.pyplot(plt.gcf())

#создаем виджет с выпадающим списком
options = st.multiselect('Книги какого года вас интересуют?', db['Год издания'].unique())
st.write('Вы выбрали: ', options)
#создаем и выводим новую таблицу, сформированную по выбранным данным
new_db = db[(db['Год издания'].isin(options))]
st.write(new_db)

