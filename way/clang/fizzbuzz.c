#include <stdio.h>

void fizzBuzz(int i)
{
    if (i % 3 == 0)
        printf("Fizz");
    if (i % 5 == 0)
        printf("Buzz");
    if ((i % 3 != 0) && (i % 5 != 0))
        printf("%d", i);
    printf("\n");
}

int main(void)
{
    int i;
    printf("Input a number: ");
    scanf("%d", &i);
    fizzBuzz(i);
    return 0;
}
