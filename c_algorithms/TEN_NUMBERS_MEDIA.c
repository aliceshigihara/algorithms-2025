#include <stdio.h>

int main()
{
    int s = 0;
    int n;
    for (int i = 1; i <= 10; i++)
    {
        printf("Digite um número: ");
        scanf("%d", &n);
        s = s + n;
    }
    int m = s / 10;

    printf("A média é de:%d\n", m);

    return 0;
}
