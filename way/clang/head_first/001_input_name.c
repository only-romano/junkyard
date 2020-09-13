#include <stdio.h>

int main()
{
    char name[30];
    printf("Input your name: ");
    fgets(name, 30, stdin);
    printf("Hello, %s\n", name);
    return 0;
}
