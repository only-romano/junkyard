#include <stdio.h>
#include <stdarg.h>

int sum(int n, ...)
{
    int result = 0;
    for(int *ptr = &n; n > 0; n--)
    {
        result += *(++ptr);
    }
    return result;
}

int sumNew(int n, ...)
{
    int result = 0;
    va_list factor;
    va_start(factor, n);
    for (int i = 0; i < n; i++)
    {
        result += va_arg(factor, int);
    }
    va_end(factor);
    return result;
}

void display(char* format, ...)
{
    int d;
    double f;
    va_list factor;
    va_start(factor, format);

    for (char *c = format; *c; c++)
    {
        if (*c != '%')
        {
            printf("%c", *c);
            continue;
        }
        switch(*++c)
        {
            case 'd':
                d = va_arg(factor, int);
                printf("%d", d);
                break;
            case 'f':
                f = va_arg(factor, double);
                printf("%.2lf", f);
                break;
            default:
                printf("%c", *c);
        }
    }
    va_end(factor);
}

int main(void)
{
    printf("%d\n", sum(4,1,2,3,4));
    printf("%d\n", sumNew(5,12,21,13,4,5));
    display("Age: %d \t Weight: %f\n", 24, 68.4);
    return 0;
}
