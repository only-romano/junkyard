#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    char *delivery = "";
    int thick = 0;
    int count = 0;
    char ch;

    while ((ch = getopt(argc, argv, "d:t")) != EOF)
        switch (ch)
        {
            case 'd':
                delivery = optarg;
                break;
            case 't':
                thick = 1;
                break;
            default:
                fprintf(stderr, "Unknown parameter: '%s'\n", optarg);
                return 1;
        }

    argc -= optind;
    argv += optind;

    if (thick)
        puts("Lush cake.");
    if (delivery[0])
        printf("To deliver: %s.\n", delivery);

    puts("Ingridients:");
    for (count = 0; count < argc; count++)
        puts(argv[count]);

    return 0;
}
