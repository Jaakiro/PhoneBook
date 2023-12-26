file = 'Phonebook.txt'

def input_contact(file):
    count = count_contact(file)
    input_ = list()
    input_.append(str(count))
    input_.append(input("Enter name: "))
    input_.append(input("Enter comment: "))
    input_.append(input("Enter phone: "))
    return input_

def count_contact(file):
    with open(file, 'r') as fp:
        return sum([1 for line in fp])

def create_contact(file):
    contact = input_contact(file)
    with open(file, 'a', encoding='utf-8') as f:
        f.write(';'.join(contact) + '\n')

def show_contact(file):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')

def searching(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        print(line, end='')
    id_search = int(input("Enter contact number: "))
    if 0 <= id_search <= len(lines):
        print(lines[id_search])
    else:
        print("Contact not found")

def change_contact(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        print(line, end='')
    id_change = int(input("Enter id to change: "))
    if 0 <= id_change <= len(lines):
        contact = input_contact(file)
        contact[0] = str(id_change)
        contact = ';'.join(contact) + '\n'
        lines[id_change] = contact

    with open(file, 'w') as f:
        f.writelines(lines)

def removing(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        print(line, end='')
    id_remove = int(input("Enter id to remove: "))
    if 0 <= id_remove <= len(lines):
        lines.pop(id_remove)
    with open(file, 'w') as f:
        f.writelines(lines)

while True:
    using = int(input("1. Adding \n2. Removing \n3. Searching \n4. Change \n5. Show \n6. Exit \nEnter your choice: "))
    if using == 1:
        create_contact(file)
    elif using == 2:
        removing(file)
    elif using == 3:
        searching(file)
    elif using == 4:
        change_contact(file)
    elif using == 5:
        show_contact(file)
    elif using == 6:
        print("Thank you for using our phonebook app")
        break



