import sys
from typing import Annotated, get_type_hints

from fastapi import APIRouter, status, Depends

from dependecy import get_task_service,  get_tasks_repository, get_tasks_cache_repository
from repository import TaskRepository
from schema.task import TaskSchema
from service.task import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@router.get("/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    print(commons)
    return commons

@router.get("/all",response_model=list[TaskSchema] | None)
async def get_tasks(
        task_service: Annotated[TaskService, Depends(get_task_service)],
    ):
    return task_service.get_tasks()


@router.post("/", response_model=TaskSchema, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskSchema,
                      task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]):
    task_id = task_repository.create_task(task)
    task.id = task_id
    return task

@router.patch("/{task_id}",
              response_model=TaskSchema,
              status_code=status.HTTP_200_OK)
async def patch_task(task_id: int,
                     name: str,
                     task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]):
    return task_repository.update_task_name(task_id, name)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int,
                      task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]):
    task_repository.delete_task(task_id)
    return {"message": "Task deleted"}

