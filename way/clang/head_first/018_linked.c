#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "linked.h"

int main(void)
{
    islands();

    return 0;
}

void islands()
{
    char name[80];
    island *start = NULL;
    for (island *i = NULL, *next = NULL; fgets(name, 80, stdin) != NULL; i = next)
    {
        next = create_island(name);
        if (start == NULL)
            start = next;
        if (i != NULL)
            i->next = next;
    }

    display_islands(start);
    release(start);
}

island* create_island(char *name)
{
    island *i = malloc(sizeof(island));
    i->name = strdup(name);
    i->opens = "09:00";
    i->closes = "17:00";
    i->next = NULL;
    return i;
}

void display_islands(island *start)
{
    for (island *i = start; i != NULL; i = i->next)
        printf("Name: %sOpen: %s-%s\n\n", i->name, i->opens, i->closes);
}

void release(island *start)
{
    for (island *i = start, *next = NULL; i != NULL; i = next)
    {
        next = i->next;
        free(i->name);
        free(i);
    }
}
