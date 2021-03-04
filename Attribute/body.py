from main import main


def Body():
    print("Hi, Please select the Menu what you want to get it")
    menu_input = input("here: ")
    input_list = []
    
    while 1:
        if menu_input == 1:
            print("Testing")
            input_list.append(menu_input)
            break

        elif menu_input == 2:
            print("Testing2")
            input_list.append(menu_input)
            break

        elif menu_input == 3:
            print("Testing3")
            input_list.append(menu_input)
            break

        elif menu_input == 4:
            print("Testing4")
            input_list.append(menu_input)
            break

        elif menu_input == 5 or menu_input == 'q' or menu_input == 'Q':
            print("Terminated the program")
            exit(0)

        else:
            print("Go back to menu")
            Body()
