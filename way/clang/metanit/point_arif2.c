#include <stdio.h>
#include <stdlib.h>

int compare(const void* left, const void* right)
{
    return (*(int*)right - *(int*)left);
}

void f1(int var)
{
    printf("This is f1 and var is: %d\n", var);
}

void f2(int var)
{
    printf("This is f2 and var is: %d\n", var);
}

void f3(int var)
{
    printf("This is f3 and var is: %d\n", var);
}


int main(void)
{
    int intArray[5] = { 10, 20, 30, 40, 50 };

    for (int i = 0; i < 5; i++)
    {
        printf("intArray[%d] has value %d - and address @ %x\n",
            i, intArray[i], &intArray[i]);
    }

    int *intPointer = &intArray[3];
    printf("adress: %x - has value %d\n", intPointer, *intPointer);
    intPointer++;
    printf("adress: %x - has value %d\n", intPointer, *intPointer);
    intPointer--;
    printf("adress: %x - has value %d\n", intPointer, *intPointer);

    int (*cmp) (const void*, const void*);
    cmp = &compare;

    int iarray[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    qsort(iarray, sizeof(iarray) / sizeof(*iarray), sizeof(*iarray), cmp);

    int c = 0;
    while (c < sizeof(iarray) / sizeof(*iarray))
    {
        printf("%d \t", iarray[c]);
        c++;
    }

    void (*funcs[]) (int) = { *f1, *f2, *f3 };
    for (int i = 0; i < 3; i++)
        funcs[i](i);

    return 0;
}
