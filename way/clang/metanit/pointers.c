#include <stdio.h>

void showPointer();
void morePointers();
void addressOfPointer();
void comparePointers();
void conversePointers();

int main(void)
{
    showPointer();
    morePointers();
    addressOfPointer();
    comparePointers();
    conversePointers();
    return 0;
}

void showPointer()
{
    int x = 10;
    int *p;
    p = &x;
    printf("Address: %p\nx = %d\n\n", p, *p);
}

void morePointers()
{
    char c = 'N';
    int d = 10;
    short s = 2;

    char *pc = &c;
    int *pd = &d;
    short *ps = &s;

    printf("Variable c: Address = %p \t value = %c\n", pc, *pc);
    printf("Variable d: Address = %p \t value = %d\n", pd, *pd);
    printf("Variable s: Address = %p \t value = %hd\n\n", ps, *ps);
    pd = NULL;
}

void addressOfPointer()
{
    int a = 10;
    int *pa = &a;
    printf("address of pointer = %p\n", &pa);
    printf("address of stored in pointer = %p\n", pa);
    printf("value on pointer = %d\n\n", *pa);
}

void comparePointers()
{
    int a = 10;
    int b = 20;
    int *pa = &a;
    int *pb = &b;
    printf("pa (%p) is %s pb (%p)\n\n", pa, (pa > pb ? "greater than" : "less or equal"), pb);
}

void conversePointers()
{
    char c = 'N';
    char *pc = &c;
    int *pd = (int *)pc;
    printf("pc = %p\npd = %p\n\n", pc, pd);
}
