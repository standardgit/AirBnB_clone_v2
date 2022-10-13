#!/usr/bin/python3
""" State Module for HBNB project """
from tkinter.tix import COLUMN
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, Integer, DATETIME
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128),)
