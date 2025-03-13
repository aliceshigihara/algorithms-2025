#include <stdio.h>

int main()

{
    printf("insira um número: \n");
    int a;
    scanf("%d",&a);
    printf ("insira um segundo número: \n");
    int b;
    scanf ("%d",&b);
    
    if(a < b) {
        printf("%d %d \n",a,b);
    } else {
        printf("%d %d \n",b,a);
    }

    return 0;
}