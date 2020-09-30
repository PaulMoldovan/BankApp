import json

from id import unique_id


def add_client():
    new_id = unique_id()
    client = {
        'name': input('Numele clientului:\n> '),
        'telephone': input('Numarul de telefon al clientului:\n> '),
        'city': input('Orasul clientului:\n> '),
        'balance': 0
    }


    read_json_file = open('bank.json','r')
    converted_json_to_dict = json.load(read_json_file)
    read_json_file.close()

    converted_json_to_dict[new_id] = client
    new_client_json = json.dumps(converted_json_to_dict, indent=4)

    write_json_file = open('bank.json', 'w')
    write_json_file.write(new_client_json)
    write_json_file.close()



def check_client():
    print('Clients:')
    print('*' * 50)

    json_client_file = open('bank.json', 'r')
    client_dict = json.load(json_client_file)
    json_client_file.close()

    for i in client_dict:
        print(f'{i}.{client_dict[i]["name"]}')
    print('*' *50)

    while True:
        option = input('Please select a client or type EXIT to return to main menu:\n> ')

        if option.lower() == 'exit':
            break
        elif option not in client_dict:
            print('Please select a valid ID\n')
            continue
        else:
            print('-' * 50)
            print(f'Nume: {client_dict[option]["name"]}')
            print(f'Telefon: {client_dict[option]["telephone"]}')
            print(f'Oras: {client_dict[option]["city"]}')
            print(f'Balanta: {client_dict[option]["balance"]}')
            print('-' * 50)
            break


