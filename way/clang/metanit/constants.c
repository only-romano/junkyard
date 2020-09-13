#include <stdio.h>

int number = 12;
const float PI = 3.14;

int main(void)
{
    printf("Number = %d\n", number);
    number = 55;
    printf("Number = %d\n", number);
    number = -23;
    printf("Number = %d\n", number);
    printf("PI = %3.2f\n", PI);
    // PI = 12.3;
    return 0;
}
