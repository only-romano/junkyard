#include <stdio.h>

void skip(char *msg);

int main(void)
{
    int contestants[] = { 1, 2, 3 };
    int *choice = contestants;
    contestants[0] = 2;
    contestants[1] = contestants[2];
    contestants[2] = *choice;
    printf("I'm gonna choice pretendent %i\n", contestants[2]);
    printf("Magic: %i\n", 1[contestants]);

    char *msg_from_any = "Don't call me";
    skip(msg_from_any);
    printf("Magic: %i\n", 5[msg_from_any]);

    char food[5];
    printf("Input your favorite food: ");
    fgets(food, sizeof(food), stdin);
    printf("Your favorite food is %s\n", food);

    return 0;
}

void skip(char *msg)
{
    puts(msg+6);
}
