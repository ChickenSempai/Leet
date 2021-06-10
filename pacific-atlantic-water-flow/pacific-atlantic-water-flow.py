class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return []
        rows, cols = len(matrix), len(matrix[0])
        dirs = [0, -1, 0, 1, 0]

        def flow_up(i, j, ocean_x, ocean_y, location_set):
            location_set.add((i, j))
            for d1, d2 in zip(dirs, dirs[1:]):
                ni, nj = i + d1, j + d2
                if (ni, nj) in location_set or not (rows > ni >= 0 <= nj < cols): continue
                if ocean_x in [ni+1, ni-1] or ocean_y in [nj+1, nj-1] or matrix[ni][nj] >= matrix[i][j]:
                    flow_up(ni, nj, ocean_x, ocean_y, location_set)
            return location_set

        pacific = flow_up(0, 0, -1, -1, set())
        atlantic = flow_up(rows-1, cols-1, rows, cols, set())

        return pacific & atlantic