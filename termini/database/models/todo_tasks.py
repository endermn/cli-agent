from sqlalchemy import Column, Integer, String
from .base import Base


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    task_description = Column(String, nullable=False,index=True)
