import datetime

from people.bloggers import Blogger

now = datetime.datetime.now()

print(now)

def return_blogger():
    return Blogger()