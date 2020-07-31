import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> ansList = new ArrayList<>();
        
        Arrays.sort(arr);
        
        if (arr[arr.length - 1] >= divisor) {
            for (int num : arr) {
                if (num%divisor == 0) {
                    ansList.add(num);
                }
            }
        }
        
        if (ansList.isEmpty()) {
            ansList.add(-1);
        }
        
        int[] answer = new int[ansList.size()];
        int size=0;

        for(int temp : ansList) {
            answer[size++] = temp;
        }
        
        return answer;
    }
}