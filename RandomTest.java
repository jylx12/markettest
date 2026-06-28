// RandomTest.java

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Random;

class Product {
    private final String name;
    private final double price;
    private final int stock;

    public Product(String name, double price, int stock) {
        this.name = name;
        this.price = price;
        this.stock = stock;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public int getStock() {
        return stock;
    }

    @Override
    public String toString() {
        return String.format("%-12s $%.2f (%d in stock)", name, price, stock);
    }
}

public class RandomTest {

    public static void main(String[] args) {
        List<Product> products = generateProducts();

        System.out.println("=== Inventory Report ===");
        System.out.println("Generated: " + LocalDateTime.now());
        System.out.println();

        products.sort(Comparator.comparing(Product::getPrice));

        double totalValue = 0;

        for (Product product : products) {
            System.out.println(product);
            totalValue += product.getPrice() * product.getStock();
        }

        System.out.printf("%nTotal Inventory Value: $%.2f%n", totalValue);
    }

    private static List<Product> generateProducts() {
        String[] names = {
            "Keyboard",
            "Mouse",
            "Monitor",
            "Laptop",
            "Headphones",
            "Webcam"
        };

        Random random = new Random();
        List<Product> list = new ArrayList<>();

        for (String name : names) {
            double price = 25 + random.nextDouble() * 475;
            int stock = random.nextInt(50) + 1;
            list.add(new Product(name, price, stock));
        }

        return list;
    }
}
