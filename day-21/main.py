# spliting code into multiple files:

from myinfo import info
from myinfo.info import get_usr_name,get_usr_age,get_usr_contact

try:
    user_name = get_usr_name()
    user_age = get_usr_age()
    user_contact = get_usr_contact()

    print(f" Name: {user_name}, Age: {user_age}, Contact:{user_contact}")
except:
    print("Something wrong! Maybe entered invalid values")
