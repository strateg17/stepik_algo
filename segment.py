# Задача на программирование: покрыть отрезки точками

import sys

def fetch_input():
    segments = []
    n = int(sys.stdin.readline())
    for _ in range(n):
        segments.append(tuple([int(i) for i in sys.stdin.readline().strip().split()]))
    return segments

segments = fetch_input()
segments.sort(key=lambda x: x[1])

point = segments[0][1]
point_list = [point]

for seg in segments:
    if point >= seg[0]:
        pass
    else:
        point = seg[1]
        point_list.append(point)

print(len(point_list))
print(*point_list)
    
