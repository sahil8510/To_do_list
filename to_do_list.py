user_input="random"
data=[]
def show_menu():
    print('Menu:')
    print('1. Add an item')
    print('2. Mark as done')
    print('3. view items')
    print('4. Exit')
while user_input!='4':
    show_menu()
    user_input=input("Enter your choice: ")
    if user_input=='1':
     
        item=input('what is to be done?: ')
        data.append(item)
        print('added item:',item)
    elif user_input=='2':
        item=input('what is to be marked as done?: ')
        if item in data:
            data.remove(item)
            print("removed item:", item)
        else:
            print("item doesn't exist")


    elif user_input=='3':
       for i in data:
            print(i)
       
    elif user_input=="4":
        print('Goodbye')
    else:
       print('please enter one of 1, 2, 3 or 4')    



