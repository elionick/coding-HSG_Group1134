import datetime
# gets a choice input
def getChoiceInput(user_input):
    if user_input not in ['q', 'Q']:
        return int(user_input)
    else:
        return user_input
    
# Get a certain error message
def getErrorMessage(error_code):
    errorMessages = {
    'choice' : 'Error! Please enter a valid option.',
    'email' : 'Error! Please enter a valid email.',
    }
    return errorMessages[error_code]


if __name__ == '__main__':
    pass
