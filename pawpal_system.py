from dataclasses import dataclass, field


@dataclass
class Task:
    name: str
    time_of_day: str
    duration: int
    priority: str
    category: str
    cost: float = 0.0
    notes: str = ""
    completed: bool = False

    def is_high_priority(self):
        return self.priority == "high"


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    age: int
    weight: float
    dietary_restrictions: str = ""
    medical_conditions: list = field(default_factory=list)
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks


class Owner:
    def __init__(self, name, phone, budget, time_available_minutes):
        self.name = name
        self.phone = phone
        self.budget = budget
        self.time_available_minutes = time_available_minutes
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def get_pets(self):
        return self.pets


class Scheduler:
    def __init__(self, owner, pet, date):
        self.owner = owner
        self.pet = pet
        self.date = date
        self.scheduled_tasks = []
        self.total_time_used = 0

    def generate_plan(self):
        pass

    def explain_plan(self):
        pass
