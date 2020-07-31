class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int p_idx, y_idx, p_cnt=0, y_cnt=0;
        
        s = s.toLowerCase();
        
        p_idx = s.indexOf('p');
        y_idx = s.indexOf('y');
        if (p_idx == -1) {
            p_cnt = 0;
        }
        if (y_idx == -1) {
            y_cnt = 0;
        }
        
        while (p_idx != -1) {
            p_idx = s.indexOf('p', p_idx+1);
            p_cnt++;
        }
        while (y_idx != -1) {
            y_idx = s.indexOf('y', y_idx+1);
            y_cnt++;
        }
        
        if (p_cnt != y_cnt) {
            answer = false;
        }
        
        return answer;
    }
}