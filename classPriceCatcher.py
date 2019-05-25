import classCoopPrices as coop
import re


class priceRetriever:

    def __init__(self, ingredients):

        self.rawIngredients = ingredients
        self.ingredients = ingredients
        self.finalIngredients = []
        self.ingredientPrices = []
        self.priceList = []
        self.menuPrice = float()
        self.shoppingList = []

    def filterIngredients(self):
        irrelevant_measurements = ['EL', 'TL', 'Tasse', 'Tassen', 'Prise', 'Msp']
        for each in irrelevant_measurements:
            for i in range(len(self.ingredients)):

                if each in self.ingredients[i][0] or self.ingredients[i][0] == '':
                    self.ingredients[i] = 'irrelevant measurement'
        try:
            for i in range(len(self.ingredients)):
                self.ingredients.remove('irrelevant measurement')
        except ValueError:
            pass

    def findIngredients(self):
        commonIngredientsDict = {'Eigelb':'Eier', 'Eiweiss':'Eier', 'Eiweiß':'Eier', 'Ei':'Eier', 'Ei(er)':'Eier'}
        splitIngredients = []
        for i in range(len(self.ingredients)):
            r = re.compile(r'.*\(.*\)')
            matches = r.findall(str(self.ingredients[i]))
            if matches:
                for match in matches:
                    splitIngredients.append(self.ingredients[i][1].split('('))

            else:
                splitIngredients.append(self.ingredients[i][1].split(' '))

        for i in range(len(splitIngredients)):
            if splitIngredients[i][0] in commonIngredientsDict:
                self.finalIngredients.append(commonIngredientsDict[splitIngredients[i][0]].strip(','))
            else:
                self.finalIngredients.append(splitIngredients[i][0].strip(','))

    def getCoopPrices(self):

        brandsCoop = ['Naturaplan', 'Bio', 'Prix', 'Garantie',
                      'Naturafarm', 'Emmi', 'Floralp', 'Zweifel']

        print('Checking for prices...')

        for ingredient in self.finalIngredients:

            # Create a new instance of the Coop Scraper
            scraper = coop.CoopScraper(ingredient)
            source = scraper.loadCoopWebsite()

            # Save the three lists
            name, weight, price = scraper.extractProductInfo(source)

            # Take only the most relevent results:
            name = name[0:5]
            weight = weight[0:5]
            price = price[0:5]

            brand = []
            # Check if we could find the good
            if name == []:
                print('We could not get prices for ' + str(ingredient))
                self.ingredientPrices.append(str(0) + ',' + str(0) + ',' + str(0.00))

            else:
                # Separate the brand out of the product-name
                for i in range(len(name)):
                    name_splited = ''
                    for coop_brand in brandsCoop:
                        if coop_brand in name[i]:
                            name_splited = name[i].split(' ')
                    brand_string = []
                    counter = 0
                    for substring in name_splited:
                        if substring in brandsCoop:
                            brand_string.append(substring)
                            counter += 1
                    if counter == 0:
                        brand.append('Coop')
                    else:
                        brand.append(' '.join(brand_string))

                # Check if the brand name is in the product name
                for i in range(len(brand)):
                    if brand[i] in name[i]:
                        name[i] = name[i].replace(brand[i], '')

                # Get the cheapest item
                for i in range(len(price)):
                    price[i] = price[i].split()[0]
                    price[i] = price[i].split('/')[0]
                    price[i] = round(float(price[i]), 2)

                minPrice = min(price)
                n = price.index(minPrice)

                # Save the result
                self.ingredientPrices.append(brand[n] + ',' + name[n] + ',' + str(price[n]))


        # Extract the prices only
        for i in range(len(self.ingredientPrices)):
            try:
                self.priceList.append(float(self.ingredientPrices[i].split(',')[2]))
            except ValueError:
                self.priceList.append(float(0))

        for i in range(len(self.priceList)):

            if self.ingredients[i][0] != self.ingredients[i][0].split(" ")[0]:
                try:
                    if float(self.ingredients[i][0].split(" ")[0]) < 20:
                        self.priceList[i] = float("%.2f" % (float(self.ingredients[i][0].split(" ")[0]) * float(self.priceList[i])))
                    else:
                        self.priceList[i] = float("%.2f" % (float(self.ingredients[i][0].split(" ")[0])/ float(1000/self.priceList[i])))
                except:
                    pass

            else:
                try:
                    self.priceList[i] = float("%.2f" % (float(self.ingredients[i][0].split(" ")[0]) * float(self.priceList[i])))
                except:
                    pass


        self.menuPrice = "%.2f" % sum(self.priceList)

        for i in range(len(self.priceList)):
            self.shoppingList.append([self.ingredients[i][0], self.ingredientPrices[i].split(',')[1], str("%.2f" % self.priceList[i]) + " CHF"])


if __name__ == '__main__':
    pass

