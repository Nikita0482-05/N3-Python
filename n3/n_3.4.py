class Car:
    
    vehicle_type = "Легковой автомобиль"
    fuel_type = "Бензин"

    def __init__(self, brand: str, model: str, year: int, color: str, engine_volume: float, mileage: int) -> None:
        
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.engine_volume = engine_volume  
        self.mileage = mileage  
        self.is_running = False

    def __str__(self) -> str:
        return f"{self.brand} {self.model} {self.year} года, {self.color}"

    def start_engine(self) -> str:
        
        if not self.is_running:
            self.is_running = True
            return f"Двигатель {self.brand} {self.model} запущен"
        return "Двигатель уже работает"

    def stop_engine(self) -> str:
        
        if self.is_running:
            self.is_running = False
            return f"Двигатель {self.brand} {self.model} остановлен"
        return "Двигатель уже выключен"

    def get_age(self, current_year: int) -> int:
        
        return current_year - self.year

    def is_high_mileage(self) -> bool:
        
        return self.mileage > 100000

    def repaint(self, new_color: str) -> None:
        
        self.color = new_color
        print(f"Автомобиль перекрашен в {new_color}")

    @classmethod
    def change_fuel_type(cls, new_fuel_type: str) -> None:
    
        cls.fuel_type = new_fuel_type



car1 = Car("Toyota", "Camry", 2018, "Серебристый", 2.5, 75000)
car2 = Car("BMW", "X5", 2020, "Чёрный", 3.0, 45000)
car3 = Car("Lada", "Vesta", 2022, "Белый", 1.6, 15000)


print(car1)  
print(car2.start_engine())  
print(car1.get_age(2024))  
print(car3.is_high_mileage())  


car2.repaint("Синий")  
Car.change_fuel_type("Дизель")
print(f"Новый тип топлива: {Car.fuel_type}")  


print(car2.stop_engine())  
print(car2.stop_engine())  