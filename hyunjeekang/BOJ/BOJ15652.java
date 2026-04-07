import java.io.*;
import java.util.*;

public class BOJ15652 {

    static int N;
    static int M;
    static int[] comb;
    static StringBuilder sb = new StringBuilder();


    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        comb = new int[M];
        
        dfs(0, 1);
        System.out.println(sb);
    }

    private static void dfs(int depth, int start){
        if(depth == M){

            for(int j = 1; j < M; j++){
                if(comb[j-1] > comb[j]) return;
            }

            for(int k = 0; k < M; k++){
                sb.append(comb[k]).append(" ");
            }
            sb.append("\n");
            
            return;
        }
        for(int i = start ; i < N+1 ; i++){
            comb[depth] = i;
            dfs(depth+1, start);
        }
    }
}
