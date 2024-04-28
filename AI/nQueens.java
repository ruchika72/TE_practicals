import java.util.*;

public class Main {
    public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      int n = sc.nextInt();
      int board[][] = new int[n][n];
      
      boolean ans = nQueen(board, 0);
      
      // System.out.println(Arrays.toString(board));
      for (int i = 0; i < board.length; i++) {
        for (int j = 0; j < board.length; j++) 
          System.out.print(board[i][j] + " ");
        System.out.println();
      }
  }
  
  static boolean nQueen(int[][] board, int col) {
    // when to stop
    if (col == board.length) {
      return true;
    }
    // what to do
    for (int i = 0; i < board.length; i++) {
      if (isItSafe(board, i, col)) {
        board[i][col] = 1;
        if (nQueen(board, col + 1)) 
          return true;
        board[i][col] = 0;
      }
    }
    
    return false;
  }
  
  static boolean isItSafe(int[][] board, int row, int col) {
    int r = row, c = col;
    while (c >= 0) {
      if (board[r][c--] == 1) return false;
    }
    c = col;
    while (r >= 0 && c >= 0) {
      if (board[r--][c--] == 1) return false;
    }
    r = row; c = col;
    while (r < board.length && c >= 0) {
      if (board[r++][c--] == 1) return false;
    }
    return true;
  }
}

// for every col:
//   for every cell of that col: 
//     is it safe to place the queen:
//       place a queen in that cell and (continue the process with next col.....)
      
//       remove that queen

