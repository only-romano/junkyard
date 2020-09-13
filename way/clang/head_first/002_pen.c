#include <stdio.h>

int main(void)
{
    int card_count = 11;
    if (card_count > 10)
        puts("Cards in deck are lucky one. Raise!");

    int c = 10;
    while (c-- > 0)
        puts("I'm not supposed to use clases");

    char ex[20];
    puts("Input your girls name: ");
    scanf("%19s", ex);
    printf("Dear %s. \n\n\tWe're Done.\n", ex);

    char suit = 'H';
    switch (suit)
    {
        case 'C':
            puts("Clubs!");
            break;
        case 'D':
            puts("Diamonds!");
            break;
        case 'H':
            puts("Hearts!");
            break;
        default:
            puts("Spades!");
    }
}
