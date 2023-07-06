import java.sql.SQLException;
import java.util.ArrayList;

interface RecipeInterface {

    public void addRecipe(String name, String tags, String ingredients, String location) throws SQLException;

    public void removeRecipe(int id) throws SQLException;

    public ArrayList<Recipe> getAllRecipes() throws SQLException;

}
