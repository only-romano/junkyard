#include <stdio.h>
#include <stdlib.h>

void createPointer1();
int * createPointer2();
void createPointer3();
int *pt = NULL;

int main(void)
{
    createPointer1();
    createPointer1();
    createPointer1();
    printf("\n");

    int *ptr;
    ptr = createPointer2();
    ptr = createPointer2();
    ptr = createPointer2();
    free(ptr);
    printf("\n");

    int n = 1;
    pt = malloc(n * sizeof(int));
    *pt = 1;
    createPointer3();
    createPointer3();
    createPointer3();
    free(pt);
    printf("\n");

    return 0;
}

void createPointer1()
{
    int *p = NULL;
    int n = 1;
    if (p == NULL)
    {
        p = malloc(n * sizeof(int));
        *p = 1;
    }
    printf("%d \t", *p);
    (*p)++;
    free(p);
}

int * createPointer2()
{
    static int *p = NULL;
    int n = 1;
    if (p == NULL)
    {
        p = malloc(n * sizeof(int));
        *p = 1;
    }
    printf("%d \t", *p);
    (*p)++;
    return p;
}

void createPointer3()
{
    printf("%d \t", *pt);
    (*pt)++;
}
