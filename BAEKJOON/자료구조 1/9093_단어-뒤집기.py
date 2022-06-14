import sys      # input()을 사용해도 통과지만 sys.stdin.readline()이 훨씬 빠름

n = int(sys.stdin.readline())

for _ in range(n):
    sentence = sys.stdin.readline().split()
    for i in range(len(sentence)):
        if i == len(sentence):
            print(sentence[i][::-1])
        else:
            print(sentence[i][::-1], end=' ')