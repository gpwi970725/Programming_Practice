from collections import deque

def solution(participant, completion):
    """
    completion_q = deque(completion)
    
    while completion_q:
        participant.remove(completion_q.pop())
        
    return participant[0]
    """   
    
    participant.sort()
    completion.sort()
    participant_q = deque(participant)
    completion_q = deque(completion)
    
    for i in range(len(completion)):
        p = participant_q.popleft()
        if p != completion_q.popleft():
            return p
    
    return participant[-1]