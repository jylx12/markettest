// todo_list.rs

#[derive(Debug)]
struct Task {
    title: String,
    completed: bool,
}

impl Task {
    fn new(title: &str) -> Self {
        Self {
            title: title.to_string(),
            completed: false,
        }
    }

    fn complete(&mut self) {
        self.completed = true;
    }
}

fn print_tasks(tasks: &[Task]) {
    println!("=== Todo List ===");

    for (i, task) in tasks.iter().enumerate() {
        let status = if task.completed { "✓" } else { " " };
        println!("{}. [{}] {}", i + 1, status, task.title);
    }
}

fn main() {
    let mut tasks = vec![
        Task::new("Write documentation"),
        Task::new("Fix API bug"),
        Task::new("Review pull request"),
        Task::new("Deploy application"),
    ];

    tasks[1].complete();
    tasks[3].complete();

    print_tasks(&tasks);

    let completed = tasks.iter().filter(|t| t.completed).count();

    println!(
        "\nCompleted {} of {} tasks.",
        completed,
        tasks.len()
    );
}
