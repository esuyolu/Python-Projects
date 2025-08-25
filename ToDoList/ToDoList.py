import json
import os


class ToDoList:
    def __init__(self):
        self.tasks = []
        self.read_from_file()

    def read_from_file(self):
        try:
            if os.path.exists("tasks.json"):
                with open("tasks.json", "r") as file:
                    self.tasks = json.load(file)
        except Exception as e:
            print(f"Dosya okuma hatası: {e}")

    def write_to_file(self):
        try:
            with open("tasks.json", "w") as file:
                json.dump(self.tasks, file, indent=2)
        except Exception as e:
            print(f"Dosya yazma hatası: {e}")

    def add_to_list(self, task_description, priority="normal"):
        task = {
            "id": len(self.tasks) + 1,
            "description": task_description,
            "priority": priority,
            "completed": False,
            "category": "genel"
        }
        self.tasks.append(task)
        self.write_to_file()
        print(f"✓ {task_description} görevi eklendi!")

    def delete_from_list(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                self.write_to_file()
                print(f"✗ '{task['description']}' görevi silindi!")
                return
            print("Görev bulunamadı!")

    def show_list(self, filter_type="all"):
        if not self.tasks:
            print("Henüz görev yok!")
            return

        filtered_tasks = self.tasks

        if filter_type == "completed":
            filtered_tasks = [task for task in self.tasks if task["completed"]]
        elif filter_type == "pending":
            filtered_tasks = [task for task in self.tasks if not task["completed"]]

        print("\n" + "=" * 50)
        print("TO-DO LİSTESİ")
        print("=" * 50)

        for task in filtered_tasks:
            status = "✓" if task["completed"] else "✗"
            print(f"{task['id']:2d}. {status} {task['description']} "
                  f"[{task['priority']}] - {task['category']}")

    def mark_as_done(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.write_to_file()
                print(f"✓ '{task['description']}' görevi tamamlandı!")
                return
            print("Görev bulunamadı!")

    def mark_as_undone(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = False
                self.write_to_file()
                print(f"✗ '{task['description']}' görevi tamamlanmadı olarak işaretlendi!")
                return
            print("Görev bulunamadı!")

    def clear_completed(self):
        completed_count = sum(1 for task in self.tasks if task["completed"])
        self.tasks = [task for task in self.tasks if not task["completed"]]
        self.write_to_file()
        print(f"{completed_count} tamamlanmış görev temizlendi!")

    def update_task(self, task_id, new_description=None, new_priority=None, new_category=None):
        for task in self.tasks:
            if task["id"] == task_id:
                if new_description:
                    task["description"] = new_description
                if new_priority:
                    task["priority"] = new_priority
                if new_category:
                    task["category"] = new_category

                self.write_to_file()
                print(f"✓ Görev güncellendi!")
                return
            print("Görev bulunamadı!")


# menu
def main():
    todo = ToDoList()

    while True:
        print("\n" + "=" * 50)
        print("TO-DO LIST UYGULAMASI")
        print("=" * 50)
        print("1. Görev Ekle")
        print("2. Görevleri Listele")
        print("3. Görev Tamamla")
        print("4. Görev Geri Al")
        print("5. Görev Sil")
        print("6. Tamamlananları Temizle")
        print("7. Sadece Tamamlananları Göster")
        print("8. Sadece Bekleyenleri Göster")
        print("9. Çıkış")
        print("=" * 50)

        choice = input("Seçiminiz (1-9): ")

        if choice == '1':
            description = input("Görev açıklaması: ")
            priority = input("Öncelik (high/medium/low) [normal]: ") or "normal"
            todo.add_to_list(description, priority)

        elif choice == '2':
            todo.show_list()

        elif choice == '3':
            todo.show_list("pending")
            try:
                task_id = int(input("Tamamlanacak görev ID: "))
                todo.mark_as_done(task_id)
            except ValueError:
                print("Geçersiz ID!")

        elif choice == '4':
            todo.show_list("completed")
            try:
                task_id = int(input("Geri alınacak görev ID: "))
                todo.mark_as_undone(task_id)
            except ValueError:
                print("Geçersiz ID!")

        elif choice == '5':
            todo.show_list()
            try:
                task_id = int(input("Silinecek görev ID: "))
                todo.delete_from_list(task_id)
            except ValueError:
                print("Geçersiz ID!")

        elif choice == '6':
            todo.clear_completed()

        elif choice == '7':
            todo.show_list("completed")

        elif choice == '8':
            todo.show_list("pending")

        elif choice == '9':
            print("Güle güle!")
            break

        else:
            print("Geçersiz seçim!")


if __name__ == "__main__":
    main()
