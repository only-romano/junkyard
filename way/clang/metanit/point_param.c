#include <stdio.h>

void incrementOld(int x);
void increment(int *x);
void swap(int *a, int *b);
void twiceOld(int n, int p[]);
void twice(int n, int *p);

int main(void)
{
    // increment
    int n = 10;
    incrementOld(n);
    printf("Main function: %d\n", n);
    increment(&n);
    printf("Main function: %d\n\n", n);

    // swap
    int x = 100;
    int y = 200;
    printf("x = %d \t y = %d\n", x, y);
    swap(&x, &y);
    printf("x = %d \t y = %d (swaped)\n\n", x, y);

    // twice 1
    int nums[] = {1, 2, 3, 4, 5};
    int length = sizeof(nums) / sizeof(nums[0]);

    twiceOld(length, nums);

    for (int i = 0; i < length; i++)
    {
        printf("%d \t", nums[i]);
    }
    printf("\n");

    // twice 2
    twice(length, nums);

    for (int i = 0; i < length; i++)
    {
        printf("%d \t", nums[i]);
    }

    return 0;
}

void incrementOld(int x)
{
    x++;
    printf("increment function: %d\n", x);
}

void increment(int *x)
{
    (*x)++;
    printf("increment function (pointers): %d\n", *x);
}

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void twiceOld(int n, int p[])
{
    for (int i = 0; i < n; i++)
    {
        p[i] *= 2;
    }
}

void twice(int n, int *p)
{
    for (int i = 0; i < n; i++)
    {
        *p++ *= 2;
    }
}
