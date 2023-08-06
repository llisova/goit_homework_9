ADDRESS_BOOK = {}

def add_handler(data):
    name = data[0].title()
    phone = data[1]
    ADDRESS_BOOK[name] = phone
    return f"Contact {name}, {phone} sved successfully."

def exit_handler(*args):
    return "Good by!"

def hello_handler(*args):
    return "How can I help you?"

def change_handler(data):  #  зберігає в пам'яті новий номер телефону існуючого контакту. Вводиться "change" ім'я та новий номер телефону (через пробіл)
    name = data[0].title()
    new_phone = data[1]
    ADDRESS_BOOK[name] = new_phone
    return f"Contact {name} cahnged with new number {new_phone}"

def phone_handler(name: str): #  виводить у консоль номер телефону для зазначеного контакту. Вводиться ім'я контакту
    for name, number in ADDRESS_BOOK.items():
        return f"The contact {name} has number {number}"

def show_handler(*args): # по команді "show all" виводить всі збереженні контакти з номерами телефонів у консоль
    return f" Your contacts: {ADDRESS_BOOK}"

def input_error(func):
    def inner(*args):
        try:
            return(func(*args))
         
        except KeyError:
            return "Please, enter right command"
                
        except ValueError:
            return "ValueError"
                
        except IndexError:
            return "IndexError"
                    
    return inner
        




def command_parser(new_raw: str):
    items = new_raw.split()
    for key, value in COMMANDS.items():
        if items[0].lower() in value:
            return key,items[1:]
        
        
COMMANDS = {
    add_handler: ["add"],
    hello_handler: ["hello"],
    change_handler: ["change"],
    phone_handler: ["phone"],
    show_handler: ["show_all"],
    exit_handler: ["good_bye", "close", "exit"]
}

@input_error
def main():
    while True:
        user_input = input(">>> ") # add Vlad 0978399927, TypeError якщо немає пробілів
        # if not user_input: # IndexError
        #     continue
        func, data = command_parser(user_input)
        if func == exit_handler:
            break
        result = func(data)
        print(result)



if __name__ == "__main__":
    main()


