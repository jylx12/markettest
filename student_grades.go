// student_grades.go

package main

import (
	"fmt"
	"sort"
)

type Student struct {
	Name  string
	Grade float64
}

func averageGrade(students []Student) float64 {
	total := 0.0
	for _, student := range students {
		total += student.Grade
	}
	return total / float64(len(students))
}

func highestGrade(students []Student) Student {
	best := students[0]

	for _, student := range students {
		if student.Grade > best.Grade {
			best = student
		}
	}

	return best
}

func main() {
	students := []Student{
		{"Alice", 91.5},
		{"Bob", 84.2},
		{"Charlie", 96.8},
		{"Diana", 88.9},
		{"Ethan", 79.4},
	}

	sort.Slice(students, func(i, j int) bool {
		return students[i].Grade > students[j].Grade
	})

	fmt.Println("=== Student Grades ===")

	for _, student := range students {
		fmt.Printf("%-8s %.1f%%\n", student.Name, student.Grade)
	}

	best := highestGrade(students)

	fmt.Printf("\nAverage Grade: %.2f%%\n", averageGrade(students))
	fmt.Printf("Top Student: %s (%.1f%%)\n", best.Name, best.Grade)
}
