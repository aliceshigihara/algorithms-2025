#include <stdio.h>

int main() {
	
	
	for (int x = 1; x < 10; x += 2) {
	
	int y;
	printf("digite um numero de 1 a 10: ");
	scanf("%d", &y);
	
	if (y == 5) {
		
		printf("parou!");
		break;
	
		}	
	
	printf("%d\n", x);
	
	}
	return 0;
}