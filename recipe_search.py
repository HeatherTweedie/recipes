"""Function to search a list of recipes for given criteria and return those that match"""


from recipe_book import recipes


def get_valid_ingredient():

    while True:
        ingredient = input("\nWhich ingredient would you like to search by? ")
        if not ingredient:
            print("\nPlease enter a string.\n")
        else:
            return ingredient


def get_valid_category():

    while True:
        category = input("Would you like to make something sweet or savoury? ")
        if category not in ("sweet", "savoury"):
            print("\nPlease answer with 'sweet' or 'savoury'.\n")
        else:
            return category


def recipe_search(recipes):

    while True:
        
        ingredient = get_valid_ingredient()
        category = get_valid_category()

        suggestions = [f"{recipe['name']}: {recipe['url']}" for recipe in recipes
            if ingredient in recipe["ingredients"] and category in recipe["category"]]

        if not suggestions:
            print("\nYou have no recipes that match those criteria.\n")
        else:
            print(f"\n{category.title()} recipes containing {ingredient}:\n")
            print("\n".join(suggestions))

        while True:
            new_search = input("\nWould you like to carry out another search? [y/n] ")
            if new_search == 'y':
                break
            elif new_search == 'n':
                return
            else:
                print("\nPlease answer with y (yes) or n (no).\n")

recipe_search(recipes)
