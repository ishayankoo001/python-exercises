
def es57(grid):
    N = []
    S = []
    E = []
    W = []
    if checkgrid(grid):
        N = countSky(grid, 'c',  1)
        S = countSky(grid, 'c', -1)
        E = countSky(grid, 'r', -1)
        W = countSky(grid, 'r',  1)
    return N, E, S, W


def countSky(grid, scan, d):
    res = []
    l = len(grid)
    if scan == 'r':
        for r in range(l):
            count = 0
            M = 0
            if d > 0:
                for c in range(l):
                    if grid[r][c] > M:
                        count += 1
                        M = grid[r][c]
            else:
                for c in range(l-1, -1, -1):
                    if grid[r][c] > M:
                        count += 1
                        M = grid[r][c]
            res.append(count)
    else:
        for c in range(l):
            count = 0
            M = 0
            if d > 0:
                for r in range(l):
                    if grid[r][c] > M:
                        count += 1
                        M = grid[r][c]
            else:
                for r in range(l - 1, -1, -1):
                    if grid[r][c] > M:
                        count += 1
                        M = grid[r][c]
            res.append(count)
    return res


def checkgrid(grid):
    l = len(grid)
    allowed = range(1, l+1)
    for r in grid:
        if len(set(r)) != l:
            return False
    for c in range(l):
        nums = set()
        for r in range(l):
            if not grid[r][c] in allowed:
                return False
            nums.add(grid[r][c])
        if len(nums) != l:
            return False
    return True
