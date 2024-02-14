file = open('user_info.txt', 'w')

name = input("Please, enter your name: ")

file.write(name)

file.close()