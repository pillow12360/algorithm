#include <stdio.h>
#include <iostream>

int main(){
    
    char a[5];
    char *pa;
    // �����Ұ� char���� '' string���� ""

    a[0] = 'a';
    a[1] = 'b';
    a[2] = 'c';
    a[3] = 'd';
    a[4] = 'e';

    //printf("%s\n",a);

    pa = a;

    printf("%s",*pa);

    return 0;
}