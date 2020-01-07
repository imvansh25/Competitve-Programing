import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class CHFDORA {

	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);
		int t = scn.nextInt();
		while (t > 0) {
			int n = scn.nextInt();
			int m = scn.nextInt();
			int[][] arr = new int[n + 1][m + 1];
			for (int i = 1; i < n + 1; i++) {
				for (int j = 1; j < m + 1; j++) {
					arr[i][j] = scn.nextInt();
				}
			}
			HashMap<Integer, Integer> map = new HashMap<>();
			for (int i = 1; i <= Integer.min(n, m); i = i + 2) {
				if (i == 1) {
					map.put(1, n * m);
				} else {
					int ans= no_of_valid_pairs(arr, map, i);
					map.put(i, ans);
				}
			}
			int sum =0;
			for(int values:map.values()) {
				sum+=values;
			}
			System.out.println(sum);
			t--;
		}

	}

	private static int no_of_valid_pairs(int[][] arr,HashMap<Integer, Integer> map,int diff) {
		int ans=0;
		for(int i=1;i<=Integer.min(arr[0].length-1,arr.length-1);i++) {
			int[] row=new int[diff+1];
			int[] col = new int[diff+1];
			for(int j=1;j<=diff && j<=Integer.min(arr[0].length-1,arr.length-1);j++) {
				row[j]=arr[i][j];
				col[j]=arr[j][i];
			}
			if(ispalindrom(row)||ispalindrom(col)) {
				ans++;
			}
		}
		return ans;
		

		
	}

	private static boolean ispalindrom(int[] arr) {
		for (int i = 1; i < arr.length / 2 + 1; i++) {
			if (arr[i] != arr[arr.length - i - 1]) {
				return false;
			}
		}
		return true;
	}

}
