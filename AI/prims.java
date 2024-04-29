import java.util.*;

public class prims {
  static int minKey(int key[], boolean vis[]) {
  	int min = (int)1e9, idx = -1;
  	for (int i = 0; i < key.length; i++) 
  		if (key[i] < min && vis[i] == false) {
  			min = key[i]; 
  			idx = i;
  		}
  	return idx;
  }
  
  static void printMST(int graph[][], int parent[]) {
  	for (int i = 0; i < graph.length; i++) {
  		System.out.println(parent[i] + " - " + i + " cost: " + graph[i][parent[i]]);
  	}
  }
  
  static void primMST(int graph[][]) {
  	int v = graph.length, key[] = new int[v], parent[] = new int[v];
  	boolean vis[] = new boolean[v];
  	for (int i = 0; i < v; i++) {
  		key[i] = (int)1e9;
  		vis[i] = false;
  	}
  
  	key[0] = 0;
  
  	for (int count = 0; count < v - 1; count++) {
  		int u = minKey(key, vis);
  		vis[u] = true;
  		for (int i = 0; i < v; i++) {
  			if (graph[u][i] != 0 && !vis[i] && graph[u][i] < key[i]) {
    			key[i] = graph[u][i];
    			parent[i] = u;
  			}
  		}
  	}
  	printMST(graph, parent);
  }
  
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int vertices = sc.nextInt(), edges = sc.nextInt();
    int graph[][] = new int[vertices][vertices];
    for (int e = 0; e < edges; e++) {
      int u = sc.nextInt(), v = sc.nextInt(), wt = sc.nextInt();
      graph[u][v] = wt;
      graph[v][u] = wt;
    }
    primMST(graph);
  }
}