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
    return sorted(all_tags)

def get_input(category):
    while True:
        all = get_all(recipes, category)
        user_input = set((input(f"\nWhich {category} would you like to search by? ")).split(", "))
        if not user_input.issubset(all):
            print(f"\nInvalid input. Available {category}: {all}")
        else:
            return user_input


def recipe_search(recipes):

    while True:
        
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
