# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

My initial UML design included four classes: Owner, Pet, Task, and Scheduler. Owner holds the user's name, phone, budget, and available time in minutes, and can add or retrieve pets. Pet holds the animal's name, species, breed, age, weight, dietary restrictions, and medical conditions, and manages a list of Task objects. Task is a dataclass storing a task's name, time of day, duration, priority, category, cost, notes, completion status, and frequency. Scheduler takes an Owner and Pet, sorts tasks by priority, fits as many as possible into the owner's available time window, and generates a human-readable explanation of the plan.

**b. Design changes**

During implementation I added three new methods to Scheduler that weren't in the original UML: `sort_by_time()`, `filter_tasks()`, and `detect_conflicts()`. These felt necessary once I started testing the CLI demo — just generating a plan wasn't enough to make the app useful. I also added `frequency` and `mark_complete()` to Task to support recurring tasks, which wasn't in the initial design but came up naturally when thinking about daily walks and feedings.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers two constraints: task priority (high, medium, low) and the owner's total available time in minutes. Priority is the primary sort key so high-priority tasks like feeding and medication are always scheduled before lower-priority ones. Time is the hard cutoff — any task that would exceed the available window is skipped entirely.

**b. Tradeoffs**

The main tradeoff is that the scheduler uses a greedy approach: it fills the schedule from highest to lowest priority and stops when time runs out, without trying to rearrange tasks to fit more in. This means a single long high-priority task could crowd out several shorter medium-priority tasks that would have fit together. This is reasonable for a pet care context because missing a high-priority task like medication is always worse than missing a lower-priority enrichment activity.

---

## 3. AI Collaboration

**a. How you used AI**

I used Claude throughout this project for system design brainstorming, generating the UML class diagram in Mermaid.js, producing the initial class skeletons using Python dataclasses, implementing scheduling logic, generating tests, and wiring the UI. The most helpful prompts were specific ones that included context — for example, sharing the current state of `pawpal_system.py` before asking for new methods, rather than asking generically.

**b. Judgment and verification**

When Claude suggested storing the task list on the Scheduler itself rather than reading it from the Pet object, I didn't accept this because it meant the same tasks would need to be added in two places. I moved task ownership back onto Pet and had the Scheduler read from there. I also manually ran `python3 main.py` after every change to verify the output made sense before accepting any AI-suggested logic.

---

## 4. Testing and Verification

**a. What you tested**

I tested task completion status, priority checking, adding tasks to a pet, scheduler time limit enforcement, priority ordering, empty task lists, chronological sorting, conflict detection, recurring task creation, and one-time task behavior. These tests matter because the scheduling logic is the core of the app — if priority ordering or time filtering is wrong, the entire output is wrong.

**b. Confidence**

I am confident the scheduler works correctly for all cases covered by the 11 tests. Edge cases I would test next include: tasks with identical priority and different durations (does order stay stable?), a task with zero duration, available time set to zero, and malformed time strings like "5:00" instead of "05:00" causing sorting issues.

---

## 5. Reflection

**a. What went well**

I am most satisfied with the clean separation between the logic layer (`pawpal_system.py`) and the UI layer (`app.py`). Designing the classes first in UML before writing any code made the implementation straightforward — I always knew what each class was responsible for and where new logic should live.

**b. What you would improve**

If I had another iteration I would add a time input validator so users can't enter malformed times like "5:00" instead of "05:00", which causes sorting to break. I would also improve the scheduler to try fitting smaller tasks into gaps rather than stopping greedily at the first task that doesn't fit.

**c. Key takeaway**

The most important thing I learned is that designing the system on paper first saves a lot of rework during implementation. When I had a clear picture of which class owned which data, every implementation decision became obvious. AI is a strong partner for generating structure quickly, but the judgment calls about ownership, relationships, and tradeoffs still require a human to reason through carefully.