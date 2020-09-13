#include <stdio.h>
#include <stdlib.h>

struct person
{
    char name[20];
    int age;
};

int save(char * filename, struct person *st, int n);
int load(char * filenmae);

int main(void)
{
    char * filename = "people1.dat";
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
    int n = sizeof(struct person);

    int i;
    printf("Input user number: ");
    scanf("%d", &i);

    int pos = (i-1) * n + 4;

    if ((fp = fopen(filename, "rb")) == NULL)
    {
        perror("Error occured while opening file");
        return 1;
    }

    fseek(fp, pos, SEEK_SET);

    struct person * ptr = (struct person *) malloc(sizeof(struct person));
    c = (char *)ptr;

    while (n > 0)
    {
        i = getc(fp);
        if (i == EOF)
            break;
        *c = i;
        c++;
        n--;
    }

    printf("%s \t %d \n", ptr->name, ptr->age);
    free(ptr);

    fclose(fp);
    return 0;
}
