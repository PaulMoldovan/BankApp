from reportlab.pdfgen.canvas import Canvas
import json
import datetime

def report():
    print('Select client:')
    print('*' * 50)


    # deschidem json file cu clienti
    json_client_file = open('bank.json','r')
    client_dict = json.load(json_client_file)
    json_client_file.close()


    for i in client_dict:
        print(f"{i}.{client_dict[i]['name']}")
    print('*' * 50)

    while True:
        option = input('Please select a client or type Exit to return to main menu:\n> ')

        if option.lower() == 'exit':
            break
        elif option not in client_dict:
            print('Please try again, ID is invalid')
            continue
        else:
            canvas = Canvas(f'./{client_dict[option]["name"]}.pdf')

            canvas.setFont("Times-Roman", 18)
            canvas.drawString(20,700,"Raport bancar")
            canvas.drawString(20, 650, "*" * 50)
            #canvas.drawString(20, 630, f"{datetime.datetime.now()}")
            canvas.drawString(20, 610, f"Nume: {client_dict[option]['name']}")
            canvas.drawString(20, 590, f"Telefon: {client_dict[option]['telephone']}")
            canvas.drawString(20, 570, f"Oras: {client_dict[option]['city']}")
            canvas.drawString(20, 550, f"Balanta: {client_dict[option]['balance']}")
            canvas.drawString(20, 650, "*" * 50)


            canvas.drawString(400,100, 'Python BankApp')


            canvas.save()
            print('File has been generated.')
            break