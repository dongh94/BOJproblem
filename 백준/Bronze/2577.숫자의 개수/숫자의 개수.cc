#include <stdio.h>
int main()
{
	int a, b, c, i, j, d[15]={};
	scanf("%d %d %d", &a, &b, &c);
	int n=a*b*c;
	
	for(i=1;n>0;i++){
		for(j=0;j<10;j++){
			if(n%10==j) d[j]++;
		}
		n=n/10;
	}
	for(j=0;j<=9;j++){
		printf("%d\n", d[j]);
	}
}