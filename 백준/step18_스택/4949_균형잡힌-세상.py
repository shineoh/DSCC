# boj 4949_균형잡힌 세상 풀이



while True:
    stack = []
    sentence = input()
    for s in sentence:
        if s == '[':
            stack.append(s)
        if s == '{':
            stack.append(s)
        if s == '(':
            stack.append(s)
        if s == ']':

