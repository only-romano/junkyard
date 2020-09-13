#include <stdio.h>

float total = 0.0;
short count = 0;
short tax_percent = 6;

float add_with_tax(float f)
{
    float tax_rate = 1 + tax_percent / 100.0;
    total = total + (f * tax_rate);
    count++;
    return total;
}

int main(void)
{
    float val;
    printf("Cost of product: ");
    while (scanf("%f", &val) == 1)
    {
        printf("Final cost: %.2f\n", add_with_tax(val));
        printf("Cost of serve: ");
    }

    printf("\nFinal cost: %.2f\n", total);
    printf("Number of serves: %hi\n", count);

    return 0;
}
