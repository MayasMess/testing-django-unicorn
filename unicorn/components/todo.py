from django_unicorn.components import UnicornView
from todo.models import Todo
from django.db.models import Q


class TodoView(UnicornView):
    task: str = ""
    num: int = 0
    is_filtred: bool = False
    filter: str = ""
    todos = Todo.objects.none()
    limit = 20

    def hydrate(self):
        if not self.is_filtred:
            self.todos = Todo.objects.all()[:self.limit]

    def load_more_tasks(self):
        self.limit += 20
        self.hydrate()

    def order_tasks(self):
        self.todos = self.todos.order_by('task')

    def filter_tasks(self):
        self.is_filtred = True if self.filter else False
        self.todos = self.todos.filter(Q(task__contains=self.filter))

    def add_todo(self):
        if self.task:
            todo = Todo(task=self.task)
            todo.save()

        self.task = ""

    def increment(self, multi: int):
        self.num += multi

    @staticmethod
    def delete_task(pk):
        todo = Todo.objects.get(id=pk)
        todo.delete()

    @staticmethod
    def populate_random_tasks(number_of_tasks: int):
        for x in range(number_of_tasks):
            random_task = f'Task number {x+1}'
            todo = Todo(task=random_task)
            todo.save()
