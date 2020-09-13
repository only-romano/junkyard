#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "fun_to_fun.h"

int main(void)
{
    comprahansion();
    dating();
    return 0;
}

void comprahansion()
{
    int scores[] = { 543, 323, 32, 554, 11, 3, 112 };
    qsort(scores, 7, sizeof(int), compare_scores_desc);
    puts("It's sorted scores:");
    for (int i = 0; i < 7; i++)
        printf("Score = %i\n", scores[i]);
    puts("");

    char *names[] = { "Karen Oganyan", "Mark 2", "Brad Pitt", "Slutty Molly" };
    qsort(names, 4, sizeof(char*), compare_names);
    puts("It's sorted names:");
    for (int i = 0; i < 4; i++)
        printf("%s\n", names[i]);
    puts("");
}

int compare_scores(const void* score_a, const void* score_b)
{
    int a = *(int*)score_a;
    int b = *(int*)score_b;
    return a - b;
}

int compare_scores_desc(const void* score_a, const void* score_b)
{
    int a = *(int*)score_a;
    int b = *(int*)score_b;
    return b - a;
}

int compare_areas(const void* a, const void* b)
{
    rectangle* ra = (rectangle*)a;
    rectangle* rb = (rectangle*)b;
    int area_a = (ra->width * ra->height);
    int area_b = (rb->width * rb->height);
    return area_a - area_b;
}

int compare_areas_desc(const void* a, const void* b)
{
    return compare_areas(b, a);
}

int compare_names(const void* a, const void* b)
{
    char** sa = (char**)a;
    char** sb = (char**)b;
    return strcmp(*sa, *sb);
}

int compare_names_desc(const void* a, const void* b)
{
    return compare_names(b, a);
}

// next

void dating()
{
    response r[] = {
        {"Mike", DUMP}, {"Louis", SECOND_CHANCE},
        {"Mathew", SECOND_CHANCE}, {"William", MARRIAGE}
    };

    void (*replies[])(response) = { dump, second_chance, marriage };
    for (int i = 0; i < 4; i++)
        replies[r[i].type](r[i]);
}

void dump(response r)
{
    printf("Dear %s,\n", r.name);
    puts("Your date partner contact us to tell you'll not see each over again.");
}

void second_chance(response r)
{
    printf("Dear %s,\n", r.name);
    puts("Good news! Your date partner want another date with you!");
    puts("Please call back as soon as you can!");
}

void marriage(response r)
{
    printf("Dear %s,\n", r.name);
    puts("Congratulations! Your date partner propose to marry you!");
}
