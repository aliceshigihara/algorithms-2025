#include <stdio.h>
#include <stdlib.h>

int BuscaBinariaRecursiva(int *vet, int chave, int inicio, int fim) {
    int meio;
    if (inicio <= fim) {
        meio = (inicio + fim) / 2;
        if (chave == vet[meio]) {
            return meio;
        } else {
            if (chave < vet[meio]) {
                return BuscaBinariaRecursiva(vet, chave, inicio, meio - 1);
            } else {
                return BuscaBinariaRecursiva(vet, chave, meio + 1, fim);
            }
        }
    }

    return -1;
}

int BuscaBinariaIterativa(int *vet, int chave, int fim) {
	int inicio = 0;
	int meio = (inicio + fim) / 2;
	
	while(inicio <= fim);
		if (chave == vet[meio]);
			return meio;
		else{
			if(chave < vet[meio]);
				fim = meio - 1;
			else
				inicio = meio + 1;
		}
	}
	return -1;

}


int main() {
    int vet[10] = {12, 16, 19, 25, 28, 30, 38, 45, 49, 52};
    int valor, op;

    do {
        printf("Digite um número: ");
        scanf("%d", &valor);
//        printf("\nResultado: %d\n", BuscaBinariaRecursiva(vet, valor, 0, 9));
		printf("\nResultado: %d\n", BuscaBinariaIterativa(vet, valor, 9));

        printf("Deseja buscar outro número? (1-Sim / 0-Não): ");
        scanf("%d", &op);
    } while (op != 0);

    return 0;
}
