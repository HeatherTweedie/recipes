import java.sql.Statement;
import java.util.ArrayList;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class SQLRecipeDB implements RecipeInterface {

    private final Connection con;

    public SQLRecipeDB(String filename) throws SQLException {
        con = DriverManager.getConnection("jdbc:sqlite:" + filename);
        System.out.println("Connected to database " + filename);

        String createTable = "CREATE TABLE IF NOT EXISTS recipes (\n"
                + "name text NOT NULL, \n"
                + "tags text, \n"
                + "ingredients text, \n"
                + "location text\n"
                + ");";
        try (Statement stmt = con.createStatement()) {
            stmt.execute(createTable);
        }
    }

    @Override
    public void addRecipe(String name, String tags, String ingredients, String location) throws SQLException {
        PreparedStatement ps = con
                .prepareStatement("INSERT INTO recipes (name, tags, ingredients, location) VALUES (?,?,?,?)");
        ps.setString(1, name);
        ps.setString(2, tags);
        ps.setString(3, ingredients);
        ps.setString(4, location);
        ps.executeUpdate();
    }

    @Override
    public void removeRecipe(int id) throws SQLException {
        PreparedStatement ps = con.prepareStatement("DELETE FROM recipes WHERE rowid = ?");
        ps.setInt(1, id);
        ps.executeUpdate();
    }

    @Override
    public ArrayList<Recipe> getAllRecipes() throws SQLException {
        String query = "SELECT rowid, name, tags, ingredients, location FROM recipes";
        ArrayList<Recipe> recipes = new ArrayList<Recipe>();

        try (Statement stmt = con.createStatement()) {
            ResultSet rs = stmt.executeQuery(query);
            while (rs.next()) {
                int id = rs.getInt("rowid");
                String name = rs.getString("name");
                String tags = rs.getString("tags");
                String ingredients = rs.getString("ingredients");
                String location = rs.getString("location");
                Recipe recipe = new Recipe(id, name, tags, ingredients, location);
                recipes.add(recipe);
            }
        }

        return recipes;
    }

}
