#include <stdio.h>
#include <stdlib.h>

struct time
{
    int hour;
    int minute;
    int second;
};

struct time addminutes(struct time, int);
struct time addminutesPointer(struct time *, int);
void showTime(struct time);
struct time * input(void);

int main(void)
{
    // Time 1
    struct time current_time = {17, 38, 10};
    int minutes = 21;

    struct time result_time = addminutes(current_time, minutes);
    showTime(result_time);

    result_time = addminutes(result_time, 23);
    showTime(result_time);

    // Time 2
    struct time * p_time = &result_time;
    addminutesPointer(p_time, 382);
    showTime(result_time);

    // Time 3
    struct time *p_time2 = input();
    printf("%2d:%2d:%2d\n", p_time2->hour, p_time2->minute, p_time2->second);
    free(p_time2);

    return 0;
}

void showTime(struct time t)
{
    printf("%2d:%2d:%2d\n", t.hour, t.minute, t.second);
}

struct time addminutes(struct time t, int minutes)
{
    struct time result = { t.hour, t.minute, t.second };
    int h, d;

    result.minute += minutes;
    if (result.minute >= 60)
    {
        h = result.minute / 60;
        result.minute -= 60 * h;
        result.hour += h;
    }
    if (result.hour >= 24)
    {
        d = result.hour / 24;
        result.hour -= 24 * d;
    }
    return result;
}

struct time addminutesPointer(struct time *t, int minutes)
{
    int h, d;

    t->minute += minutes;
    if (t->minute >= 60)
    {
        h = t->minute / 60;
        t->minute -= 60 * h;
        t->hour += h;
    }
    if (t->hour >= 24)
    {
        d = t->hour / 24;
        t->hour -= 24 * d;
    }
}

struct time * input()
{
    struct time * p_time = (struct time *) malloc(sizeof(struct time));
    printf("Enter hour: ");
    scanf("%d", &p_time->hour);
    printf("Enter minutes: ");
    scanf("%d", &p_time->minute);
    printf("Enter seconds: ");
    scanf("%d", &p_time->second);

    return p_time;
}
