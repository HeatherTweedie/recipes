"""Function to search a list of recipes for given criteria and return those that match"""


from recipe_book import recipes


def get_valid(prompt, correction_prompt, validator):
    while True:
        result = input(prompt)
        if not validator(result):
            print(correction_prompt)
        else:
            return result


def recipe_search(recipes):

    while True:
        
        INGREDIENT_PROMPT = "\nWhich ingredient would you like to search by? "
        INGREDIENT_CORRECTION_PROMPT = "\nPlease enter a string.\n"
        CATEGORY_PROMPT = "Would you like to make something sweet or savoury? "
        CATEGORY_CORRECTION_PROMPT = "\nPlease answer with 'sweet' or 'savoury'.\n"

        ingredient = get_valid(INGREDIENT_PROMPT, INGREDIENT_CORRECTION_PROMPT, lambda ingredient : ingredient)
        category = get_valid(CATEGORY_PROMPT, CATEGORY_CORRECTION_PROMPT, lambda category : category in ("sweet", "savoury"))

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
