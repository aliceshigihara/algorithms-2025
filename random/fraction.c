#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
	int x;
	printf("quantos N termos você deseja?:");
	scanf("%d", &x);
	
	int n;
	int v;
	for (n = 0; n < x; n++) {
		v = (int)pow(2,n);
		printf("1/%d ", v);
	}

	return 0;

}