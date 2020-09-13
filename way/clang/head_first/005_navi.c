#include <stdio.h>

void go_south_east(int *lat, int *lon);

int main(void)
{
    char msg[] = "Hello darkness my old friend!";
    printf("String msg has an address: %p\n", msg);
    int latitude = 32;
    int longitude = -64;
    go_south_east(&latitude, &longitude);
    printf("Stop! Our coordinates now: [%i, %i]\n", latitude, longitude);
}

void go_south_east(int *lat, int *lon)
{
    (*lat)--;
    (*lon)++;
}
