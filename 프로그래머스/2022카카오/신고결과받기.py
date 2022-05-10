
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2


def solution(id_list, report, k):

    # to_lst = [0] * len(id_list)
    # from_lst = list([''] for _ in range(len(id_list)))
    # for name in report:
    #     a, b = name.split()
    #     to_lst[b] += 1
    #     from_lst[b].append(a)
    #
    # for name in report:
    #     a, b = name.split()
    #     if to_lst[b] >= k:
    #         for id in range(len(id_list)):
    #             answer.append(len(from_lst[id]))
    answer = [0] * len(id_list)
    report = set(report)

    reports = {x: 0 for x in id_list}

    for r in report:
        reports[r.split()[1]] += 1

    for r in report:
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

ans = solution(id_list, report, k)
print(ans)