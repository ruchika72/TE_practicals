import java.util.*;

class Node {
    int val;
    Node left = null, right = null;
    
    Node(int val) {
        this.val = val;
    }
    
    Node(int val, Node left, Node right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}



public class Main {
    public static void dfs(Node root) {
        // when to stop
        if (root == null) return;
        // what to do
        dfs(root.left);
        System.out.print(root.val + " ");
        dfs(root.right);
    }
    
    public static void main(String args[]) {
        // Scanner sc = new Scanner(System.in);
        // int n = sc.nextInt();
        Node one = new Node(1), three = new Node(3), root = new Node(2, one, three);
        // two is root;
        dfs(root);
    }
}