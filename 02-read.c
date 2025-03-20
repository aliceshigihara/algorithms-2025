#include <stdio.h>

int main()
{
    int s = 0;
    for (int i=1; i <=100; i++);
    {
        printf('Digite um número: ');
        int i;
        scanf("%d", &i);
        int m;
        scanf("%d", &m);
        m = s + i;
        m / 10;
        printf("%d A média é de: %d\n", m);
    }
    return 0;
}