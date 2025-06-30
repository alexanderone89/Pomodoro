from dataclasses import dataclass

from exception import TaskNotFound
from repository import TaskRepository, TaskCache
from schema.task import TaskSchema, TaskCreateSchema


# dataclass - декоратор позволяет не писать __init__
# а просто объявить атрибуты task_repository и task_cache
@dataclass
class TaskService:
    # def __init__(self,
    #              task_repository: TaskRepository,
    #              task_cache: TaskCache):
    #     self.task_repository = task_repository
    #     self.task_cache = task_cache

    task_repository: TaskRepository
    task_cache: TaskCache


    def get_tasks(self)-> list[TaskSchema]:
        # тонарный оператор :=
        if tasks := self.task_cache.get_tasks():
            return tasks
        else:
            tasks = self.task_repository.get_tasks()
            # Преобразование данных базы в данные pydantic
            tasks_schema = [TaskSchema.model_validate(task) for task in tasks]
            self.task_cache.set_tasks(tasks_schema)
            return tasks_schema

    def create_task(self, body: TaskCreateSchema, user_id: int) -> TaskSchema:
        task_id = self.task_repository.create_task(body, user_id)
        task = self.task_repository.get_task(task_id)
        return TaskSchema.model_validate(task)

    def update_task_name(self, task_id: int, name: str, user_id: int)-> TaskSchema:
        task = self.task_repository.get_user_task(user_id=user_id, task_id=task_id)
        if not task:
            raise TaskNotFound
        task = self.task_repository.update_task_name(task_id=task_id, name=name)
        return TaskSchema.model_validate(task)

    def delete_task(self, task_id: int,  user_id: int)->None:
        task = self.task_repository.get_user_task(user_id=user_id, task_id=task_id)
        if not task:
            raise TaskNotFound
        self.task_repository.delete_task(task_id=task_id, user_id=user_id)
