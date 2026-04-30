from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Solutions(Base):
    __tablename__ = "solutions"

    id = Column(Integer, primary_key=True, index=True)
    issue_id = Column(Integer, ForeignKey("issues.id"), nullable=False, index=True)
    solution_description = Column(String, nullable=False)

    issue = relationship("Issues", back_populates="solutions")
