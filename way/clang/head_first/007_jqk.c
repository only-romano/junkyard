#include <stdio.h>
#include <string.h>

void moveCard();
void musicMachine();
int search_track(char *tracks[], int len);
int find_track(char *tracks[], int len, char* search_for);

int main(void)
{
    moveCard();
    musicMachine();

    return 0;
}

void moveCard()
{
    char cards[] = "JQK";
    char a_card = cards[2];

    cards[2] = cards[1];
    cards[1] = cards[0];
    cards[0] = cards[2];
    cards[2] = cards[1];
    cards[1] = a_card;

    puts(cards);
}

void musicMachine()
{
    int len = 5;
    int searchResult;
    char *tracks[80] = {
        "Over the cloudy rainbow",
        "Why dont you sell me drugs",
        "Slaughter house",
        "Kiss me then its over",
        "Goodbay my love goodbay"
    };

    searchResult = search_track(tracks, len);
    if (searchResult > -1)
        printf("%s\n", tracks[searchResult]);
    else
        printf("No results...\n");
}

int search_track(char *tracks[], int len)
{
    char search_for[80];
    printf("Search for: ");
    fgets(search_for, 80, stdin);
    search_for[strlen(search_for) - 1] = '\0';
    return find_track(tracks, len, search_for);
}

int find_track(char *tracks[], int len, char* search_for)
{
    for (int i = 0; i < len; i++)
    {
        if (strstr(tracks[i], search_for))
            return i;
    }
    return -1;
}
