# Coding-HSG-Group1134 - Members: Elio Hahn
![University of St. Gallen](https://images.ecosia.org/L_7Z3IlQPAI7RVqrb1QRQpIsVfE=/0x390/smart/https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fen%2Fthumb%2Fb%2Fb5%2FUniversity_of_St._Gallen_logo_english.svg%2F640px-University_of_St._Gallen_logo_english.svg.png)

6,781,1.00 - Skills: Programming - Introduction Level


Welcome to my project. This is a python project for the introductory programming course.


## Installation: 

My application has been developed on the current python version 3.7. In order to run it, said version needs to be properly installed on your machine. Furthermore, make sure that pip is installed properly and is added to the PATH systemvariable if you are on Windows. If needed check the [link for a guide.](https://matthewhorne.me/how-to-install-python-and-pip-on-windows-10/)


In order to get all the needed packages, I included a requirements.txt file in my project folder. To make use of it, open your windows command line , and change the directory to the project’s folder location with the command: 
```
cd ‘folder-location’
```
The same is possible for mac with the command: 
```
cd ~ ‘folder-location’ .
```
Then use the pip command: 
```
pip install -r requirements.txt
```
This will automatically install and update all the packages I have included in my application. The last step is to enter the command: 
```
python main.py 
```
with which my application will be started. 

## Instructions

Once the application is running, the user can navigate throught the menu with the indicated numbers / keys. E.g: To go into sub-menu point 1, simply press 1.

## The application

This application is for people who are looking for new recipes, have ingredients in their home but don't know what to do with them, or simply for those who love cooking. It lets the user search for meals or ingredients and with webscraping it delivers a wide range of recipes. I get the data from https://www.chefkoch.de/ where users share, comment and rate eachother's recipes and it hosts many hundert thousands of them.

Once he/she has found a nice recipe, the user can get more information about the detailed ingredient amounts, the cooking instructions and even an approximation price. The price is calculated with data from the http://coopathome.ch/ website. In the application itself, the approximate price for the whole meal is stated. 

If the user wishes he can save that recipe with all its ingredients and the instruction and let it be sent to his email address. Furthermore he can also request for a shopping list to be generated, where the needed ingredients are listed, with the exact brand and product name that is available at coop, as well as how much the amount used in the recipt would cost. It will ignore common ingredients like salt, pepper, other spices or oil, which are usually already found in a kitchen. The shopping list will be sent per email as well. 

For the price approximation I scraped the Coop website for their per 100g prices. It will then be scaled accordingly to the needs of the recipe. However, sometimes the prices were provided in a different format, such as for eggs, were it will take the per piece price. For the calculation it will take that into account to some degree. However, as there are so many different ingredients and products, it will happen that sometimes the price is off. For that reason I included the possibility to check for the ingredient prices in the shopping list, so that the user can see where the problem occured.

The recipes are hosted on a german-speaking website. Naturally the instructions are in german. However it also possible to search with English ingredient- or mealnames. It might however show different results. For my users who also want to browse the german recipes I included a translator, where all your desired ingredients can be entered, and the German output can then be used in the search function. 
