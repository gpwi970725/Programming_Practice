#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* s) {
    char* answer=(char*)malloc(sizeof(char));
    int slen=strlen(s), idx=0;
    
    if(slen%2 == 0) {
        idx = slen / 2 - 1;
        answer[0] = s[idx];
        answer[1] = s[idx+1];
        answer[2] = '\0';
    }
    else {
        idx = slen / 2;
        answer[0] = s[idx];
        answer[1] = '\0';
    }
    
    return answer;
}