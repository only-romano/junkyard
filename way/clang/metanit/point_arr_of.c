#include <stdio.h>

void example();
void strings();
void pointers();

int main(void)
{
    example();
    strings();
    pointers();
    return 0;
}

void example()
{
    int a[] = {1, 2, 3, 4};
    int *p1[3];
    int *p2[] = { &a[1], &a[2], &a[0] };
    int *p3[3] = { &a[3], &a[1], &a[2] };
}

void strings()
{
    char hello[] = "Hello World";
    char *hell = "Hello World!";
    printf("%s\n%s\n\n", hello, hell);

    char *fruit[] = { "apricot", "apple", "banana", "lemon", "pear", "plum" };
    int n = sizeof(fruit) / sizeof(fruit[0]);

    for (int i = 0; i < n; i++)
    {
        printf("%s\n", fruit[i]);
    }
    printf("\n");
}

void pointers()
{
    int x = 22;
    int *ptr1;
    int **ptr2;
    ptr1 = &x;
    ptr2 = &ptr1;

    printf("Address o ptr1: %p\nAddress of x: %p\nValue of x: %d\n", ptr2, *ptr2, **ptr2);
}
