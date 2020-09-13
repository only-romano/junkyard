#include <stdio.h>

int add(int x, int y)
{
    return x + y;
}

int subtract(int x, int y)
{
    return x - y;
}

int operation(int (*op)(int, int), int a, int b)
{
    return op(a, b);
}

int isEven(int x)
{
    return x % 2 == 0;
}

int isPositive(int x)
{
    return x > 0;
}

void action(int (*condition)(int), int numbers[], int n)
{
    for (int i = 0; i < n; i++)
    {
        if (condition(numbers[i]) != 0)
        {
            printf("%d \t", numbers[i]);
        }
    }
}

int action1(void)
{
    printf("Action 1");
    return 1;
}

int action2(void)
{
    printf("Action 2");
    return 2;
}

int action3(void)
{
    printf("Action 3");
    return 3;
}

int (*select(void)) (void)
{
    int choice;
    int (*actions[])() = { action1, action2, action3 };

    printf("Select action (1, 2, 3): ");
    scanf("%d", &choice);
    if (choice > 0 && choice < 4)
        return actions[choice-1];
    else
        return NULL;
}

int main(void)
{
    // First
    int a = 10;
    int b = 5;
    int result;
    result = operation(add, a, b);
    printf("result = %d\n", result);
    result = operation(subtract, a, b);
    printf("result = %d\n", result);
    printf("\n");

    // Second
    int nums[] = { -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5 };
    int n = sizeof(nums) / sizeof(nums[0]);
    printf("\nEven numbers: ");
    action(isEven, nums, n);
    printf("\nPositive numbers: ");
    action(isPositive, nums, n);
    printf("\n");

    // Third
    int (*action)(void);
    int actionNumber;

    while (1)
    {
        action = select();
        if (action == NULL)
            break;
        actionNumber = action();
        printf("\nselected action %d \n", actionNumber);
    }
    printf("End");

    return 0;
}
