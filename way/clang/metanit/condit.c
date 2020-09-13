#include <stdio.h>

int main(void)
{
    int x, y;
    printf("Input number: ");
    scanf("%d", &x);
    if (x > 10)
        printf("If statement!\nx (%d) is greater than 10!\n", x);
    else if (x < 10)
        printf("Else if statement!\nx (%d) is less than 10!\n", x);
    else
        printf("Else statement!\nx (%d) is equal 10!\n", x);

    switch(x)
    {
        case 1:
            printf("\nSwitch statement\nx = 1\n");
            break;
        case 10:
            printf("\nSwitch statement\nx = 10\n");
            break;
        case 100:
            printf("\nSwitch statement\nx = 100\n");
            break;
        default:
            printf("\nSwitch statement\nx is undefined\n");
            break;
    }

    printf("\nInput second number: ");
    scanf("%d", &y);
    char op = '+';

    int z = op == '+' ? (x + y) : (x - y);
    printf("x + y = %d\n", z);

    return 0;
}
