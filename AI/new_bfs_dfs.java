import java.util.*;

public class new_bfs_dfs {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int vertices = sc.nextInt(), edges = sc.nextInt();
    int graph[][] = new int[vertices][vertices];
    for (int e = 0; e < edges; e++) {
      int u = sc.nextInt(), v = sc.nextInt();
      graph[u][v] = 1;
      graph[v][u] = 1;
    }
    
    Traverse t = new Traverse();
    boolean visDfs[] = new boolean[vertices];
    t.dfs(graph, 0, visDfs);
    System.out.println();
    
    boolean visBfs[] = new boolean[vertices];
    t.bfs(graph, 0, visBfs); 
  }
}

class Traverse {
  void dfs(int graph[][], int currNode, boolean vis[]) {
      vis[currNode] = true;
      System.out.print(currNode + " ");
      for (int nextNode = 0; nextNode < graph.length; nextNode++) {
        if (graph[currNode][nextNode] == 1 && !vis[nextNode]) {
          dfs(graph, nextNode, vis);
        }
      }
      
      //System.out.println();
  }
  
  void bfs(int graph[][], int node, boolean vis[]) {
    Queue <Integer> q = new LinkedList <> ();
    q.add(node);
    vis[node] = true;
    
    while (!q.isEmpty()) {
      System.out.println(q);
      int size = q.size();
      for (int i = 0; i < size; i++) {
        int currNode = q.poll();
        for (int nextNode = 0; nextNode < graph.length; nextNode++) 
          if (graph[currNode][nextNode] == 1 && !vis[nextNode]) {
            vis[nextNode] = true;
            q.add(nextNode);
          }
      }
    }
  }
}