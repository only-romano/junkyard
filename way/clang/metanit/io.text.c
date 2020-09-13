#include <stdio.h>

int main(void)
{
    char * message = "Hello \n world!\n An apple a day keeps the doctor away";
    char * filename = "data5.txt";
    char cc[256];
    FILE *fp;

    if ((fp = fopen(filename, "w")) == NULL)
    {
        perror("Error occured while opening file");
        return 1;
    }
    fputs(message, fp);

    fclose(fp);

    if ((fp = fopen(filename, "r")) == NULL)
    {
        perror("Error occured while opening file");
        return 1;
    }
    while ((fgets(cc, 256, fp)) != NULL)
    {
        printf("%s", cc);
    }

    fclose(fp);
    return 0;
}
