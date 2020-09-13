#include <stdio.h>
#include <stdarg.h>
#include "args.h"

int main(void)
{
    printf("Full price is %.2f\n", total(3, MONKEY_GLAND, MUDSLIDE, FUZZY_NAVEL));

    return 0;
}

double total(int args, ...)
{
    double total = 0;
    va_list ap;
    va_start(ap, args);
    for (int i = 0; i < args; i++)
    {
        total += price(va_arg(ap, enum drink));
    }
    va_end(ap);

    return total;
}

double price(enum drink d)
{
    switch (d)
    {
        case MUDSLIDE:
            return 6.79;
        case FUZZY_NAVEL:
            return 5.31;
        case MONKEY_GLAND:
            return 4.82;
        case ZOMBIE:
            return 5.89;
    }
    return 0;
}
