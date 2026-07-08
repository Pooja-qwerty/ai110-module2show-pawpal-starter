# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```


## 🖥️ Sample Output

```
Daily plan for Mochi (Shiba Inu) on 2026-07-08:
  08:00 — Morning walk (30 min) [priority: high]
  08:30 — Feeding (10 min) [priority: high]
  08:40 — Grooming (20 min) [priority: low]

Total time used: 60 min
```

## 🧪 Testing PawPal+

```bash
python3 -m pytest tests/test_pawpal.py -v
```

Tests cover:
- Task completion and priority checking
- Adding tasks to a pet
- Scheduler respects time limits
- Scheduler orders by priority
- Empty task list returns no plan
- Sorting tasks chronologically
- Conflict detection (duplicate times)
- Recurring task creates new instance
- One-time task returns None on complete

Sample test output:

```
# Paste your pytest output here
====================================================================== test session starts ======================================================================
collected 11 items
tests/test_pawpal.py::test_task_completion PASSED
tests/test_pawpal.py::test_is_high_priority PASSED
tests/test_pawpal.py::test_add_task_increases_count PASSED
tests/test_pawpal.py::test_generate_plan_respects_time_limit PASSED
tests/test_pawpal.py::test_generate_plan_orders_by_priority PASSED
tests/test_pawpal.py::test_empty_tasks_returns_no_plan PASSED
tests/test_pawpal.py::test_sort_by_time PASSED
tests/test_pawpal.py::test_detect_conflicts_finds_duplicate_times PASSED
tests/test_pawpal.py::test_detect_no_conflicts PASSED
tests/test_pawpal.py::test_recurring_task_creates_new_instance PASSED
tests/test_pawpal.py::test_non_recurring_task_returns_none PASSED
11 passed in 0.02s
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | | e.g., by priority, duration |
| Filtering | | e.g., skip tasks if time runs out |
| Conflict handling | | e.g., overlapping time slots |
| Recurring tasks | | e.g., daily vs. weekly |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Sorts by time_of_day in HH:MM format |
| Filtering | `Scheduler.filter_tasks(completed=True/False)` | Filter by completion status |
| Conflict handling | `Scheduler.detect_conflicts()` | Warns if two tasks share the same time slot |
| Recurring tasks | `Task.mark_complete()` | Creates a new task for tomorrow if frequency is "daily" |