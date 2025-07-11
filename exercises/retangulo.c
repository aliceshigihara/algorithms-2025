#include <stdio.h>

int main() {
	
	int largura;
	printf("digite a largura: ");
	scanf("%d", &largura);
	
	int altura;
	printf("digite a altura: ");
	scanf("%d", &altura);
	
	
	printf("+");
	
	for (int contador = 1; contador < largura - 2; contador++) {
		printf("-");
	}
	
	printf("+\n");
	
	for (int linha = 1; linha < altura - 2; linha++) {
		printf("|");
		
		for (int space = 1; space < largura -2; space++) {
			printf(" ");
			
		}
		printf("|\n");
	}
	
	printf("+");
	
	for (int contador = 1; contador < largura - 2; contador++) {
		printf("-");
	}
	
	printf("+\n");
	
return 0;

}

