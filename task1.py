import re

password = input('Input password: ')


def password_check(p):
    if re.search(r'((?=^[a-zA-Z])(?=\S*[!@#$%^&*-+=|:.?~])(?=\S+\d$)\S{6,20})', p):
        print('Your password is valid')
    else:
        print('Your password is not valid')


password_check(password)
