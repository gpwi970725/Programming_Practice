class Solution {
    public int[] solution(int[] prices) {
        int len = prices.length;
        int[] answer = new int[len];
        
        answer[len-1] = 0;
        for (int i=0; i<len-1; i++) {
            answer[i] = len-i-1;
            for (int j=i; j<len; j++) {
                if (prices[i] > prices[j]) {
                    answer[i] = j-i;
                    break;
                }
            }
        }
        
        return answer;
    }
}