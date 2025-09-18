import heapq
from typing import List

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # Maps taskId -> userId
        self.taskToUser = {}
        # Maps taskId -> current priority
        self.taskToPriority = {}
        # Heap to store all tasks as (-priority, -taskId)
        # Using negatives ensures Python's min-heap behaves like a max-heap.
        # Tie-breaking: larger taskId comes first if priorities are equal.
        self.topTask = []

        # Initialize with given tasks
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        """
        Add a new task for a user with the given priority.
        - taskId is guaranteed not to exist already.
        """
        self.taskToUser[taskId] = userId
        self.taskToPriority[taskId] = priority
        # Push into heap with negative values for max-heap behavior
        heapq.heappush(self.topTask, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        """
        Update the priority of an existing task.
        - Push the new value into the heap (old entry becomes stale).
        - Lazy deletion ensures we skip stale entries later.
        """
        self.taskToPriority[taskId] = newPriority
        heapq.heappush(self.topTask, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        """
        Remove a task from the system.
        - Only delete from dictionaries.
        - The heap may still contain stale entries for this task.
        - These stale entries will be ignored when popped in execTop.
        """
        if taskId in self.taskToUser:
            del self.taskToUser[taskId]
            del self.taskToPriority[taskId]

    def execTop(self) -> int:
        """
        Execute the task with the highest priority.
        - If multiple tasks have the same priority, pick the larger taskId.
        - Remove the executed task from the system and return its userId.
        - If no tasks exist, return -1.
        """
        if not self.taskToUser:
            return -1

        # Keep popping until we find a valid (non-stale) entry
        while self.topTask:
            priority, negTaskId = heapq.heappop(self.topTask)
            taskId = -negTaskId  # restore original taskId
            # Check if this entry is valid
            if taskId in self.taskToPriority and self.taskToPriority[taskId] == -priority:
                # Found the correct top task -> remove it from the system
                user = self.taskToUser.pop(taskId)
                self.taskToPriority.pop(taskId)
                return user

        # If heap is empty and no valid tasks are left
        return -1