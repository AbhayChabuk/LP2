def solveQueenBB(mat, row, n, colSet, diag1Set, diag2Set):
    if row == n:
        for r in mat:
            print(r)
        print()
        return True  # Return True if you want to stop after first solution

    for col in range(n):
        if col in colSet or (row - col) in diag1Set or (row + col) in diag2Set:
            continue  # Bounded: skip this branch

        # Place queen
        mat[row][col] = 1
        colSet.add(col)
        diag1Set.add(row - col)
        diag2Set.add(row + col)

        if solveQueenBB(mat, row + 1, n, colSet, diag1Set, diag2Set):
            return True  # Return True if only one solution needed

        # Backtrack
        mat[row][col] = 0
        colSet.remove(col)
        diag1Set.remove(row - col)
        diag2Set.remove(row + col)

    return False


if __name__ == '__main__':
    n = 4
    mat = [[0 for _ in range(n)] for _ in range(n)]
    solveQueenBB(mat, 0, n, set(), set(), set())
