import re

def clean_and_validate_cars(raw_cars):
    valid_cars = []
    for car in raw_cars:
        car['car_code'] = car['car_code'].strip().upper()
        if re.match(r'^C\d+$', car['car_code']):
            valid_cars.append(car)
    return valid_cars

def search_cars(cars, max_price, status=None):
    result = []
    for car in cars:
        if car['rental_price'] <= max_price:
            if status is None or car.get('status') == status:
                result.append(car)
    return result

def sort_cars_by_rental_price_desc(cars):
    n = len(cars)
    for i in range(n):
        for j in range(0, n - i - 1):
            if cars[j]['rental_price'] < cars[j + 1]['rental_price']:
                cars[j], cars[j + 1] = cars[j + 1], cars[j]
    return cars
