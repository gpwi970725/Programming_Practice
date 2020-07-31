class Solution {
    public boolean solution(String s) {
        boolean answer = true;
        
        try {
            int a = Integer.parseInt(s);
        } catch(NumberFormatException e) {
            return false;
        }
        
        if(s.length()==4 || s.length()==6) {
            return true;
        } else {
            return false;    
        }
        
    }
}