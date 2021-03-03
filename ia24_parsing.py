# import requests
# from bs4 import BeautifulSoup as BS
# from datetime import datetime
#
# start = datetime.now()
# url = 'https://24.kg/'
# urls = []
#
# for i in range(1, 1614):
#     urls.append(f"{url}page_{i}")
#     print(f"{url}page_{i}")
#
# for link in urls:
#     response = requests.get(link)
#     print(response)
#
#     html = response.text
#     soup = BS(html, "html.parser")
#
#     news = soup.find_all('div', class_='one')
#     print(type(news))
#     for i in news:
#         href = i.find('a').get('href')
#         print(href)
#         with open('links.txt', 'a') as file:
#             file. write(f'{url}{href[1:]}\n')
#     print(f'Все ссылки собраны за {datetime.now() - start}')
#
# # all_links()
#
# links_list = []
#
# with open("links.txt") as file:
#     for link in file:
#         links_list.append(file. readline().replace('\n', ''))
#         # print(file. readline().replace('\n', ''))
#
# i = 1
# print(len(links_list))
# for link in links_list:
#     response = requests.get(link)
#     # print(response)
#     soup = BS(response.text, "html.parser")
#     data = soup.find('div', itemid=link)
#     # print(data.text)
#     i += 1
#     with oen(f"{link}.txt", 'w') as file:
#         file.write(data)
#
