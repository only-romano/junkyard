#include <stdio.h>

int main(void)
{
    char * filename1 = "data5.txt";
    char * filename2 = "data4.txt";
    char cc[256];
    FILE *f1, *f2;

    if ((f1 = fopen(filename1, "r")) == NULL)
    {
        perror("Error occured while opening file");
        return 1;
    }
    if ((f2 = fopen(filename2, "w")) == NULL)
    {
        perror("Error occured while opening file");
        return 1;
    }

    while ((fgets(cc, 256, f1)) != NULL)
    {
        fputs(cc, f2);
        printf("%s", cc);
    }

    fclose(f1);
    fclose(f2);

    return 0;
}