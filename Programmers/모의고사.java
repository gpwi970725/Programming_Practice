class Solution {
    public int[] solution(int[] answers) {
        int[] answer1 = {1,2,3,4,5};
        int[] answer2 = {2,1,2,3,2,4,2,5};
        int[] answer3 = {3,3,1,1,2,2,4,4,5,5};
        int supoja1=0, supoja2=0, supoja3=0;
        int idx1=0, idx2=0, idx3=0;
        
        for(int i=0; i<answers.length; i++) {
            if(answers[i] == answer1[idx1]) {
                supoja1++;
            }
            if(answers[i] == answer2[idx2]) {
                supoja2++;
            }
            if(answers[i] == answer3[idx3]) {
                supoja3++;
            }
            idx1++;
            idx2++;
            idx3++;
            if(idx1 == 5) { idx1 = 0; }
            if(idx2 == 8) { idx2 = 0; }
            if(idx3 == 10) { idx3 = 0; }
        }
        
        int max = supoja1;
        if(max < supoja2) { max = supoja2; }
        if(max < supoja3) { max = supoja3; }
        
        int[] supoja = new int[3];
        int cnt = 0;
        if(max == supoja1) {
            supoja[cnt] = 1;
            cnt++;
        }
        if(max == supoja2) {
            supoja[cnt] = 2;
            cnt++;
        }
        if(max == supoja3) {
            supoja[cnt] = 3;
            cnt++;
        }
        
        int[] ans;
        if(cnt == 1) {
            ans = new int[cnt];
            ans[0] = supoja[0];
        }
        else if(cnt == 2) {
            ans = new int[cnt];
            ans[0] = supoja[0];
            ans[1] = supoja[1];
        }
        else {
            ans = new int[cnt];
            ans[0] = supoja[0];
            ans[1] = supoja[1];
            ans[2] = supoja[2];
        }
        
        return ans;
    }
}