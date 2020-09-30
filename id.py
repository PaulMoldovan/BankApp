import json

def unique_id():
    check_id_file = open('bank.json', 'r')
    dict_from_json = json.load(check_id_file)
    check_id_file.close()

    calculate_keys = []

    for i in dict_from_json:
        calculate_keys.append(i)

    calculate_keys.sort()
    try:
        id = int(calculate_keys[-1]) + 1
    except:
        id = 1
    return id
