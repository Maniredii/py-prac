class car:
    wheels = 4
    engine = 'petrol'
    base_speed = '60kmph'
    max_speed = '150kmph'

tata = car()
#calling with object 
print(tata.wheels)
print(tata.engine)
print(tata.base_speed)
print(tata.max_speed)

# calling with class 
# print(car)

# print(car.wheels)
# print(car.engine)
# print(car.base_speed)
# print(car.max_speed)


# data objects 

class car:
    def __init__(qspiders, wheelers, engine, base_speed, max_speed):
        qspiders.wheelers = wheelers
        qspiders.engine = engine
        qspiders.base_speed = base_speed
        qspiders.max_speed = max_speed
tata = car(4, 'petrol', '60kmph', '150kmph')

print(tata)
print(tata.wheelers)
print(tata.engine)
print(tata.base_speed)
print(tata.max_speed)