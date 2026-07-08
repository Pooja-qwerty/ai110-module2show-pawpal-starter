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
        """Return True if this task is high priority."""
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
        """Add a task to this pet's task list."""
        self.tasks.append(task)

    def get_tasks(self):
        """Return all tasks for this pet."""
        return self.tasks


class Owner:
    def __init__(self, name, phone, budget, time_available_minutes):
        self.name = name
        self.phone = phone
        self.budget = budget
        self.time_available_minutes = time_available_minutes
        self.pets = []

    def add_pet(self, pet):
        """Add a pet to this owner's pet list."""
        self.pets.append(pet)

    def get_pets(self):
        """Return all pets owned by this owner."""
        return self.pets


class Scheduler:
    def __init__(self, owner, pet, date):
        self.owner = owner
        self.pet = pet
        self.date = date
        self.scheduled_tasks = []
        self.total_time_used = 0

    def generate_plan(self):
        """Sort tasks by priority, fit as many as possible within available time."""
        priority_order = {"high": 0, "medium": 1, "low": 2}
        sorted_tasks = sorted(
            self.pet.get_tasks(),
            key=lambda t: priority_order.get(t.priority, 99)
        )
        plan = []
        time_used = 0
        for task in sorted_tasks:
            if time_used + task.duration <= self.owner.time_available_minutes:
                plan.append(task)
                time_used += task.duration
        self.scheduled_tasks = plan
        self.total_time_used = time_used
        return plan

    def explain_plan(self):
        """Return a human-readable daily schedule."""
        plan = self.generate_plan()
        if not plan:
            return "No tasks fit within the available time."
        lines = [f"Daily plan for {self.pet.name} ({self.pet.breed}) on {self.date}:"]
        time_cursor = 8 * 60  # start at 8:00 AM
        for task in plan:
            hour = time_cursor // 60
            minute = time_cursor % 60
            lines.append(
                f"  {hour:02d}:{minute:02d} — {task.name} "
                f"({task.duration} min) [priority: {task.priority}]"
            )
            time_cursor += task.duration
        lines.append(f"\nTotal time used: {self.total_time_used} min")
        return "\n".join(lines)