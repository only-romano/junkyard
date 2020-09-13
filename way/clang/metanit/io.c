#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE * fp, * fp2;
    fp = fopen("data.txt", "w");
    fclose(fp);
    if ((fp2 = fopen("data28.txt", "r")) == NULL)
    {
        perror("Error occured while opening data28.txt");
        exit(0);
    }
    fclose(fp2);
    return 0;
}
