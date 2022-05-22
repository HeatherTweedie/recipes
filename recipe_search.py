"""Function to search a list of recipes for given criteria and return those that match"""


from recipe_book import recipes

def recipe_search(recipes):

    repeat = True

    while repeat == True:

        ingredient = input("\nWhich ingredient would you like to search by? ")
        type = input("Would you like to make something sweet or savoury? ")
        suggestions = "\n"

        for recipe in recipes:
            if ingredient in recipe["ingredients"] and type in recipe["type"]:
                recipe_name = recipe["name"]
                recipe_url = recipe["url"]
                suggestions += f"{recipe_name}: {recipe_url}\n"

        if suggestions == "\n":
            print("\nYou have no recipes that match those criteria.\n")
        else:
            print(f"\n{type.title()} recipes containing {ingredient}: \n{suggestions}")

        valid = False
        while valid == False:
            new_search = input("Would you like to carry out another search? [y/n] ")
            if new_search in ('y', 'n'):
                if new_search == 'y':
                    valid = True
                    repeat = True
                if new_search == 'n':
                    valid = True
                    repeat = False
            else:
                valid = False
                print("\nPlease answer with y (yes) or n (no).\n")

recipe_search(recipes)
