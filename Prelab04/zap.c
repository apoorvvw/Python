#include<stdio.h>
int main() {
    int * a = malloc(sizeof(int));
    a[0] = 2;
    int i;
    for ( i = 0; i< 20 ; i++) {
        printf("%d",a[i]);
    }
    free(a);
    return 0;
}
