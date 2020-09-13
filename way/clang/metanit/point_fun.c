#include <stdio.h>

void hello(void)
{
    printf("Hello, World\n");
}

void goodbye()
{
    printf("Good Bye, World\n");
}

int add(int x, int y)
{
    return x + y;
}

int subtract(int x, int y)
{
    return x - y;
}

int multiply(int x, int y)
{
    return x * y;
}

int main(void)
{
    void (*message) (void);

    message = hello;
    message();
    message = goodbye;
    message();
    printf("\n");

    int a = 10;
    int b = 5;
    int result;
    int (*operation) (int a, int b);

    operation = add;
    result = operation(a, b);
    printf("resuolt = %d\n", result);

    operation = subtract;
    result = operation(a, b);
    printf("result = %d\n", result);
    printf("\n");

    int (*operations[3]) (int, int) = { add, subtract, multiply };
    int length = sizeof(operations) / sizeof(operations[0]);

    for (int i = 0; i < length; i++)
    {
        result = operations[i](a, b);
        printf("result = %d\n", result);
    }

    return 0;
}
