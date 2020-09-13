#include <stdio.h>

struct person
{
    char name[20];
    int age;
};

int main(void)
{
    char * filename = "users.dat";
    char * text = "%s\t%d\n";
    // Writing
    struct person people[] = { "Tom", 23, "Alice", 27, "Bob", 31, "Kate", 29 };
    int n = sizeof(people) / sizeof(people[0]);
    FILE *fp;

    if ((fp = fopen(filename, "w")) == NULL)
    {
        perror("Error occured while opening file");
        return 1;
    }

    for (int i = 0; i < n; i++)
    {
        fprintf(fp, text, people[i].name, people[i].age);
    }
    fclose(fp);

    // Reading
    char name[20];
    int age;

    if ((fp = fopen(filename, "r")) == NULL)
    {
        perror("Error occured while opening file");
        return 1;
    }
    while (fscanf(fp, text, &name, &age) != EOF)
    {
        printf(text, name, age);
    }
    fclose(fp);

    return 0;
}
