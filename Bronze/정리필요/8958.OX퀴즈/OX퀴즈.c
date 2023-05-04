#include <stdio.h>
#include <string.h>

int ox_score(int numbering,char oxs[][80]);

int main(void)
{
    int n;
    scanf("%i", &n);

    char ox[n][80];

    for(int i =0; i < n; i++)
    {
        scanf("%s", ox[i]);
    }


    for(int i =0; i<n; i++)
    {
        printf("%i\n", ox_score(i, ox));
    }
}

int ox_score(int numbering,char oxs[][80])
{
    int score =0;
    int plus = 0;
    int j = 0;
    
    while(oxs[numbering][j] != '\0')
    {
        if(oxs[numbering][j] == 'O')
        {
            score += 1;
            score += plus;
            plus += 1;
        }

        else
        {
            plus = 0;
        }

        j+=1;
    }

    return score;
}