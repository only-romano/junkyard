#include <stdio.h>

#define PERSON struct { int age; char name[20]; }

struct man
{
    int age;
    char * name;
} bob, alice;

typedef struct
{
    int age;
    char * name;
} person;

int main(void)
{
    struct man rome = { 19, "Rome" };
    printf("Age: %d \t Name: %s\n", rome.age, rome.name);
    PERSON kate = { 19, "Kate" };
    printf("Age: %d \t Name: %s\n", kate.age, kate.name);
    person tom = { 23, "Tom" };
    printf("Age: %d \t Name: %s\n", tom.age, tom.name);
    printf("Enter name: ");
    scanf("%s", &bob.name);
    printf("Enter age: ");
    scanf("%d", &bob.age);
    printf("Age: %d \t Name: %s\n", bob.age, bob.name);
    alice.name = "Alice";
    alice.age = 25;
    printf("Age: %d \t Name: %s\n", alice.age, alice.name);
    return 0;
}
