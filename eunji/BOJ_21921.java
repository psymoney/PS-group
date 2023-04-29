import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_21921 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str[] = br.readLine().split(" ");
		int N = Integer.parseInt(str[0]);
		int X = Integer.parseInt(str[1]);
		
		int [] arr = new int [N];
		String str2[] = br.readLine().split(" ");
		for(int i = 0; i < N; i++) {
			arr[i] =  Integer.parseInt(str2[i]);
		}
		
	
		int sum = 0;
		for(int i=0;i<X;i++) {
			sum+=arr[i];
		}
		
		int max = sum;
		int cnt = 1;
 		for(int j=X;j<N;j++) {
 			sum += arr[j] - arr[j-X];
 			
 			if(max<sum) {
 				max=sum;
 				cnt=1;
 			}else if(max==sum) {
 				cnt++;
 			}
 			
 		}
		
 		if(max!=0) {
 			 System.out.println(max);
 			 System.out.println(cnt);
 		}else {
 			 System.out.println("SAD");
 		}
 		
	}

}
