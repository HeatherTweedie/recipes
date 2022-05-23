"""Search a list of recipes for given criteria and return those that match"""


from recipe_book import recipes


def get_all(recipes, category):
    """Get all of a given available category from all recipes"""
    all_tags = set()
    for recipe in recipes:
        all_tags = all_tags.union(recipe[category])
    return sorted(all_tags)


def get_input(category):
    """Get input as set from user and validate"""
    while True:
        all = get_all(recipes, category)
        user_input = set((input(f"\nWhich {category} would you like to search by? ")).split(", "))
        if not user_input.issubset(all):
            print(f"\nInvalid input. Please enter {category} seperated by ', '. Available {category}: {all}")
        else:
            return user_input


def recipe_search(recipes):
    """Search a list of recipes for given criteria and return those that match"""

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

        while True:
            new_search = input("Would you like to carry out another search? [y/n] ")
            if new_search not in ("y", "n"):
                print("\nPlease answer with y (yes) or n (no).\n")
            else:
                break

        if new_search == 'n':
            return


recipe_search(recipes)
