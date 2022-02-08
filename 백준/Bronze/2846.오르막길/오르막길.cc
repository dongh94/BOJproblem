#include <stdio.h>

int main(void)
{
	int n;
	int pi[1001];
	int max = 0;
	int high = 0;
	int i;
	scanf("%d", &n);
	
	for (i = 0; i < n; i++)
	{
		scanf("%d", &pi[i]);
	}
	
	for (i = 0; i < n; i++)
	{
		if (pi[i] < pi[i + 1])
		{
			high = high + (pi[i + 1] - pi[i]);
		}
		else
		{
			if (max < high)
			{
				max = high;
			}
			high = 0;
		}
	}
	printf("%d", max);
	
	return 0;
}