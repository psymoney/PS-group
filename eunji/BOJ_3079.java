import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ_3079 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
		String str[] = br.readLine().split(" ");
		long N = Long.parseLong(str[0]);
		long M = Long.parseLong(str[1]);
		
		long arr[]= new long[(int)N];
		for(int i=0;i<N;i++) {
			arr[i]=Long.parseLong(br.readLine());
		}
		
		Arrays.sort(arr);
		
		long min = 1;
		long max = arr[(int)N-1]*M;
		long mid = (min+max)/2;
		long cnt = 0;
		long ans = mid;
		while(min<=max) {
			cnt = 0;
			mid = (min+max)/2;
			
			for(int i=0;i<N;i++) {
				cnt+=(mid/arr[i]);
			}
			if(cnt>=M) {
				ans = Math.min(ans,mid);
				max=mid-1;
			}
			else min=mid+1;
		}
		
		System.out.print(ans);
	}
}
