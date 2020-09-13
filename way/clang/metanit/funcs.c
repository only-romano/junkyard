#include <stdio.h>

void hello();
long long int factorial(int n);
double exchange(double currate, double sum);
void add(int *Array, int c);
int fibonachi(int n);
void display();

int main(void)
{
    int a;
    long long int b;
    double c, d, e;
    int f[2];
    int l[2];
    int g, h, k;
    hello();
    printf("Input number: ");
    scanf("%d", &a);
    b = factorial(a);
    printf("Factorial of %d is %d\n", a, b);
    hello();
    printf("Input currate: ");
    scanf("%lf", &c);
    printf("Input sum: ");
    scanf("%lf", &d);
    e = exchange(c, d);
    printf("Exchanged value is %.2f\n", e);
    hello();
    printf("Input number 1: ");
    scanf("%d", &l[0]);
    printf("Input number 2: ");
    scanf("%d", &l[1]);
    printf("Input number to add: ");
    scanf("%d", &k);
    add(l, k);
    printf("New values: number1 = %d; number2 = %d\n", l[0], l[1]);
    hello();
    printf("Input fibonachi number: ");
    scanf("%d", &g);
    h = fibonachi(g);
    printf("%d'th fibonachi number is %d\n", g, h);
    hello();
    display();
    display();
    display();
    hello();
    return 0;
}

void hello()
{
    printf("Hello\n");
}

long long int factorial(int n)
{
    long long int result = 1;
    for (int i = 2; i <= n; i++)
        result *= i;
    return result;
}

double exchange(double currate, double sum)
{
    double result = sum / currate;
    return result;
}

void add(int *Array, int c)
{
    Array[0] += c;
    Array[1] += c;
}

int fibonachi(int n)
{
    if (n == 0)
    {
        return 0;
    }
    if (n == 1)
    {
        return 1;
    }
    else
    {
        return fibonachi(n - 1) + fibonachi(n - 2);
    }
}

void display()
{
    static int i = 0;
    i++;
    printf("Static i = %d\n", i);
}
