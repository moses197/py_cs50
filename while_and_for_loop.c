#include <stdio.h>


int main(void)
{
    int n=7, i,j=1;

    for (i=1; i<n; i++)
    {
        printf("%d\n", i);
        if (i == j)
        {
            printf("Null");
        }
        for(j=1; j<i; j++)
        {
            printf("%d ", j);
        }
        printf("\n");
        printf("---------------\n");
        
    }
}

/*
int main(void)
{
    int i=1, j; // here, i and j are set to int and 1 is assign to 1
    while(i <= 5) // while i is less than or equal to 5 then run the loop
    {
        j = 1; // int j is set to 1
        printf("%d", i);
        while(j<i) // if j is less than or equal to i then run the loop
        {
            printf("%d ",j); //  the the value of j
            j++; // increment j by 1
        }
        printf("\n"); // new line
        i++; // increment i bt 1
    }
    return 0;
}

*/