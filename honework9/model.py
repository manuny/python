phone_book = []
path = 'honework9\phone.txt'

def open_file():
    with open(path, 'r', encoding ='UTF-8') as file:
        data = file.readlines()
    for fields in data:
        fields = fields.strip().split(';')
        contact = {'name': fields[0],
                	'phone': fields[1],
                    'comment': fields[2]}
        phone_book.append(contact)
        
def get_phone_book():
    return phone_book

def add_contact(contact: dict):
    phone_book.append(contact)

def save_file():
    data = []
    for contact in phone_book:
        data.append(';'.join(contact.values()))
    data = '\n'.join(data)
    with open(path,'w', encoding='UTF-8') as file:
        file.write(data)