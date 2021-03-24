def zero_one_knapsack(cargo):
    capacity = 15
    pack = []

    for row in range(len(cargo) + 1):  # 최대 물건 개수
        pack.append([])
        for col in range(capacity + 1):  # 최대 수용 무게
            if row == 0 or col == 0:
                pack[row].append(0)
            elif cargo[row-1][1] <= col:  # 현재 물건의 무게가 최대 무게 이하
                pack[row].append(
                    max(
                        pack[row-1][col],
                        cargo[row-1][0] + pack[row-1][col - cargo[row-1][1]]
                    )
                )
            else:  # 현재 물건의 무게가 최대 무게 초과
                pack[row].append(pack[row-1][col])
        print(pack[row])

    return pack[-1][-1]


# cargo : [(물건의 값, 물건의 무게), ...] 형태의 정보
cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2)
]

print(zero_one_knapsack(cargo))