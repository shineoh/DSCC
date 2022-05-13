    to_lst = [0] * len(id_list)
    from_lst = list([''] for _ in range(len(id_list)))
    for name in report:
        a, b = name.split()
        to_lst[b] += 1
        from_lst[b].append(a)
    
    for name in report:
        a, b = name.split()
        if to_lst[b] >= k:
            for id in range(len(id_list)):
                answer.append(len(from_lst[id]))