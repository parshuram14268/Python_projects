phones = [['Rahul reddy', '(977)9122590263'], #contact
          ['Parshuram Kumar', '(91)8825829622'],
          ['Asutosh Mopatra','(91)7928128970'],
          ['Nithin Thota','(91)9798567903']]
name_pos = 0
phone_pos = 1
phone_header = [ 'Name', 'Phone Number']

def proper_menu_choice(which):
    if not which.isdigit():
        print ("'" + which + "' must to be the number of a phone!")
        return False
    which = int(which)
    if which < 1 or which > len(phones):
        print ("'" + str(which) + "' must to be the number of a phone!")
        return False
    return True
    
def remove_phone(which):
    if not proper_menu_choice(which):
        return
    which = int(which)

    del phones[which-1]
    print( "Deleted phone #", which)

def edit_phone():
    print("Editing")

  
def save_phone_list():
    print("saving")
  
def load_phone_list():
    print("loading")

def show_phones():
    show_phone(phone_header, "")
    index = 1
    for phone in phones:
        show_phone(phone, index)
        index = index + 1
    print()

def show_phone(phone, index):
    outputstr = "{0:>3}  {1:<20}  {2:>16}"
    print(outputstr.format(index, phone[name_pos], phone[phone_pos]))

def create_phone():
    print("Enter the data for a new phone:")
    newname = input("Enter name: ")
    newphone_num = input("Enter phone number: ")
    phone = [newname,newphone_num]
    phones.append(phone)
    print()
    
def menu_choice():
    
    print("Choose one of the following options?")
    print("   s) Show Contact List")
    print("   n) Add New Contact")
    print("   d) Delete Contact")
    print("   e) Edit Contact")
    print("   q) Quit")
    choice = input("Choice: ")    
    if choice.lower() in ['n','d', 's','e', 'q']:
        return choice.lower()
    else:
        print(choice +"?" + " That is an invalid option!!!")
        return None


def main_loop():
    
    load_phone_list()
    
    while True:
        choice = menu_choice()
        if choice == None:
            continue
        if choice == 'q':
            print( "Exiting...")
            break     # come out of while loop
        elif choice == 'n':
            create_phone()
        elif choice == 'd':
            which = input("Which contact do you want to delete? ")
            print("which is ", which)
            remove_phone(which)
        elif choice == 's':
            show_phones()
        elif choice == 'e':
             edit_phone()
        else:
            print("Invalid choice.")
            
    save_phone_list()
    
 
if __name__ == '__main__':
    main_loop()
