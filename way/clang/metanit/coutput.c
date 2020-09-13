#include <stdio.h>

int main(void)
{
    printf("\t\\\'\n\"\n");
    printf("%c, %s, %d, %i, %u, %f\n", 200, "Hello", 5, -50, 99, 1.55);
    printf("%e, %g, %o, %x, %X, %%", 0.0015, 1.255750, 66, 188, 188);

    float r = 71.8986;
    short s = 7100;
    printf("\nx = %4.2f; y = %hd\n", r, s);

    printf("Name: %s \t Age: %d \t Weight: %3.2f\n", "Kate", 19, 51.3456);

    printf("%d; % d; %+d; %#o; %#3.2f", 8, 8, +8, 8, 8.);
    return 0;
}
