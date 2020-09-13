#include <stdio.h>
#include <limits.h>
#include <float.h>
#include "my_header.h"

int main(void)
{
    char c[80];
    actors();
    printf("Input msg: ");
    scanf("%79[^\n]", &c);
    int len = sizeof(c) / sizeof(c[0]);
    encrypt(len, &(c[0]));
    printf("Encrypted message: %s\n", c);
    encrypt(len, &(c[0]));
    printf("Decrypted message: %s\n", c);
    return 0;
}

void actors()
{
    printf("Value INT_MAX is %i\n", INT_MAX);
    printf("Value INT_MIN is %i\n", INT_MIN);
    printf("int takes %li bytes\n", sizeof(int));

    printf("Value FLT_MAX is %i\n", FLT_MAX);
    printf("Value FLT_MIN is %i\n", FLT_MIN);
    printf("float takes %li bytes\n", sizeof(float));
}

void encrypt(int len, char *msg)
{
    while (len--)
    {
        if (*msg) *msg = *msg ^ 31;
        msg++;
    }
}
