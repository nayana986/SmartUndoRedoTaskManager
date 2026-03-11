class TaskNode:
    def __init__(self, task_id, name):
        self.task_id = task_id
        self.name = name
        self.next = None


class TaskList:

    def __init__(self):
        self.head = None

    def add_task(self, task_id, name):

        new_task = TaskNode(task_id, name)

        if self.head is None:
            self.head = new_task
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_task


    def display_tasks(self):

        temp = self.head

        if temp is None:
            print("No tasks")
            return

        while temp:
            print(temp.task_id, "-", temp.name)
            temp = temp.next


    def delete_task(self, task_id):

        temp = self.head
        prev = None

        while temp:

            if temp.task_id == task_id:

                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next

                return temp.name

            prev = temp
            temp = temp.next

        return None


class UndoStack:

    def __init__(self):
        self.stack = []

    def push(self, action):
        self.stack.append(action)

    def pop(self):

        if not self.stack:
            return None

        return self.stack.pop()


def undo(task_list, undo_stack):

    action = undo_stack.pop()

    if action is None:
        print("Nothing to undo")
        return

    operation, task_id, task_name = action

    if operation == "add":
        task_list.delete_task(task_id)
        print("Undo: task removed")

    elif operation == "delete":
        task_list.add_task(task_id, task_name)
        print("Undo: task restored")


task_list = TaskList()
undo_stack = UndoStack()

task_id = 1

while True:

    print("\n1 Add Task")
    print("2 Delete Task")
    print("3 Display Tasks")
    print("4 Undo")
    print("5 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        name = input("Enter task name: ")
        task_list.add_task(task_id, name)

        undo_stack.push(("add", task_id, name))

        task_id += 1


    elif choice == 2:

        tid = int(input("Enter task id: "))

        name = task_list.delete_task(tid)

        if name:
            undo_stack.push(("delete", tid, name))
            print("Task deleted")
        else:
            print("Task not found")


    elif choice == 3:
        task_list.display_tasks()


    elif choice == 4:
        undo(task_list, undo_stack)


    elif choice == 5:
        break