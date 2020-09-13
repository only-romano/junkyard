#include <stdio.h>

void incIntPointer();
void difPointers();
void minIntPointers();

int main(void)
{
    incIntPointer();
    difPointers();
    minIntPointers();
    return 0;
}

void incIntPointer()
{
    int n = 10;

    int *ptr = &n;
    printf("address = %p \t value = %d \n", ptr, *ptr);

    ptr++;
    printf("address = %p \t value = %d (incremented) \n", ptr, *ptr);

    ptr--;
    printf("address = %p \t value = %d \n", ptr, *ptr);
}

void difPointers()
{
    double d = 10.6;
    double *pd =  &d;
    printf("Pointer pd: address = %p\n", pd);
    pd++;
    printf("Pointer pd: address = %p (incremented)\n", pd);
    pd += 2;
    printf("Pointer pd: address = %p (+2)\n", pd);

    char c = 'N';
    char *pc = &c;
    printf("Pointer pc: address = %p\n", pc);
    pd++;
    printf("Pointer pc: address = %p (incremented)\n", pc);
    pc -= 3;
    printf("Pointer pc: address = %p (-3)\n", pc);
}

void minIntPointers()
{
    int a = 10;
    int b = 23;
    int *pa = &a;
    int *pb = &b;
    int c = pa - pb;

    printf("pa = %p\npb = %p\nc = %d\n\n", pa, pb, c);
    printf("b = *pa++\npa: address = %p \t value = %d\n", pa, *pa);
    b = *pa++;
    printf("b: value = %d \n", b);
    printf("pa: address = %p \t value = %d\n\n", pa, *pa);

    pa--;
    printf("b = (*pa)++\npa: address = %p \t value = %d\n", pa, *pa);
    b = (*pa)++;
    printf("b: value = %d \n", b);
    printf("pa: address = %p \t value = %d\n\n", pa, *pa);

    printf("b = (*pa)++\npa: address = %p \t value = %d\n", pa, *pa);
    b = ++*pa;
    printf("b: value = %d \n", b);
    printf("pa: address = %p \t value = %d\n\n", pa, *pa);

    printf("b = (*pa)++\npa: address = %p \t value = %d\n", pa, *pa);
    b = *++pa;
    printf("b: value = %d \n", b);
    printf("pa: address = %p \t value = %d\n\n", pa, *pa);
}
