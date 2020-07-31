#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
bool solution(const char* s) {
    bool answer=true;
    char *str=s;
    char temp[8];
    int s_to_int=atoi(str), slen=strlen(s);
    
    sprintf(temp, "%d", s_to_int);
    
    if(s_to_int==0 || strlen(temp)!=slen) {
        answer = false;
    }
    else if(slen != 4 && slen != 6) {
        answer = false;
    }
    
    return answer;
}