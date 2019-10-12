import string
import random
import re

def load_password_list():
    print("loading")
    
def generate_password1():
    length=int(input("enter length of password: "))
    n=int(input("Enter number of password to be generated: ")) #number of password to be generated
    print("generating password")
    str=string.ascii_letters+"0123456789@#$%&*?_[](){}<>"
    i=0
    while(i<n):
        p="".join(random.sample(str,length))
        if(p[0].isupper() and re.findall("[0-9]", p) and re.findall("[a-z]", p) and re.findall("[@#{}$*%()&?_<>]",p)):
            print(p)
            i+=1
            
def generate_password2():
    length=int(input("enter length of password: "))
    n=int(input("Enter number of password to be generated: ")) #number of password to be generated
    print("generating password")
    str=string.ascii_letters
    i=0
    while(i<n):
        p="".join(random.sample(str,length))
        if(p[0].isupper()and re.findall("[a-z]", p)):
            print(p)
            i+=1
            
def generate_password3():
    length=int(input("enter length of password: "))
    n=int(input("Enter number of password to be generated: ")) #number of password to be generated
    print("generating password")
    str=string.ascii_letters+"0123456789"
    i=0
    while(i<n):
        p="".join(random.sample(str,length))
        if(p[0].isupper() and re.findall("[0-9]", p) and re.findall("[a-z]", p)):
            print(p)
            i+=1
def generate_password4():
    length=int(input("enter length of password: "))
    n=int(input("Enter number of password to be generated: ")) #number of password to be generated
    print("generating password")
    str="0123456789"
    i=0
    while(i<n):
        p="".join(random.sample(str,length))
        print(p)
        i+=1

        
def menu_choice():
    """ Find out what the user wants to do next. """
    print("Choose one of the following options?")
    print("   g) generate New password")
    print("   q) Quit")
    choice = input("Choice: ")    
    if choice.lower() in ['g','q']:
        return choice.lower()
    else:
        print(choice +"?" + " That is an invalid option!!!")
        return None
def password_condition():
    print("Choose one of the following options?")
    print("  a for password with aplhanumeric and contains symbol's")
    print("  b for password with only alphabets")
    print("  c for password with only aplhabets and numbers")
    print("  d for password with only numbers(OTP)")
    option=input("choice: ")
    if option.lower() in ['a','b','c','d']:
        return option.lower()
    else:
        print(option +"?" + " That is an invalid option!!!")
        return None
        
 
def main_loop():
    
    load_password_list()
    while True:
        choice = menu_choice()
        if choice == None:
            continue
        if choice == 'q':
            print( "Exiting...")
            break     # jump out of while loop
        elif choice == 'g':
            option = password_condition()
            if option == 'a':
                generate_password1()
            if option == 'b':
                generate_password2()
            if option == 'c':
                generate_password3()
            if option == 'd':
                generate_password4()
        else:
            print("Invalid choice.")


if __name__ == '__main__':
    main_loop()
