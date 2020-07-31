import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int startIdx = 0;
        int endIdx = 0;
        int order = 0;
        int[] answer = new int[commands.length];
        int cnt=0;
        
        for(int[] command : commands) {
            startIdx = command[0]-1;
            endIdx = command[1]-1;
            order = command[2]-1;
            int[] curArr = new int[endIdx-startIdx+1];
            int idx = 0;
            for(int i=startIdx; i<=endIdx; i++) {
                curArr[idx] = array[i];
                idx++;
            }
            Arrays.sort(curArr);
            answer[cnt] = curArr[order];
            cnt++;
        }
        
        return answer;
    }
}