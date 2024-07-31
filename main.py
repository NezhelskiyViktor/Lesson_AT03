import requests


#  Решение поставленной задачи.
#  Функция, которая делает запрос к TheCatAPI
#  для получения случайного изображения кошки
def get_the_cat_picture():
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]['url']
    else:
        return None


'''
Пример кода, который был создан во время обучения

def get_weather(api_key, city):
   url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
   response = requests.get(url)
   if response.status_code == 200:
       return response.json()
   else:
       return None


def get_github_user(username):
   url = f'https://api.github.com/users/{username}'
   response = requests.get(url)
   if response.status_code == 200:
       return response.json()
   else:
       return None
'''
