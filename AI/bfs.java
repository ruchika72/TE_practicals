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
    public static void bfs(Node root) {
        if (root == null) return;
        Queue <Node> q = new LinkedList <> ();
        q.add(root);
        while (!q.isEmpty()) {
            // Get the num of nodes in curr level
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                Node curr = q.poll();
                System.out.print(curr.val + " ");
                if (curr.left != null) 
                    q.add(curr.left);
                if (curr.right != null) 
                    q.add(curr.right);
            }
            System.out.println();
        }
    }
    
    public static void main(String args[]) {
        // Scanner sc = new Scanner(System.in);
        // int n = sc.nextInt();
        Node four = new Node(4), five = new Node(5), six = new Node(6), seven = new Node(7);
        Node one = new Node(1, four, five), three = new Node(3, six, seven), root = new Node(2, one, three);
        // two is root;
        bfs(root);
    }
}