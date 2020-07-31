#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int a, int b) {
    long long sum = 0;
    int i, temp;
    
    if(a>b) {
        temp = a;
        a = b;
        b = temp;
    }
    
    for(i=a; i<=b; i++) {
        sum = sum + i;
    }
    
    return sum;
}