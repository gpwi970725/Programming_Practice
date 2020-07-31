class Solution {
  public String solution(int a, int b) {
      String[] weeks = {"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};
      int[] months = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
      int sum=b;
      
      for(int i=0; i<a-1; i++) {
          sum = sum + months[i];
      }
      
      return weeks[(sum-1)%7];
  }
}