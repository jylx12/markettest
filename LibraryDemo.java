// LibraryDemo.java

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

class Book {
    String title;
    String author;
    boolean checkedOut;

    Book(String title, String author) {
        this.title = title;
        this.author = author;
        this.checkedOut = false;
    }

    void checkOut() {
        checkedOut = true;
    }

    void returnBook() {
        checkedOut = false;
    }
}

public class LibraryDemo {
    public static void main(String[] args) {
        List<Book> books = new ArrayList<>();

        books.add(new Book("Clean Code", "Robert Martin"));
        books.add(new Book("Dune", "Frank Herbert"));
        books.add(new Book("The Hobbit", "J.R.R. Tolkien"));
        books.add(new Book("Atomic Habits", "James Clear"));

        Random random = new Random();

        for (Book book : books) {
            if (random.nextBoolean()) {
                book.checkOut();
            }
        }

        System.out.println("=== Library Status ===");

        for (Book book : books) {
            String status = book.checkedOut ? "Checked out" : "Available";
            System.out.println(book.title + " by " + book.author + " - " + status);
        }
    }
}
