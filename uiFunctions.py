from checkFunctions import *
from getFunctions import *
from menuElements import *
import os
import platform

# Clears the command prompt, depending on user's OS
def clear_screen():
    if platform.system().lower()=='windows':
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)

# Displays a menu and returns an input
def uiMenu(menu_elements_list, menu_title = None, sub_title = None, user_instruction = None, nOptions = None, input_type = "choice",
            clear = True, quit_option = True):

    if input_type == "questions":
        answers = []

    while True:
        if clear == True:
            clear_screen()

        if menu_title != None:
            if isinstance(menu_title, str) == False:
                menu_title()
                print("")
            else:
                print("*** " + menu_title + " ***")
                print("")
        if sub_title != None:
            if isinstance(sub_title, str) == False:
                sub_title()
                print("")
            else:
                print(sub_title)
                print("")
        
        #Prints the user's options and returns his input
        if input_type == "choice":
            for index, element in enumerate(menu_elements_list):
                print(str(index + 1) + ":\t", end = "")
                print(element)
            if quit_option == True:
                print("q:\tQuit")
            print("")
            if user_instruction != None:
                print(user_instruction)
            user_input = input()
            if nOptions == None:
                nOptions = len(menu_elements_list)
            if checkIfChoice(user_input, range(1, nOptions + 1), quit_option = quit_option)  == False:
                error_status = True
            else:
                choice = getChoiceInput(user_input)
                return choice
            
        #Prints the questions and returns the input
        if input_type == "questions":
            for index, answer in enumerate(answers):
                print(menu_elements_list[index] + ": " + answer)
                print("")
            user_input = input(menu_elements_list[len(answers)] + ": ")
            answers.append(user_input)
            if len(menu_elements_list) == len(answers):
                return answers


if __name__ == "__main__":
    pass
