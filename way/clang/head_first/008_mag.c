#include <stdio.h>
#include <string.h>

void print_reverse(char *s);
void getJSON();

int main(void)
{
    print_reverse("\nHello");
    getJSON();
    return 0;
}

void print_reverse(char *s)
{
    size_t len = strlen(s);
    char *t = s + len - 1;
    while (t >= s)
    {
        printf("%c", *t);
        t -= 1;
    }
    puts("");
}

void getJSON()
{
    float latitude;
    float longitude;
    char info[80];
    int started = 0;
    puts("data=[");
    while (scanf("%f,%f,%79[^\n]", &latitude, &longitude, info) == 3)
    {
        if (started)
            printf(",\n");
        else
            started = 1;
        printf("{latitude: %f, longitude: %f, info: '%s'", latitude, longitude, info);
    }
    puts("\n]");
}
