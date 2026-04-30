from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Issues(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, index=True)
    issue_description = Column(String, nullable=False)
    
    solutions = relationship("Solutions", back_populates="issue")
