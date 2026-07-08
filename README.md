# 🐾 PawPal+

A Streamlit app that helps a busy pet owner plan daily care tasks for their pet, using smart scheduling based on priority and time constraints.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

## ✨ Features

- Enter basic owner and pet info
- Add tasks with a title, duration, priority, and time of day
- Generate a daily schedule sorted by priority that fits within available time
- View tasks sorted chronologically
- Detect scheduling conflicts (two tasks at the same time)
- Automatic recurring task creation for daily tasks

## 🛠️ Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 -m streamlit run app.py
```

## 🖥️ Sample Output

```
Daily plan for Mochi (Shiba Inu) on 2026-07-08:
  08:00 — Morning walk (30 min) [priority: high]
  08:30 — Feeding (10 min) [priority: high]
  08:40 — Grooming (20 min) [priority: low]

Total time used: 60 min
```

## 📸 Demo Walkthrough

1. Launch the app with `python3 -m streamlit run app.py` — a browser window opens automatically.
2. Enter an owner name (e.g. "Jordan") and pet name (e.g. "Mochi") and select a species.
3. Add tasks using the form — give each task a title, duration, priority, and time of day (HH:MM format).
4. Click **Add task** to add it to the list. Repeat for as many tasks as you need.
5. Click **Generate schedule** to produce a daily plan sorted by priority that fits within 120 minutes.
6. View the sorted task list below the schedule to see tasks in chronological order.
7. Check the Conflict Check section — any two tasks sharing the same time slot will trigger a warning.

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Sorts by time_of_day in HH:MM format |
| Filtering | `Scheduler.filter_tasks(completed=True/False)` | Filter by completion status |
| Conflict handling | `Scheduler.detect_conflicts()` | Warns if two tasks share the same time slot |
| Recurring tasks | `Task.mark_complete()` | Creates a new task for tomorrow if frequency is "daily" |

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

```
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

⭐⭐⭐⭐⭐ Confidence: 5/5 — all core behaviors verified.