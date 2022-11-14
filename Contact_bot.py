contacts_dict = {
    'Alex': '380991551515',
    'Ivan': '380630010101',
    'Inna': '380444451405'
}

#----------------------Декоратор з помилками-------------
def input_error(function):

    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except IndexError:
            return 'Print: name as "Oleh" and phonenumber as "1234567890"'
        except KeyError:
            return 'Enter correct name'
        except TypeError:
            return 'Wrong command.'
        except ValueError as exception:
            return exception.args[0]

    return wrapper

#----------------------Функція стартового повідомлення---------
@input_error
def start_app():
    return 'How can I help you?'

#----------------------Функція завершального повідомлення---------
@input_error
def finish_app():
    return 'Good bye!'

#----------------------Функція додавання нового контакту---------
@input_error
def add_contact(contact):
    name, phone = create_contact(contact)

    if name in contacts_dict:
        raise ValueError('This contact already exist.')
    contacts_dict[name] = phone
    return f'You added new contact: {name} - phonenumber: {phone}.'

#----------------------Функція заміни номера існуючого контакту---------
@input_error
def change_phonenumber(contact):
    name, phone = create_contact(contact)
    if name in contacts_dict:
        contacts_dict[name] = phone
        return f"{name}'s phone is changed to {phone}."
    return "Contact isn't detected. Add new contact."

#---------------------Функція виводу книги контактів---------
@input_error
def show_contactbook():
    contacts = ''
    for key, value in contacts_dict.items():
        contacts += f'{key} : {value} \n'
    return contacts

#---------------------Функція пошуку номера існуючого контакту---------
@input_error
def search_phonenumber(name):
    if name.strip() not in contacts_dict:
        raise ValueError('This contact does not exist.')
    return contacts_dict.get(name.strip())


COMMANDS_DICT = {
    'hello': start_app,
    'add': add_contact,
    'change': change_phonenumber,
    'show all': show_contactbook,
    'phone': search_phonenumber,
    'exit': finish_app,
    'close': finish_app,
    'good bye': finish_app
}

#---------------------Функція перетворення і обробки введеної команди-------------
def change_input(user_input):
    new_input = user_input
    contact = ''
    for key in COMMANDS_DICT:
        if user_input.strip().lower().startswith(key):
            new_input = key
            contact = user_input[len(new_input):]
            break
    if contact:
        return reaction_func(new_input)(contact)
    return reaction_func(new_input)()

#---------------------Функція виводу відповіді (ф-ція зі словника або помилка)
def reaction_func(reaction):
    return COMMANDS_DICT.get(reaction, break_func)

#---------------------Функція створення нового контакту---------
def create_contact(contact):
    new_contact = contact.strip().split(" ")
    name = new_contact[0]
    phone = new_contact[1]
    if name.isdigit():
        raise ValueError('You entered wrong name.')
    if not phone.isdigit():
        raise ValueError('You entered wrong phone.')
    return name, phone

#---------------------Функція повідомлення про відсутність введеної команди в словнику-------------
def break_func():
    return "Command not found."

#-----------------Основне тіло програми---------------------

def main():
     while True:
        user_input = input('Enter command for bot: ')
        result = change_input(user_input)
        print(result)
        if result in ['good bye', 'exit', 'close', 'Good bye!']:
            break

#---------------------Точка входу----------------------    
if __name__ == '__main__':
    main()