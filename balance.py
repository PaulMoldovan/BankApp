import json

def client_balance():
    option = input('\nEnter client ID or Exit to return to main menu:\n> ')
    print('*' * 50)

    json_client_file = open('bank.json', 'r')
    client_dict = json.load(json_client_file)
    json_client_file.close()
    do_edit = True
    while do_edit:
        if option.lower() == 'exit':
            break
        elif option not in client_dict:
            print('Invalid ID.')
            break
        else:
            print(f'Current balance for "{client_dict[option]["name"]}":\n-- {client_dict[option]["balance"]}')
            while do_edit:
                try:
                    edit_balance = int(input('Enter new balance:\n'))
                except:
                    print('Please input a valid number')
                    continue

                client_dict[option]["balance"] = edit_balance
                update_client_json = open('bank.json', 'w')
                update_client_json.write(json.dumps(client_dict, indent=4))
                update_client_json.close()
                print('Balance updated')
                do_edit = False