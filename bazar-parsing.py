# # pip install requests
# # pip install bs4
#
#
# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://www.bazar.kg/kyrgyzstan/elektronika/telefony-gadzhety'  # какую страницу спарсить
# page = '?page='
# i = 0
# while i <= 70:
#     i += 1
#     response = requests.get(f"{url}{page}{i}").text
#     # print(response)
#
#     soup = BeautifulSoup(response, "html.parser")
#     data = soup.find_all('div', class_="listing")
#     print(f"{url}{page}{i} Спарсил удачно")
#     for block in data:
#
#         title = block.find('div', class_="left-side").text.strip()
#         price = block.find('p', class_="price").text
#         # print(title)
#         # print(price)
#
#         with open("bazar.txt", 'a') as file:
#             file.write(title + price + "\n")