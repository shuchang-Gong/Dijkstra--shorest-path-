import math
import sys

def main():    
    while(True):
        nmList = sys.stdin.readline().split()
        n = int(nmList[0])
        m = int(nmList[1])
        if n == 0:
            break
        cost_map = dict.fromkeys([num for num in range(n)], None)
        for i in range(n):
            cost_map[(n-1) - i] = [int(num) for num in sys.stdin.readline().split()]
        result = min_cost(n, m, cost_map)
        print(result)

def NotInMap(x, y, n, m):
    if x >= 0 and x < n and y >= 0 and y < m:
        return False
    else:
        return True

def min_cost(n, m, cost_map):
    result_map = [math.inf] * m * n
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    dy = [1, 1, 1, 0, -1, -1, -1, 0]
    visited = 0
    result_map[0] = cost_map.get(0)[0]
    while result_map[-1] == math.inf:
        pos_cost= min(result_map)
        pos = result_map.index(pos_cost) 
        row = pos // m
        col = pos % m
        visited += (1 << pos)
        for i in range(8):
            if NotInMap(row + dx[i], col + dy[i], n, m):
                continue
            cost = pos_cost + cost_map.get(row + dx[i])[col + dy[i]]
            current = (row + dx[i])* m + col + dy[i]
            if (not ((visited >> current) & 1)) and cost < result_map[current]:
                result_map[current] = cost
        result_map[pos] = math.inf
    return result_map[-1]

main()