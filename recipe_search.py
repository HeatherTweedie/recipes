# Copyright 2022 Heather Tweedie
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file
# except in compliance with the License. You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the
# License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing permissions and
# limitations under the License.

"""Search a list of recipes for given criteria and return those that match"""


from recipe_scrapers import scrape_me
import yaml


def get_all(recipes, category):
    """Get all of a given available category from all recipes"""
    all = set()
    for recipe in recipes:
        all = all.union(recipe[category])
    return sorted(all)


def get_input(category):
    """Get input from user and validate"""
    while True:
        all = get_all(recipes, category)
        all_string = ", ".join(all)
        user_input = set((input(f"\nWhich {category} would you like to search by? ")).split(", "))
        if "none" in user_input:
            user_input = "none"
            return user_input
        if not user_input.issubset(all):
            print(f"\nInvalid input. Please enter {category} separated by ', '. Available {category}: {all_string}.")
        else:
            return user_input


def format_recipe(recipe_to_format):
    """Scrape recipe from website (if available) and print to terminal"""
    scraper = scrape_me(recipe_to_format["location"])
    ingredients = "\n-".join(scraper.ingredients())
    print(f"\n--{scraper.title()}--")
    print("\nIngredients:\n")
    print(f"-{ingredients}")
    print("\nInstructions:\n")
    print(scraper.instructions())


def get_valid_y_n(prompt, correction):
    """Get y/n input and check validity"""
    while True:
        user_input = input(prompt)
        if user_input not in ("y", "n"):
            print(correction)
        else:
            return user_input
        

def recipe_search(recipes):
    """Search a list of recipes for given criteria and return those that match"""

    while True:
        
        ingredients = get_input("ingredients")
        tags = get_input("tags")

        suggestions = []
        count = 0
        tags_string = ", ".join(tags)
        ingredients_string = ", ".join(ingredients)
        if tags == "none":
            for recipe in recipes:
                if ingredients.issubset(recipe["ingredients"]):
                    count += 1
                    suggestions.append(recipe)
                    message = f"\nAll recipes containing {ingredients_string}:\n"
        elif ingredients == "none":
            for recipe in recipes:
                if tags.issubset(recipe["tags"]):
                    count += 1
                    suggestions.append(recipe)
                    message = f"\nAll {tags_string} recipes:\n"
        else:
            for recipe in recipes:
                if ingredients.issubset(recipe["ingredients"]) and tags.issubset(recipe["tags"]):
                    count += 1
                    suggestions.append(recipe)
                    message = f"\n{tags_string} recipes containing {ingredients_string}:\n"

        if not suggestions:
            print("\nYou have no recipes that match those criteria.\n")
        else:
            print(message)
            print("\n".join((f"{suggestions.index(recipe) + 1}. {recipe['name']}: {recipe['location']} (scrapable: {recipe['scrapable']})") for recipe in suggestions))

        while True:
            view_recipe = get_valid_y_n(("\nWould you like to view a recipe? [y/n] "),
                                        ("\nPlease answer with 'y' (yes) or 'n' (no)."))
            if view_recipe == "y":
                recipe_index = int(input("Which recipe would you like to view? ")) - 1
                recipe_to_view = suggestions[recipe_index]
                if recipe_to_view["scrapable"] == True:
                    print(format_recipe(recipe_to_view))
                else:
                    print("That recipe is not available to view.")
            else:
                break

        new_search = get_valid_y_n(("\nWould you like to carry out another search? [y/n] "), 
                                    ("\nPlease answer with 'y' (yes) or 'n' (no).\n"))
        if new_search == 'n':
            return


if __name__ == "__main__":
    with open("recipes.yaml", "r", encoding="utf-8") as stream:
        recipes = yaml.safe_load(stream)
    recipe_search(recipes)
