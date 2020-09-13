#include <string.h>
#include <stdio.h>
#include <errno.h>
#include <process.h>

int main(int argc, char *argv[])
{
    char *my_env[] = { "FOOD=coffee"/*donuts*/, NULL };
    if (execle("coffee.exe"/*, "coffee.exe"*/,
        "donuts"/*cream, coffee*/, NULL, my_env) == -1)
    {
        fprintf(stderr, "Cannot make an order: %s\n", strerror(errno));
        return 1;
    }
    return 0;
}
