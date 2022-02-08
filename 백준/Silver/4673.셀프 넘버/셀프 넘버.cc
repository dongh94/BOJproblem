#include <stdio.h>

int num(int n)
{
	int d = n;
	while(n > 0)
	{
		d += n % 10;
		n /= 10;
	}
	return d;
 }
int main(void)
{
	int arr[10001], i, j;
	
	for(i = 1;i < 10001;i++)
	{
		j = num(i);
		if(j < 10001)
		{
			arr[j] = 1;
		}
	}
	for(i = 1;i < 10001;i++)
	{
		if(arr[i] != 1)
		{
			printf("%d\n", i);
		}
	}	
	return 0;
} 