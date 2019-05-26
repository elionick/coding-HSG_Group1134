from classWebscraper import *
from classCoopPrices import *
from classPriceCatcher import *
from sendEmail import *
from translateFunctions import *
from uiFunctions import *
import time

choice = ''
clear_screen()
print('Welcome to my application. I hope you are hungry!')
time.sleep(2)


# Main Menu
while choice not in ['q', 'Q']:
    if 'translations' in globals():
        translationString = '\n'.join(translations)
    else:
        translations = []
        translationString = ''

    choice = uiMenu(mainMenu, menu_title='Main Menu',sub_title=f'In this application you can search for a meal and we will suggest recipes. \nHowever, this search is only available in german. So if you need some help with the translation I also implemented a translator. \nYour translations will appear here!\n\n{translationString} ', user_instruction='What would you like to do?')
    
    # Menu for finding a recipe
    if choice == 1:

        # Look for a recipe
        choice = uiMenu(chooseMeal, menu_title='Look for a recipe', sub_title=f'Your translations: \n\n{translationString}',input_type='questions')
        meal = str(choice[0])

        ms = mealScraper(choice)
        ms.getMeals()
        
        # Chose a recipe
        choice = uiMenu(numberOfRecipes, menu_title=f'Recipes for {meal}!', input_type='questions')
        ms.showRecipes(choice[0])
        ms.getRecipe()

        while choice not in ['q', 'Q']:
            choice = uiMenu(recipeMenu, menu_title=f'You chose {ms.recipeList[ms.choice][1]}!' ,sub_title='What would you like to do?')

            if choice == 1:
                if 'pr' in globals():
                    del pr

                #Get the prices for the recipe!
                pr = priceRetriever(ms.ingredients)
                pr.filterIngredients()
                pr.findIngredients()
                pr.getCoopPrices()

                if 'ingredients' not in globals():
                    for i in range(len(ms.originalIngredients)):
                        ms.originalIngredients[i] = ' '.join(ms.originalIngredients[i])

                    ingredients = '\n'.join(ms.originalIngredients)

                choice = uiMenu(detailMenu, menu_title=f'Here are the ingredients:', sub_title=f'\nThe price is aproximately: {pr.menuPrice} CHF in Coop! (For more info check the shopping list)\n\n{ingredients}\n\n{ms.instructions}')
                
                # Send recipe to email
                if choice == 1:
                    while choice not in ['q', 'Q']:
                        choice = uiMenu(email, menu_title='Sending the recipe!', input_type='questions')
                        if checkEmail(choice[0]):
                            sendEmail(choice, 'recipe', [pr.menuPrice, ingredients, ms.instructions])
                            print(f'An email has been sent to {choice[0]}')
                            time.sleep(2)

                            choice = ''
                            break
                        
                # Send shoppinglist to email
                if choice == 2:
                    while choice not in ['q', 'Q']:
                        choice = uiMenu(email, menu_title='Sending the shoppinglist!', input_type='questions')
                        if checkEmail(choice[0]):
                            sendEmail(choice, 'shoppinglist', [pr.ingredientPrices, pr.priceList, pr.menuPrice])
                            print(f'An email has been sent to {choice[0]}')
                            time.sleep(2)

                            choice = ''
                            break
                        
                # Go back in menu
                if choice == 3:
                    choice = ''
                    break
                    
            # Send recipe to email
            if choice == 2:
                while choice not in ['q', 'Q']:
                    choice = uiMenu(email, menu_title='Sending the recipe!', input_type='questions')
                    if checkEmail(choice[0]):
                        # Get the prices for the recipe!
                        if 'pr' in globals():
                            del pr
                        pr = priceRetriever(ms.ingredients)
                        pr.filterIngredients()
                        pr.findIngredients()
                        pr.getCoopPrices()

                        if 'ingredients' not in globals():
                            for i in range(len(ms.originalIngredients)):
                                ms.originalIngredients[i] = " ".join(ms.originalIngredients[i])

                            ingredients = '\n'.join(ms.originalIngredients)

                        sendEmail(choice, 'recipe', [pr.menuPrice, ingredients, ms.instructions])
                        print(f'An email has been sent to {choice[0]}')
                        time.sleep(2)

                        choice = ''
                        break
            # Go back in menu
            if choice == 3:
                choice = ''
                break
                
    # Menu for translator
    if choice == 2:
        while choice not in ['q', 'Q']:
            choice = uiMenu(translator, menu_title='Translator', input_type='questions', quit_option=True)
            translation = translate(choice[0])
            translations.append(f'{choice[0]} - {translation}')
            print(translations)
            time.sleep(1)
            break


# Show Quit
print('Goodbye! Enjoy your meal')
