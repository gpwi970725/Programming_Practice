from collections import deque

def solution(board, moves):
    board = list(map(list, zip(*board)))
    moves_queue = deque(moves)
    basket = []
    board_no_zero = []
    answer = 0

    for idx in range(0, len(board)):
        board_no_zero.append(list(filter(lambda x: x!=0, board[idx])))
    board_no_zero_queue = list(map(deque, board_no_zero))

    while moves_queue:
        try:
            basket.append(board_no_zero_queue[moves_queue.popleft()-1].popleft())
        except IndexError:
            continue

        if len(basket)>1 and basket[-1]==basket[-2]:
            basket.pop()
            basket.pop()
            answer = answer + 2
    
    
    return answer



board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))
