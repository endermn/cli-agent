import sys
sys.path.append('.')
import logging
import pytest

from sqlalchemy import create_engine
from termini.tools.agent_tools.todo import ToDoTool
from termini.services.logger import terminiLogger
from termini.database.models.base import Base

logger: logging.Logger = terminiLogger(name=__name__, file="termini.log").get_logger()

@pytest.fixture
def todo_tool():
    """Provides a ToDoTool connected to an isolated in-memory test database."""
    test_engine = create_engine("sqlite:///:memory:")

    Base.metadata.create_all(test_engine)

    tool = ToDoTool()
    tool.engine = test_engine

    yield tool

    Base.metadata.drop_all(test_engine)

def test_todo_functionality(todo_tool):
    """Test the basic CRUD operations of the ToDoTool"""
    
    logger.info("Testing ToDoTool functionality...")
    
    logger.info("\n1. Adding tasks:")
    add_task = todo_tool.add_task("Complete the project")
    assert add_task != None
    logger.info(f"   Result: {add_task}")
    
    add_task2 = todo_tool.add_task("Write documentation")
    assert not add_task2 == None
    logger.info(f"   Result: {add_task2}")
    
    add_task3 = todo_tool.add_task("Run tests")
    assert add_task3 != None
    logger.info(f"   Result: {add_task3}")
    
    logger.info("\n2. Viewing tasks:")
    tasks = todo_tool.view_tasks()
    assert tasks != None
    logger.info(f"   {tasks}")
    print(tasks)
    
    logger.info("\n3. Removing task with ID 2:")
    remove_result = todo_tool.remove_task(2)
    assert remove_result != None
    logger.info(f"   Result: {remove_result}")
    
    logger.info("\n4. Viewing tasks after removal:")
    tasks_after_removal = todo_tool.view_tasks()
    assert tasks_after_removal != None
    logger.info(f"   {tasks_after_removal}")
    
    logger.info("\n5. Trying to remove non-existent task (ID 999):")
    invalid_remove = todo_tool.remove_task(999)
    assert invalid_remove == None
    logger.info(f"   Result: {invalid_remove}")
