#include <stdio.h>

void recall(int n)
{
    if (n == 1)
    {
        printf("%d end", n);
        return;
    }
    printf("%d\n", n);
    return recall(n - 1);
}

int factorial(int n)
{
    if (n == 0)
    {
        return 1;
    }
    else
    {
        return n * factorial(n - 1);
    }
}

int main()
{
    recall(3);
    printf("\n");

    printf("%d", factorial(4));
    return 0;
}
