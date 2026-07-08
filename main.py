from pawpal_system import Task, Pet, Owner, Scheduler

# Create owner
owner = Owner(name="Jordan", phone="555-1234", budget=100.0, time_available_minutes=120)

# Create pets
mochi = Pet(name="Mochi", species="dog", breed="Shiba Inu", age=3, weight=10.5)
luna = Pet(name="Luna", species="cat", breed="Tabby", age=2, weight=4.2)

# Add tasks to Mochi
mochi.add_task(Task(name="Morning walk", time_of_day="08:00", duration=30, priority="high", category="walk"))
mochi.add_task(Task(name="Feeding", time_of_day="09:00", duration=10, priority="high", category="feeding"))
mochi.add_task(Task(name="Grooming", time_of_day="10:00", duration=20, priority="low", category="grooming"))

# Add tasks to Luna
luna.add_task(Task(name="Medication", time_of_day="08:30", duration=5, priority="high", category="meds"))
luna.add_task(Task(name="Playtime", time_of_day="11:00", duration=15, priority="medium", category="enrichment"))

# Add pets to owner
owner.add_pet(mochi)
owner.add_pet(luna)

# Run scheduler for Mochi
scheduler = Scheduler(owner=owner, pet=mochi, date="2026-07-08")
print(scheduler.explain_plan())