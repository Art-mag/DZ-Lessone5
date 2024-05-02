class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.completed = True
                print(f"Task '{description}' marked as completed.")
                return
        print(f"No task found with description '{description}'.")

    def display_tasks(self):
        print("Current tasks:")
        for task in self.tasks:
            if not task.completed:
                print(f"- {task.description} (Deadline: {task.deadline})")


# Пример использования
task_manager = TaskManager()

# Добавляем задачи
task_manager.add_task("Подготовить отчет", "2024-05-10")
task_manager.add_task("Проверить почту", "2024-05-05")
task_manager.add_task("Позвонить клиенту", "2024-05-07")

# Отмечаем выполненную задачу
task_manager.mark_task_completed("Проверить почту")

# Выводим текущие (не выполненные) задачи
task_manager.display_tasks()
