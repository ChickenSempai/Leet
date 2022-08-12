class Solution {
    public boolean isValidSudoku(char[][] board) {
        ArrayList<HashSet<Character>> vertical = new ArrayList<HashSet<Character>>(Collections.nCopies(9, new HashSet<Character>()));
        ArrayList<HashSet<Character>> horizontal = new ArrayList<HashSet<Character>>(Collections.nCopies(9, new HashSet<Character>()));
        ArrayList<HashSet<Character>> cubes = new ArrayList<HashSet<Character>>(Collections.nCopies(9, new HashSet<Character>()));
        for(int i=0; i < 9; i++){
            vertical.set(i, new HashSet());
            horizontal.set(i, new HashSet());
            cubes.set(i, new HashSet());
        }
        for(int i=0; i < 9; i++){
            for(int j=0; j<9; j++){
                if (board[i][j]!='.') {
                    if (vertical.get(i).contains(board[i][j])) {
                        return false;
                    }
                    if (horizontal.get(j).contains(board[i][j])) {
                        return false;
                    }
                    if (cubes.get((int) Math.floor(i / 3) * 3 + (int) Math.floor(j / 3)).contains(board[i][j])) {
                        return false;
                    }
                    vertical.get(i).add(board[i][j]);
                    horizontal.get(j).add(board[i][j]);
                    cubes.get((int) Math.floor(i / 3) * 3 + (int) Math.floor(j / 3)).add(board[i][j]);
                }
            }
        }
        return true;
    }
}