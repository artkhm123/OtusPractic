import os.path

FILE_DIR =os.path.dirname(__file__)

def get_file (filename:str):
    return os.path.join(FILE_DIR,filename)

BOOKS_CSV = get_file("books.csv")
USERS_JSON = get_file("users.json")
