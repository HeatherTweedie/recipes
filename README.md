# Recipes
This repository contains the code and data for searching a database of recipes for ingredients and tags inputed by the user. 

## Format
Recipe data are in YAML format in [recipes](recipes.yaml).

### Required fields:
A recipe must have a name, at least one tag, at least one ingredient, and a location. For example:

```yaml
- name: Apple crumble
    tags:
      - sweet
      - pudding
    ingredients:
      - apple
      - cinnamon
    location: "https://www.bbc.co.uk/food/recipes/applecrumble_2971"
```

- `name`: First word must be uppercase, the rest lowercase. No more than eight words.
- `tags`: Lowercase and singular.
- `ingredients`: Lowercase and singular unless singular is silly. Specify fresh/dried/ground for herbs and spices. e.g. carrot, egg, raisins, ground ginger.
- `location`: URL or recipe book and page number.
