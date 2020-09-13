#include <stdio.h>
#include <stdlib.h>

struct person
{
    char name[20];
    int age;
};

int save(char * filename, struct person *st, int n);
int load(char * filename);

int main(void)
{
    char * filename = "people.dat";
    struct person people[] = { "Tom", 23, "Alice", 27, "Bob", 31, "Kate", 29 };
    int n = sizeof(people) / sizeof(people[0]);

    save(filename, people, n);
    load(filename);

    return 0;
}

int save(char * filename, struct person * st, int n)
{
    FILE * fp;
    char *c;

    int size = n * sizeof(struct person);

    if ((fp = fopen(filename, "wb")) == NULL)
    {
        perror("Error occured while opening file");
        return 1;
    }

    c = (char *)&n;
    for (int i = 0; i < sizeof(int); i++)
    {
        putc(*c++, fp);
    }

    c = (char *)st;
    for (int i = 0; i < size; i++)
    {
        putc(*c, fp);
        c++;
    }
    fclose(fp);

    return 0;
}

int load(char * filename)
{
    FILE * fp;
    char *c;
    int m = sizeof(int);
    int n, i;

    int *pti = (int *)malloc(m);

    if ((fp = fopen(filename, "r")) == NULL)
    {
        perror("Error occured while opening file");
        return 1;
    }

    c = (char *)pti;
    while (m > 0)
    {
        i = getc(fp);
        if (i == EOF)
            break;
        *c = i;
        c++;
        m--;
    }
    n = *pti;

    struct person * ptr = (struct person *) malloc(n * sizeof(struct person));
    c = (char * )ptr;

    while ((i = getc(fp)) != EOF)
    {
        *c = i;
        c++;
    }
    printf("\n%d people in the file stored\n\n", n);

    for (int k = 0; k < n; k++)
    {
        printf("%-5d %-20s %5d \n", k+1, (ptr+k)->name, (ptr+k)->age);
    }

    free(pti);
    free(ptr);
    fclose(fp);

    return 0;
}
