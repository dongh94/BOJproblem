#include <stdio.h>

int main(void)
{
	int num, num2;
	int a, b, c, d;
	int count = 1;

	scanf("%d", &num);
	num2 = num;

	while (1)
	{
		a = num / 10;
		b = num % 10;
		c = (a + b) % 10;
		d = (b * 10) + c;
		num = d;
		
		if (num2 == d)
			break;
		count++;
	}
	printf("%d", count);

	return 0;
}
