#include <stdio.h>
#include <stdlib.h>

int dealCard();

int main(void)
{
    int game = 1;
    while (game)
        game = dealCard();
    return 0;
}

int dealCard()
{
    static int count = 0;
    char card_name[3];
    int val = 0;
    puts("Input card name (X for exit): ");
    scanf("%2s", card_name);
    switch (card_name[0])
    {
        case 'K':
        case 'Q':
        case 'J':
            val = 10;
            break;
        case 'A':
            val = 11;
            break;
        case 'X':
            return 0;
        default:
            val = atoi(card_name);
            if (val > 10 || val < 2)
                val = 0;
    }
    if (val > 9)
        count++;
    else if (val > 2 && val < 7)
        count--;
    printf("Card's value is %i%s\n", val, (val == 0 ? " (error)" : ""));
    printf("Chance to win counter: %i\n", count);
    return 1;
}
