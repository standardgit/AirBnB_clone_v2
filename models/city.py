#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy.ext.declarative  import declarative_base
from sqlalchemy import Column, String, Integer, DATETIME
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship



class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
