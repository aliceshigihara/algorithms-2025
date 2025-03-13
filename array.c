#include <stdio.h>

int main()
{
    int numbers[10];
    for (int i=0; i <=9; i++) {
        printf("Digite um número: ");
        int n;
        scanf("%d", &n);

        numbers[i] = n;
    }

for (int i=0; i <=9; i++) {
    printf("vetor[%d] = %d\n", i, numbers[i]);
}

    return 0;
}