# You are given a collection of product IDs. Some IDs may appear more than once.
# Write a function that returns True if any duplicates are found, and False otherwise.

def has_duplicates(product_ids):
    seen = set()
    for pid in product_ids:
        if pid in seen:
            return True
        seen.add(pid)
    return False

# Justification:
# A set is used because it provides O(1) average-time membership checks and insertions.
# This lets us detect duplicates efficiently. Runtime is O(n) time and O(n) space in the worst case.


# You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.

from collections import deque

class TaskQueue:
    def __init__(self):
        self.queue = deque()

    def add_task(self, task):
        self.queue.append(task)

    def remove_oldest_task(self):
        if self.queue:
            return self.queue.popleft()
        return None

# Justification:
# A deque (double-ended queue) supports O(1) appends and O(1) pops from the front.
# This makes it the best choice for queue-like behavior compared to a list, which would take O(n) for front removals.


# You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

class UniqueTracker:
    def __init__(self):
        self.seen = set()

    def add(self, value):
        self.seen.add(value)

    def get_unique_count(self):
        return len(self.seen)

# Justification:
# A set automatically enforces uniqueness and allows O(1) average-time insertions.
# Each add operation is constant time, and the count of unique values can be retrieved in O(1).


# Tests
if __name__ == "__main__":
    # Problem 1 tests
    print(has_duplicates([10, 20, 30, 20, 40]))  # True
    print(has_duplicates([1, 2, 3, 4, 5]))       # False

    # Problem 2 tests
    tq = TaskQueue()
    tq.add_task("Email follow-up")
    tq.add_task("Code review")
    print(tq.remove_oldest_task())  # "Email follow-up"
    print(tq.remove_oldest_task())  # "Code review"
    print(tq.remove_oldest_task())  # None

    # Problem 3 tests
    tracker = UniqueTracker()
    tracker.add(10)
    tracker.add(20)
    tracker.add(10)
    print(tracker.get_unique_count())  # 2