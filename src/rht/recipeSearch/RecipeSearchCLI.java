import java.io.IOException;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Scanner;

public class RecipeSearchCLI {

    private final RecipeInterface recipeDB;

    public RecipeSearchCLI(RecipeInterface recipeDB) {
        this.recipeDB = recipeDB;
    }

    public static void main(String args[]) {
        try (Scanner sc = new Scanner(System.in)) {
            RecipeInterface recipeDB = new SQLRecipeDB("recipes.sqlite");
            RecipeSearchCLI cli = new RecipeSearchCLI(recipeDB);
            cli.mainMenu(sc);

        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }

    private void mainMenu(Scanner sc) throws IOException, SQLException {
        while (true) {
            System.out.println("What would you like to do today?");
            System.out.println("0: Quit");
            System.out.println("1: List all recipes");
            System.out.println("2: Add a recipe");
            System.out.println("3: Remove a recipe");
            System.out.print("Option: ");

            int choice = Integer.parseInt(sc.nextLine());

            switch (choice) {
                case 0:
                    return;
                case 1:
                    listAllRecipes();
                    break;
                case 2:
                    System.out.print("Name: ");
                    String name = sc.nextLine();
                    System.out.print("Location: ");
                    String location = sc.nextLine();
                    String tags = "tags";
                    String ingredients = "ingredients";
                    addRecipe(name, tags, ingredients, location);
                    break;
                case 3:
                    System.out.println("Which recipe would you like to remove?");
                    int removeID = Integer.parseInt(sc.nextLine());
                    removeRecipe(removeID);
                    break;
                default:
                    System.out.println("Invalid option.");
            }
        }

    }

    private void listAllRecipes() throws IOException, SQLException {
        ArrayList<Recipe> recipes = recipeDB.getAllRecipes();
        for (Recipe recipe : recipes) {
            System.out.println(recipe.getID() + ": " + recipe.getName() + ": " + recipe.getLocation());
        }
    }

    private void addRecipe(String name, String tags, String ingredients, String location)
            throws IOException, SQLException {
        recipeDB.addRecipe(name, tags, ingredients, location);
        System.out.println("Added " + name);
    }

    private void removeRecipe(int id) throws IOException, SQLException {
        recipeDB.removeRecipe(id);
        System.out.println("Removed entry " + id + ".");
    }
}
