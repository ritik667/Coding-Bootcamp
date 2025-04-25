from collections import deque
def find(tasks, time_slice):
    Q = deque()
    for task in tasks:
        Q.append(task)
    time = 0
    while Q:
        task = Q.popleft()
        if task > time_slice:
            time += time_slice
            Q.append(task-time_slice)
        else:
            time += task
            print(f"Task {task} finished at {time}")
    return time
tasks = [10,5,8]
time_slice = 4
print(find(tasks, time_slice))