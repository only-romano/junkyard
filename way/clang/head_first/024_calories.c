#include <stdio.h>
#include "includes/calories.h"

int main(void)
{
    display_calories(115.2, 11.3, 0.79);

    return 0;
}

void display_calories(float weight, float distance, float coeff)
{
    printf("Weight: %3.2f pounds\n", weight);
    printf("Distance: %3.2f miles\n", distance);
    printf("Calories: %4.2f cal\n", coeff * weight * distance);
}
