import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pawpal_system import Task, Pet, Owner, Scheduler


# --- Task tests ---

def test_task_completion():
    """Marking a task complete changes its status."""
    task = Task(name="Walk", time_of_day="08:00", duration=30, priority="high", category="walk")
    task.completed = True
    assert task.completed is True

def test_is_high_priority():
    """is_high_priority returns True only for high priority tasks."""
    high = Task(name="Meds", time_of_day="08:00", duration=5, priority="high", category="meds")
    low = Task(name="Grooming", time_of_day="10:00", duration=20, priority="low", category="grooming")
    assert high.is_high_priority() is True
    assert low.is_high_priority() is False


# --- Pet tests ---

def test_add_task_increases_count():
    """Adding a task to a pet increases its task count."""
    pet = Pet(name="Mochi", species="dog", breed="Shiba Inu", age=3, weight=10.5)
    assert len(pet.get_tasks()) == 0
    pet.add_task(Task(name="Walk", time_of_day="08:00", duration=30, priority="high", category="walk"))
    assert len(pet.get_tasks()) == 1


# --- Scheduler tests ---

def test_generate_plan_respects_time_limit():
    """Scheduler excludes tasks that exceed available time."""
    owner = Owner(name="Jordan", phone="555-1234", budget=100.0, time_available_minutes=30)
    pet = Pet(name="Mochi", species="dog", breed="Shiba Inu", age=3, weight=10.5)
    pet.add_task(Task(name="Walk", time_of_day="08:00", duration=30, priority="high", category="walk"))
    pet.add_task(Task(name="Grooming", time_of_day="09:00", duration=20, priority="low", category="grooming"))
    scheduler = Scheduler(owner=owner, pet=pet, date="2026-07-08")
    plan = scheduler.generate_plan()
    assert len(plan) == 1
    assert plan[0].name == "Walk"

def test_generate_plan_orders_by_priority():
    """Scheduler puts high priority tasks before low priority ones."""
    owner = Owner(name="Jordan", phone="555-1234", budget=100.0, time_available_minutes=120)
    pet = Pet(name="Luna", species="cat", breed="Tabby", age=2, weight=4.2)
    pet.add_task(Task(name="Playtime", time_of_day="11:00", duration=15, priority="low", category="enrichment"))
    pet.add_task(Task(name="Medication", time_of_day="08:30", duration=5, priority="high", category="meds"))
    scheduler = Scheduler(owner=owner, pet=pet, date="2026-07-08")
    plan = scheduler.generate_plan()
    assert plan[0].name == "Medication"

def test_empty_tasks_returns_no_plan():
    """Scheduler returns empty plan when pet has no tasks."""
    owner = Owner(name="Jordan", phone="555-1234", budget=100.0, time_available_minutes=120)
    pet = Pet(name="Mochi", species="dog", breed="Shiba Inu", age=3, weight=10.5)
    scheduler = Scheduler(owner=owner, pet=pet, date="2026-07-08")
    plan = scheduler.generate_plan()
    assert plan == []