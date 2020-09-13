#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "system_t.h"

int main(void)
{
    //system("dir");
    char comment[80];
    char cmd[120];
    scanf("%79[^\n]", &comment);
    sprintf(cmd, "echo '%s %s' >> reports.log", comment, now());
    system(cmd);
    return 0;
}

char* now()
{
    time_t t;
    time (&t);
    return asctime(localtime (&t));
}
