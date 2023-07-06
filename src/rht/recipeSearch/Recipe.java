public class Recipe {

    private final String name;
    private final String[] tags;
    private final String[] ingredients;
    private final String location;

    public Recipe(String name, String[] tags, String[] ingredients, String location) {
        this.name = name;
        this.tags = tags;
        this.ingredients = ingredients;
        this.location = location;
    }

    public String getName() {
        return this.name;
    }

    public String[] getTags() {
        return this.tags;
    }

    public String[] getIngredients() {
        return this.ingredients;
    }

    public String getLocation() {
        return this.location;
    }
}