package graph_traversal;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedList;

public class BOJ_2606 {
	public static int cnt = 0;
	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		LinkedList<Integer> list[] = new LinkedList[N+1];
		boolean visited[] = new boolean[N+1]; // 방문 여부 
		
		for (int i = 0; i <= N; i++) {
			list[i] = new LinkedList<Integer>();
		}

		
		for(int i=0;i<M;i++) {
			String str[] = br.readLine().split(" ");
			int v1 =  Integer.parseInt(str[0]);
			int v2 =  Integer.parseInt(str[1]);
			
			list[v1].add(v2);
			list[v2].add(v1);
		}
		
		// 방문 순서 정렬 
		for(int i=0;i<=N;i++) {
			Collections.sort(list[i]);
		}
		
		dfs(1,list,visited);
		
		System.out.print(cnt-1);
	}
	
	
	
	public static void dfs(int v,LinkedList<Integer> list[], boolean visited[]) {
		
		cnt++;
		visited[v]=true; // 방문 
		Iterator<Integer> iter = list[v].listIterator();
		
		while(iter.hasNext()) {
			int x = iter.next();
			if(!visited[x]) { // 방문하지 않았을 때 
				dfs(x,list,visited);
			}
		}
	}
}
