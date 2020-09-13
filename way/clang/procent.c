#include <stdio.h>
#include <math.h>


int timeCycle(int a, int b, int c)
{
    int i = 0;
    float r = a;
    float p = 1 + (float)c / 100;
    while (r < b)
    {
        r *= p;
        i++;
    }
    return i;
}

int timeRecursion(float a, int b, int c, int d)
{
    a *= 1 + (float)c/100;
    d++;
    if (a < b)
        return timeRecursion(a, b, c, d);
    return d;
}

int timeFormula(int a, int b, int c)
{
    double d = a;
    double e = b;
    double f = c;
    double r = log(e/d) / log(1+f/100);
    return ceilf(r);
}

int main(void)
{
    int a, b, c;
    printf("Deposit: ");
    scanf("%d", &a);
    printf("Result: ");
    scanf("%d", &b);
    printf("Interest: ");
    scanf("%d", &c);
    //printf("Result: %d", timeCycle(a,b,c));
    //printf("Result: %d", timeRecursion((float)a,b,c,0));
    printf("Result: %d", timeFormula(a,b,c));
    return 0;
}
