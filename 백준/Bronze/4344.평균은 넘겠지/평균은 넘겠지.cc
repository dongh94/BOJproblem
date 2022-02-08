#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int choice, choice2;
	int student[1000] = { 0, };
	int j, k, cnt;

	scanf("%d", &choice);

	for (int i = 0; i < choice; i++)
	{
		cnt = 0;
		int sum = 0;
		double avg;
		scanf("%d", &choice2);
		for (j = 0; j < choice2; j++)
		{
			scanf("%d", student + j);
			sum += *(student + j);
		}
		avg = sum / (double)j;
		for (k = 0; k < choice2; k++)
		{
			if (avg < student[k])
				cnt++;
		}
		printf("%.3lf%%\n", cnt / (double)choice2 * 100);
		
	}
	return 0;
}