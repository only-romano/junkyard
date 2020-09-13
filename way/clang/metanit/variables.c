#include <stdio.h>

void vars()
{
    unsigned char uch = 244;
    // same:
    char ch = 'a';
    signed char sch = 'f';
    printf("char: %c, unsigned char: %c, signed char: %c\n", ch, uch, sch);
    // same:
    short int sin = 500;
    short s = 499;
    signed short int ssin = 32700;
    signed short ss = -31000;
    // same:
    unsigned short int usin = 61000;
    unsigned short us = 111;
    // same:
    int i = 2150444444;
    signed int si = 2;
    signed sss = 5;
    long int li = 255555;
    long l = 2;
    signed long int sli = 5;
    signed long sl = 112;
    // same:
    unsigned int ui = 4293000000;
    unsigned u = 5;
    unsigned long int uli = 99;
    unsigned long ul = 11;
    // same:
    long long int lli = -922222222222222222;
    long long ll = 1122123;
    signed long long int slli = 15;
    signed long long sll = 12;
    // same:
    unsigned long long int ulli = 1844444444444444444;
    unsigned long long ull = 1254;

    float fl = 3.3e+38;
    double db = 1.6e-307;
    long double ldb = 1.2E+300;

    printf("Size of int: %d\n", sizeof(i));
    printf("Size of long long int: %d\n", sizeof(lli));
    printf("Size of float: %d\n", sizeof(fl));
    printf("Size of double: %d\n", sizeof(db));
    printf("Size of long double: %d\n", sizeof(ldb));
}

int main(void)
{
    vars();
    return 0;
}
