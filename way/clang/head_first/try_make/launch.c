#include <stdio.h>
#include "launch.h"
#include "thruster.h"

int main(void)
{
    launch();
    thruster();
    return 0;
}

void launch()
{
    printf("Launch!\n");
}

void thruster()
{
    printf("Launch Thruster!\n");
}
