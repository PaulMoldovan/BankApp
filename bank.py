import random
# bank App

# requirements:

# utility files - clients.txt bank.txt - same FOLDER
# add clients in clients.txt
# clients: unique ID generated by cod, name, telephone, city
# manipulate balance from bank.txt (unique id - balance)
# bank report - generate new txt file based on id/name with all the info of one client

# utilily functions

# unique id function - ranfomly generate 6 digits and check if it is already exists
# if it does, regenerate, if it doesn't aply it to the client
import client
import id


import client
import balance
import reports
import menu



while True:
    for i in menu.menu_items:
        print(i)
    menu_option = int(input('Select option:\n> '))
    if menu_option == 1:
        client.add_client()
    elif menu_option == 2:
        client.check_client()
    elif menu_option == 3:
        balance.client_balance()
    elif menu_option == 4:
        reports.report()
    elif menu_option == 5:
        print('Program ended.')
        break
    else:
        print('Select valid option.')
        continue





