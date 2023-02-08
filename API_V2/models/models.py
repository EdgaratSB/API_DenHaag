from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class roles(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    roles_name = Column(String, unique=True)
    cases_name = relationship("cases", back_populates="roles")

class cases(Base):
    __tablename__ = "cases"
    id = Column(Integer, primary_key=True, index=True)
    roles_id = Column(Integer, ForeignKey("roles.id"))
    cases_name = Column(String)
    cases_identifier = Column(String)
    access_levels = relationship("access_levels", back_populates="cases")
    roles = relationship("roles", back_populates="cases_name")

class access_levels(Base):
    __tablename__ = "access_levels"
    id = Column(Integer, primary_key=True, index=True)
    access_levels_name = Column(String, unique=True)
    cases_id = Column(Integer, ForeignKey("cases.id"))
    cases = relationship("cases", back_populates="access_levels")


    
    
    