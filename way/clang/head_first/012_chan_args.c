#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char line[80];
    int flag;

    if (argc < 5)
    {
        fprintf(stderr, "You have to pass at least 4 arguments\n");
        return 1;
    }
    // [name, in, v1, f1, v2, f2, out]
    // [1,3,5,6]
    FILE *all[(argc+1)/2];
    if (!all[0] = fopen(argv[1], "r"))
    {
        fprintf(stderr, "Cannot open file %s.\n", argv[1]);
        return 1;
    }
    for (int i = 3; i < argc; i += 2)
        all[i/2] = fopen(argv[i], "w");
    all[argc/2] = fopen(argv[argc-1], "w");

    while (fscanf(all[0], "%79[^\n]\n", line) == 1)
    {
        flag = 1;
        for (int i = 2; i < argc-1; i+=2)
        {
            if (strstr(line, argv[i]))
            {
                fprintf(all[i/2], "%s\n", line);
                flag = 0;
                break;
            }
        }

        if (flag)
            fprintf(all[argc/2], "%s\n", line);
    }

    for (int i = 0; i <= argc/2; i++)
        fclose(all[i]);

    return 0;
}
