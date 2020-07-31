#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int a, int b) {
    // 리턴할 값은 메모리를 동적 할당해주세요.
    char* answer = (char*)malloc(sizeof(char));
    char* weeks[7] = {"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};
    int monthDate[12] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int dateSum=b, i;
    
    for(i=0; i<a-1; i++) {
        dateSum = dateSum + monthDate[i];
    }
    
    answer = weeks[(dateSum-1)%7];
    
    return answer;
}