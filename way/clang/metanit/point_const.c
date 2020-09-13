#include <stdio.h>

int main(void)
{
    const int a = 10;
    const int *pa = &a;
    printf("\nconst int *pa = &a\n");
    printf("address = %p \t value = %d \n", pa, *pa);

    int b = 20;
    const int *pb = &b;
    printf("\nconst int *pb = &b\n");
    printf("address = %p \t value = %d \n", pb, *pb);
    b = 33;
    printf("b = 33\n");
    printf("address = %p \t value = %d \n", pb, *pb);
    // *pb = 35;

    pb = &a;
    printf("\npb = &a\n");
    printf("address = %p \t value = %d \n", pb, *pb);

    int c = 10;
    int *const pc = &c;
    printf("\nint *const pc = &c\n");
    printf("address = %p \t value = %d \n", pc, *pc);
    *pc = 22;
    printf("*pc = 22\n");
    printf("address = %p \t value = %d \n", pc, *pc);
    // pc = &b;

    int d = 10;
    const int *const pd = &d;
    printf("\nconst int *const pd = &d\n");
    printf("address = %p \t value = %d \n", pd, *pd);
    // *pd = 22;
    // pc = &b;

    return 0;
}
