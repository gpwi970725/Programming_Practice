from collections import deque

def solution(skill, skill_trees):
    cnt = 0
    
    while skill_trees:
        isCan = True
        skill_q = deque(skill)
        skill_tree_q = deque(skill_trees[0])
        del skill_trees[0]

        while skill_tree_q and skill_q:
            now_skill = skill_tree_q.popleft()
            
            if now_skill in skill_q:                
                if now_skill==skill_q[0]:
                    skill_q.popleft()
                    continue
                else:
                    isCan = False
                    break
            else:
                continue

        if isCan:
            cnt += 1
        
    return cnt


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))



"""
Another answer

'''
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
'''
"""
