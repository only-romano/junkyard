#include <stdio.h>
#include "dynamic.h"

int main(void)
{
    security();
    return 0;
}

void security()
{
    char s[] = "Say friend and come over";
    encrypt(s);
    printf("Encrypted to '%s'\n", s);
    printf("Control sum is %i\n", checksum(s));
    encrypt(s);
    printf("Decrypted message is '%s'\n", s);
    printf("Contril sum is %i\n", checksum(s));
}

void encrypt(char *message)
{
    while (*message)
    {
        *message = *message ^ 31;
        message++;
    }
}

int checksum(char *message)
{
    int c = 0;
    while (*message)
    {
        c += c ^ (int)(*message);
        message++;
    }
    return c;
}
