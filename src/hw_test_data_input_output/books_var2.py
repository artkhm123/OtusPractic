import json
from csv import DictReader
from test_data import USERS_JSON, BOOKS_CSV

#считываем csv и помещаем только нужные поля по книге в список словарей books_list
def get_book_info(row:dict):
    """функция которая оставляет только нужные поля по книге"""
    title = row['Title']
    author = row["Author"]
    pages = row["Pages"]
    genre = row["Genre"]
    book_dict = {"title": title, "author": author, "pages": pages, "genre": genre}
    return book_dict
file_books = DictReader(open(BOOKS_CSV, "r"))
books_list=[]
for row in file_books:
    books_list.append(get_book_info(row))

#считываем json и помещаем всю информацию по пользователям в список словарей users
with open(USERS_JSON,"r") as file_users:
     users = json.load(file_users)
#создаем список пользователей с нужными нам данными по каждому пользователю
def user_formater(user):
    """
    функция, которая создает словарь нужных параметров по каждому пользователю
    """
    gender = users[user]["gender"]
    name = users[user]["name"]
    address = users[user]["address"]
    age = users[user]["age"]
    books = []
    user_dict={"name":name,"gender":gender,"address":address,"age":age,"books":books}
    return user_dict
user_list=[]
for i in range(len(users)):
    user_list.append(user_formater(i))

#добавим книги из списка books_list пользователям списка user_list
p=0
d=len(user_list)
for i in range(len(books_list)):
    if i<d:
        user_list[p]['books'].append(books_list[i])
        p+=1
    else:
        d=d+len(user_list)
        p=0
        user_list[p]['books'].append(books_list[i])
        p += 1

#выведем получившийся список словарей u в файл result_var2.json
with open ('result_var2.json', 'w') as file:
    s = json.dumps(user_list, indent=4)
    file.write(s)
