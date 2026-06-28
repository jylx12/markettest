// random_test.cpp

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <random>

class Student {
public:
    Student(std::string name, int score)
        : name(name), score(score) {}

    std::string getName() const {
        return name;
    }

    int getScore() const {
        return score;
    }

private:
    std::string name;
    int score;
};

int main() {
    std::vector<std::string> names = {
        "Alice", "Bob", "Charlie", "Diana", "Ethan"
    };

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> scoreDist(60, 100);

    std::vector<Student> students;

    for (const auto& name : names) {
        students.emplace_back(name, scoreDist(gen));
    }

    std::sort(students.begin(), students.end(),
        [](const Student& a, const Student& b) {
            return a.getScore() > b.getScore();
        });

    std::cout << "=== Student Rankings ===\n\n";

    for (const auto& student : students) {
        std::cout << student.getName()
                  << " - Score: "
                  << student.getScore()
                  << '\n';
    }

    std::cout << "\nTop student: "
              << students.front().getName()
              << " (" << students.front().getScore() << ")\n";

    return 0;
}
