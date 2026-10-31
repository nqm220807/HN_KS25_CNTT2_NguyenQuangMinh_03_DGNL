from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/cars", response_model=schemas.BaseResponse)
def get_cars(db: Session = Depends(get_db)):
    cars = db.query(models.Car).all()
    data = [
        {
            "id": car.id,
            "car_code": car.car_code,
            "rental_price": car.rental_price,
            "car_type": {
                "id": car.car_type.id,
                "name": car.car_type.name
            } if car.car_type else None
        } for car in cars
    ]
    return schemas.BaseResponse(
        statusCode=200,
        message="Lấy danh sách xe thành công",
        data=data
    )

@app.post("/cars", response_model=schemas.BaseResponse)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    db_car = models.Car(
        car_code=car.car_code,
        rental_price=car.rental_price,
        car_type_id=car.car_type_id
    )
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    
    return schemas.BaseResponse(
        statusCode=201,
        message="Thêm xe thành công",
        data={"id": db_car.id, "car_code": db_car.car_code}
    )

@app.delete("/car-types/{id}", response_model=schemas.BaseResponse)
def delete_car_type(id: int, db: Session = Depends(get_db)):
    car_type = db.query(models.CarType).filter(models.CarType.id == id).first()
    
    if not car_type:
        return schemas.BaseResponse(
            statusCode=404,
            error="Not Found",
            message="Không tìm thấy loại xe"
        )
        
    if db.query(models.Car).filter(models.Car.car_type_id == id).first():
        return schemas.BaseResponse(
            statusCode=400,
            error="Bad Request",
            message="Không thể xóa do có xe thuộc loại này"
        )
        
    db.delete(car_type)
    db.commit()
    
    return schemas.BaseResponse(
        statusCode=200,
        message="Xóa loại xe thành công"
    )
