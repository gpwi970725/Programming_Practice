from collections import deque

def solution(priorities, location):
    order = 1
    key = [i for i in range(len(priorities))]
    
    key_queue = deque(key)
    priorities_queue = deque(priorities)

    while key[location] in key_queue:
        
        if priorities_queue[0]==max(priorities_queue):
            if key_queue[0]==key[location]:
                return order
            else:
                priorities_queue.popleft()
                key_queue.popleft()
                order += 1
        else:
            priorities_queue.append(priorities_queue.popleft())
            key_queue.append(key_queue.popleft())            



priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities, location))
