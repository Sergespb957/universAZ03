# Шаг 3: Парсинг цен на диваны с сайта divan.ru, сохранение в CSV и анализ данных

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# URL сайта для парсинга
url = 'https://www.divan.ru/sankt-peterburg/category/divany-i-kresla'

# Отправка запроса на сайт
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

prices = []  # Список для хранения цен

for price in soup.find_all('span', class_='ui-LD-ZU KIkOH'):
    prices.append(float(price.text.replace('руб', '').replace(' ', '').strip()))

# Создание DataFrame и сохранение в CSV файл
df = pd.DataFrame(prices, columns=['Цена'])
df.to_csv('prices_divans.csv', index=False)

# Анализ данных: вычисление средней цены
average_price = df['Цена'].mean()
print(f'Средняя цена на диваны: {average_price:.2f} ₽')

# Гистограмма цен на диваны
plt.figure(figsize=(10, 6))
plt.hist(df['Цена'], bins=30, alpha=0.7, color='green', edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (₽)')
plt.ylabel('Частота')
plt.grid()
plt.show()
