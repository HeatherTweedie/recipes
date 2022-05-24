# Recipes
This repository contains the code and data for searching a database of recipes for ingredients and tags inputed by the user. 

## Format
Recipe data are in YAML format in [recipes](recipes.yaml). Recipes are in alphabetical order under commented section headers.

### Required fields:
A recipe must have a name, at least one tag, at least one ingredient, and a location. For example:

```yaml
- name: Chocolate chip cookies
  tags:
    - sweet
    - baking
    - cookie
  ingredients:
    - cocoa powder 
    - golden syrup 
    - chocolate chips 
    - milk
  location: Be-Ro Book p16
    
- name: Thai green curry
  tags:
    - savoury
    - main
    - curry
  ingredients:
    - thai green curry paste
    - chilli
    - butternut squash
    - pepper
    - coconut milk
    - mangetout
    - baby corn
    - fresh coriander
  location: "https://www.bbcgoodfood.com/recipes/vegetarian-thai-green-curry"},
```

- `name`: First word must be uppercase, the rest lowercase. No more than eight words.
- `tags`: Lowercase and singular.
- `ingredients`: Lowercase and singular unless singular is silly. Specify fresh/dried/ground for herbs and spices. e.g. carrot, egg, raisins, ground ginger.
- `location`: URL or recipe book and page number.
