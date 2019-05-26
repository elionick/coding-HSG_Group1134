from requests_html import HTML, HTMLSession
from checkFunctions import *
from getFunctions import *


class mealScraper():

    def __init__(self, keyword):
        self.keyword = keyword
        self.recipeList = []
        self.choice = int()
        self.url = ''
        self.originalIngredients = []
        self.ingredients = []
        self.instructions = ''

    def getMeals(self):
        session = HTMLSession()
        r = session.get(f'https://www.chefkoch.de/rs/s0/{self.keyword}/Rezepte.html')

        recipes = r.html.find('article')
        i = 1
        
        # Find title, time, difficulty and recipe-URL
        try:
            for recipe in recipes:
                title = recipe.find('h2', first=True).text
                time = recipe.find('.recipe-preptime', first=True).text[1:]
                difficulty = recipe.find('.recipe-difficulty', first=True).text[1:]
                recipeURL = recipe.find('a', first=True).attrs['href']
                self.recipeList.append([i, title, time, difficulty, recipeURL])
                i += 1
        except (TimeoutError, AttributeError):
            print('Error! Website not responding. Try again!')

    # Show the recipes for a desired ingredient / meal by the user. Also he can say how many.
    def showRecipes(self, *args):
        arglist = list(args)
        try:
            arglist[0] = int(arglist[0])
        except ValueError:
            pass
        print()
        if isinstance(arglist[0], int):
            if arglist[0] < len(self.recipeList):
                length = arglist[0]
            else:
                length = len(self.recipeList)
        else:
            if 5 <= len(self.recipeList):
                length = 5
            else:
                length = len(self.recipeList)

        for i in range(length):
            print(f'Recipe Nr: {self.recipeList[i][0]}\nTitle: {self.recipeList[i][1]}\nTime: {self.recipeList[i][2]}\nDifficulty: {self.recipeList[i][3]}')
            print("--------------------------------------------")

        i = 0
        while i == 0:
            self.choice = input('Which recipe would you like to inspect?: ')
            if checkStringIsInt(self.choice) == False:
                print(getErrorMessage('choice'))
            elif int(self.choice) > length:
                print(getErrorMessage('choice'))
            else:
                self.choice = int(self.choice)
                i = 1

    # Get detailed information for recipe chosen.
    def getRecipe(self):
        self.choice = self.choice-1
        self.url = self.recipeList[self.choice][4]

        try:
            session = HTMLSession()
            r = session.get(self.url)
            ingredients = r.html.find('.incredients', first=True).find('tr')
            for ingredient in ingredients:
                amount = ingredient.find('.amount')[0].text.replace('\xa0', ' ')
                type = ingredient.find('td')[1].text
                self.originalIngredients.append([amount, type])
                self.ingredients.append([amount, type])

            self.instructions = r.html.find('.instructions', first=True).text
        except:
            print('Error! There seems to be a problem with this recipe. Try again!')


if __name__ == '__main__':
    pass

