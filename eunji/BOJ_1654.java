import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ_1654 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str[] = br.readLine().split(" ");
		
		int K = Integer.parseInt(str[0]);
		int N = Integer.parseInt(str[1]);
		int[] arr = new int[K];
		
		for(int i=0;i<K;i++) {
			arr[i]=Integer.parseInt(br.readLine());
		}
		
		Arrays.sort(arr);
		
		int cnt=0;
		long l=1, r=arr[K-1];
		while(l<=r) {
			long mid = (l+r)/2;
			cnt=0;
			for(int i=0;i<K;i++) {
				cnt+=arr[i]/mid;
			}
			if(cnt<N) r=mid-1;
			else l=mid+1;
		}
		
		System.out.print(r);
	}
}
