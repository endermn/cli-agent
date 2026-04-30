from sqlalchemy.orm import Session
from .interfaces import Tool
from termini.database.config.database_manager import database_manager
from termini.database.models.todo_tasks import Tasks
import logging

from termini.services.logger import terminiLogger

logger: logging.Logger = terminiLogger(name=__name__, file="termini.log").get_logger()


class ToDoTool(Tool):
    """A simple to-do list tool."""

    @property
    def name(self) -> str:
        return "ToDoTool"

    @property
    def description(self) -> str:
        return "A tool to manage a to-do list. You can add, view, and remove tasks."

    def __init__(self):
        self.todo_list = []
        self.engine = database_manager.engine 

    def add_task(self, task_description: str) -> str:
        logger.info(f"Tool called - Adding task: {task_description}")
        try:
            with Session(self.engine) as session:
                new_task = Tasks(task_description=task_description)
                session.add(new_task)
                session.commit()
            return f'Task "{task_description}" added to your to-do list.'
        except Exception as e:
            print("Error: Adding todo task failed. For more information please check termini.log")
            logger.error(f"Failed to add todo task: {e}")

            return None

    def view_tasks(self) -> str:
        logger.info("Tool call - 'view_tasks' called")
        try:
            with Session(self.engine) as session:
                tasks_list = session.query(Tasks).all()
                if not tasks_list:
                    return "To-do list currently empty."
                tasks = "\n".join(
                    f"{task.id}. {task.task_description}" for task in tasks_list
                )
            return f"Current To-do list:\n{tasks}"
        except Exception as e:
            print("Error: Viewing todo list failed. For more information please check termini.log")
            logger.error(f"Failed to view todo list: {e}")
            return None

    def remove_task(self, task_number: int) -> str | None:
        logger.info(f"Tool call - Removing task: {task_number}")
        try:
            with Session(self.engine) as session:
                task = session.query(Tasks).filter(Tasks.id == task_number).first()
                if task:
                    session.delete(task)
                    session.commit()
                    return f"Task {task_number} removed from the current To-do list."
                else:
                    logger.debug(f"Invalid task number: {task_number}")
                    print("Please mention a valid task number to remove.")
                    return None
        except Exception as e:
            print("Error: Removing To-do task failed. For more information please check termini.log")
            logger.error(f"Failed to remove todo task: {e}")
            return None

    def clear_tasks(self) -> str | None:
        logger.info("Tool call - Clearing all tasks")
        try:
            with Session(self.engine) as session:
                num_deleted = session.query(Tasks).delete()
                session.commit()
                return f"All tasks cleared from the to-do list. ({num_deleted} tasks removed)"
        except Exception as e:
            print("Error: Clearing To-do tasks failed. For more information please check termini.log")
            logger.error(f"Failed to clear todo tasks: {e}")
            return None
