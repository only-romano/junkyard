#include <stdio.h>
#include <locale.h>
//#include <windows.h>
#include "number.h"
#include "number.c"

#define BEGIN {
#define END }
#define N 23

int main(void)
BEGIN
    char *locale = setlocale(LC_ALL, "");
    //SetConsoleCP(1251);
    //SetConsoleOutputCP(1251);

    printf("Русский текст!\n%d\n%d\n", number, N);
    #undef N
    #define N 55
    int age;
    char name[10];
    float weight;
    scanf("%s %d %f", &name, &age, &weight);

    printf("Name: %s \t Age: %d \t Weight: %4.2f", name, age, weight);
    printf("%d", N);
    return 0;
END
