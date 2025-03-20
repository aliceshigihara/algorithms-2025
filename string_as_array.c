#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <locale.h>

int main()
{

    char frase[100];
    strcpy(frase,"Olá tudo bem com você?");

    int tam = strlen(frase);

    char frase2[] = "Tudo certo";

    int tam2 = strlen(frase2);

    printf("tamfrase1=%d tamfrase2=%d\n", tam, tam2);

    for (int i=0; i < tam; i++){
        printf("%c ", frase[i]);

    }
    printf("\n");

    for (int i=0; i < tam2; i++){
        printf("%c ", frase2[i]);
    }

    printf("\n");

    frase[2] = 'a';
    frase[3] = ' ';
    frase[21] = 'e';
    frase[22] = ' ';

     for (int i=0; i < tam; i++){
        printf("%c ", frase[i]);

    }

    printf("\n");


    return 0;

}