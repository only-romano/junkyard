#include <stdio.h>

int main(void)
{
    printf("1");
    getchar();
    printf("2");
    getchar();
    printf("3\n");

    char name[20];
    puts("Enter name: ");

    gets(name);
    printf("Your name: %s", name);

    int c;
    while ((c = getchar()) != EOF)
    {
        putchar(c);
    }

    return 0;
}
