"""Search a list of recipes for given criteria and return those that match"""


from recipe_book import recipes


def get_valid(prompt, correction_prompt, validator):
    while True:
        result = input(prompt)
        if not validator(result):
            print(correction_prompt)
        else:
            return result

def get_all(recipes, category):
    all_tags = set()
    for recipe in recipes:
        all_tags = all_tags.union(recipe[category])
    return all_tags

def get_input(category):
    all = sorted(get_all(recipes, category))
    print(f"Available {category}: {all}")
    user_input = input(f"Which {category} would you like to search by? ")
    return set(user_input.split(", "))


def recipe_search(recipes):

    while True:
        
        #INGREDIENT_PROMPT = "\nWhich ingredient would you like to search by? "
        #INGREDIENT_CORRECTION_PROMPT = "\nPlease enter a string.\n"
        #CATEGORY_PROMPT = "What tags would you like to search by? "
        #CATEGORY_CORRECTION_PROMPT = "\nPlease enter at least one tag.\n"

        #ingredient = get_valid(INGREDIENT_PROMPT, INGREDIENT_CORRECTION_PROMPT, lambda ingredient : ingredient)
        #category = get_valid(CATEGORY_PROMPT, CATEGORY_CORRECTION_PROMPT, lambda category : category in ("sweet", "savoury"))
        
        ingredients = get_input("ingredients")
        tags = get_input("tags")

        suggestions = [f"{recipe['name']}: {recipe['location']}" for recipe in recipes
            if ingredients.issubset(recipe["ingredients"]) and tags.issubset(recipe["tags"])]

        if not suggestions:
            print("\nYou have no recipes that match those criteria.\n")
        else:
            print(f"\n{tags} recipes containing {ingredients}:\n")
            print("\n".join(suggestions))

        NEW_SEARCH_PROMPT = "\nWould you like to carry out another search? [y/n] "
        NEW_SEARCH_CORRECTION_PROMPT = "\nPlease answer with y (yes) or n (no).\n"

        new_search = get_valid(NEW_SEARCH_PROMPT, NEW_SEARCH_CORRECTION_PROMPT, lambda result : result in ("y", "n"))

        if new_search == 'n':
            return


recipe_search(recipes)
