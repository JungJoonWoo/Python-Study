def solution(friends, gifts):
    answer = 0
    giveCount = [0 for _ in range(len(friends))]
    takeCount = [0 for _ in range(len(friends))]
    for i in gifts:
        give, take = i.split()
        for j in range(len(friends)):
            if give == friends[j]:
                giveCount[j] += 1
            if take == friends[j]:
                takeCount[j] += 1
    giveMax = giveCount.index(max(giveCount))
    print(giveCount)
    print(takeCount)

    return answer


friends = ["muzi", "ryan", "frodo", "neo"]
gifts = [
    "muzi frodo",
    "muzi frodo",
    "ryan muzi",
    "ryan muzi",
    "ryan muzi",
    "frodo muzi",
    "frodo ryan",
    "neo muzi",
]

print(solution(friends, gifts))
