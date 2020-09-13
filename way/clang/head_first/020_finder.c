#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "finder.h"

int main(void)
{
    finder();
    return 0;
}

void finder()
{
    int NUM_ADS = 7;
    char *ADS[] = {
        "William: lonely, afroamerican, humor, sport, tv, food",
        "Mathiew: lonely, european, nosmoking, art, movie, theater",
        "Louis: lonely, latinoamerican, nodrinking, books, theater, art",
        "Mike: devorced, european, trucks, sport, Justin Bieber",
        "Piter: lonely, asian, chess, gym, art",
        "Josh: lonely, jewish, sport, movie, theater",
        "Djedd: devorced, afroamerican, theater, books, food"
    };
    char *pluses[] = {
        "2", "sport", "theater"
    };
    char *minuses[] = {
        "1", "Bieber"
    };

    find(NUM_ADS, ADS, pluses, minuses);
}

void find(int count, char *ads[], char *pluses[], char *minuses[])
{
    puts("Results of search:");
    for (int i = 0; i < count; i++)
    {
        int next = 0;
        for (int j = 1; j <= atoi(pluses[0]); j++)
        {
            if (!strstr(ads[i], pluses[j]))
            {
                next = 1;
                break;
            }
        }
        if (next) continue;

        for (int j = 0; j < atoi(minuses[0]); j++)
        {
            if (strstr(ads[i], minuses[j]))
            {
                next = 1;
                break;
            }

        }
        if (next) continue;

        printf("\t%s\n", ads[i]);
    }
}
