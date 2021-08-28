import csv

filenames = ["01_Recipe_Details.csv", "02_Ingredients.csv", "03_Compound_Ingredients.csv", "04_Recipe-Ingredients_Aliases.csv"]
    
data = [[],[],[],[]]
    
for i in range(4):
    f = open(filenames[i], "r")
    lines = csv.reader(f)
    
    for line in lines:
        data[i].append(line)

def find_potential(words):
    ingredients = []
    
    for i in range(len(data[1])):
        for word in words:
            if word.lower() == data[1][i][0].lower():
                ingredients.append(int(data[1][i][2]))
    
    recipe_ingredients = [[] for i in range(len(data[3]))]
    for i in range(1, len(data[3]), 1):
        index = int(data[3][i][0]) - 1
        recipe_ingredients[index].append(int(data[3][i][3]))
    
    potential_recipes = []
    for i in range(1, len(recipe_ingredients), 1):
        contains = True
        for ingredient in ingredients:
            if ingredient not in recipe_ingredients[i]:
                contains = False
        if contains:
            potential_recipes.append(i+1)
    
    return potential_recipes

def details(potential_recipes):
    details = []

    for recipe in potential_recipes:
        details.append(data[0][recipe])

    return details
