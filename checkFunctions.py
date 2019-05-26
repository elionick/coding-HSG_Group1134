from validate_email import validate_email

# checks if user input is possible choice
def checkIfChoice(input, poss_options, quit_option = True):
    if quit_option == True:
        if input not in ["q", "Q"]:
            try:
                int(input)
                if int(input) in poss_options:
                    return True
                else:
                    return False
            except ValueError:
                return False
        else:
            return True
    else:
        try:
            int(input)
            if int(input) in poss_options:
                return True
            else:
                return False
        except ValueError:
            return False

# Checks if string is integer
def checkStringIsInt(input):
    try:
        if input.isdigit() == True:
            return True
        else:
            return False
    except ValueError:
        return False

#Checks if string contains a number
def checkIfStringContainsNumbers(input):
        return any(char.isdigit() for char in input)

# Checks if a string is in a valid email address format
def checkEmail(input):
    return True if validate_email(input) == True else False


if __name__ == "__main__":
    pass
