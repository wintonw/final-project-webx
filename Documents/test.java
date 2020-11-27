
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

public class test {

    public static void main(String[] args) {
        ArrayList<String> FOOD = new ArrayList<String>();
        ArrayList<String> DESC = new ArrayList<String>();
        ArrayList<String> PRICE = new ArrayList<String>();
        BufferedReader br = null;
        BufferedReader br2 = null;
        BufferedReader br3 = null;
        try {
            File file = new File("FOOD.txt"); // java.io.File
            File file2 = new File("DESCRIPTIONS.txt");
            File file3 = new File("PRICE.txt");
            FileReader fr = new FileReader(file); // java.io.FileReader
            FileReader fr2 = new FileReader(file2);
            FileReader fr3 = new FileReader(file3);
            br = new BufferedReader(fr); // java.io.BufferedReader
            br2 = new BufferedReader(fr2);
            br3 = new BufferedReader(fr3);
            String line;
            while ((line = br.readLine()) != null) {
                FOOD.add(line);
            }
            while ((line = br2.readLine()) != null) {
                DESC.add(line);
            }
            while ((line = br3.readLine()) != null) {
                PRICE.add(line);
            }
            for (int i = 0; i < FOOD.size(); i++) {
                System.out.println("<p> <p class = \"price\">" + PRICE.get(i) + "</p>" + FOOD.get(i) + "</p>");
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (br != null)
                    br.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
            try {
                if (br2 != null)
                    br2.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
            try {
                if (br3 != null)
                    br3.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}