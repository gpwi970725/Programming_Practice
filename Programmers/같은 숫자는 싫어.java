import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Queue<Integer> q = new LinkedList<Integer>();
        
        q.offer(arr[0]);
        for (int i=1; i<arr.length; i++) {
            if (arr[i] != arr[i-1]) {
                q.offer(arr[i]);
            }
        }
        
        int len=q.size(), idx=0;
        int[] answer = new int[len];
        
        while (!q.isEmpty()) {
            answer[idx] = q.poll();
            idx++;
        }

        return answer;
    }
}