# create a contacts dict, where the user can search for a person
# name and if the name exists, it display the phone no
# else, the user should be provided a choice to add  the phone no of a person . 
# Also the user can also choose to list all person and numbers


from traceback import print_list

contacts = {
    'emergency': 101,
    'police': 100
}

while True:
    print('# options')
    print('1️⃣  Search person')
    print('2️⃣  View all')
    print('3️⃣  Exit')
    ans = input("enter a number: ")
    if ans  == '1':
        name = input("enter the persons' name: ")
        if name in contacts:
            print(f"👉 {name} => {contacts[name]}")
        else:
            print(f"Not found, would you like to add the {name}s' number?")
            number = input(f'enter number for {name} =>')
            contacts[name] = number
            print('details added')
    elif ans == '2':
        for name, number in contacts.items():
            print(f'👉 {name} => {number}')
    elif ans == '3':
        print("BYE")
        break
    else:
        print("⚠️ wrong input ⚠️")