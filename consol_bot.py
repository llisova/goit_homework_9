ADDRESS_BOOK = {}



def input_error(func):
    def inner(*args):
        try:
            return(func(*args))
         
        except KeyError:
            return "KeyError"
                
        except ValueError:
            return "Unknown command"
           
        except IndexError:
            return "Please, enter the name and phone number"
                    
    return inner
@input_error
def add_handler(data):
    name = data[0].title()
    phone = data[1]
    ADDRESS_BOOK[name] = phone
    return f"Contact {name}, {phone} sved successfully."

def exit_handler(*args):
    return "Good by!"

def hello_handler(*args):
    return "How can I help you?"
@input_error
def change_handler(data):  #  зберігає в пам'яті новий номер телефону існуючого контакту. Вводиться "change" ім'я та новий номер телефону (через пробіл)
    name = data[0].title()
    new_phone = data[1]
    ADDRESS_BOOK[name] = new_phone
    return f"Contact {name} cahnged with new number {new_phone}"

@input_error
def phone_handler(data): #  виводить у консоль номер телефону для зазначеного контакту. Вводиться ім'я контакту
    name = data[0].title()
    number = ADDRESS_BOOK.get(name)
    if number != None:
        return f"The contact {name} has number {number}"
    return f"Contact {name} is not in the ADDRESSBOOK"

def show_handler(*args): # по команді "show all" виводить всі збереженні контакти з номерами телефонів у консоль
    for name, phone in ADDRESS_BOOK.items():        
        return "{:^7}|{:^10}".format(name, phone)
    

def unkn_command(*args):
    return "Unknown command"

def command_parser(new_raw: str):
    items = new_raw.split()
    for key, value in COMMANDS.items():
        if items[0].lower() in value:
            return key,items[1:]
        elif " ".join(items[:2]).lower() in value:
            return key, items[2:]
    return unkn_command, None    
            
        
COMMANDS = {
    add_handler: ["add"],
    hello_handler: ["hello"],
    change_handler: ["change"],
    phone_handler: ["phone"],
    show_handler: ["show all"],
    exit_handler: ["good bye", "close", "exit"]
}


def main():
    while True:
        user_input = input(">>> ") # add Vlad 0978399927, TypeError якщо немає пробілів
        if not user_input:
             print("Please, enter command you need")
             continue
        func, data = command_parser(user_input)
        result = func(data)
        print(result)
        if func == exit_handler:
            break
        



if __name__ == "__main__":
    main()


