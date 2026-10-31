from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class CarType(Base):
    __tablename__ = "car_types"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

    cars = relationship("Car", back_populates="car_type")

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    car_code = Column(String(10), unique=True, nullable=False)
    rental_price = Column(Float, nullable=False)
    car_type_id = Column(Integer, ForeignKey("car_types.id"))

    car_type = relationship("CarType", back_populates="cars")
