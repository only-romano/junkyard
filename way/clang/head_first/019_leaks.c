#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "leaks.h"


int main(void)
{
    char question[80];
    char suspect[40];
    node *start_node = create("Does suspect has mustache");
    start_node->no = create("Lorette Barnshwarz");
    start_node->yes = create("Ivan Lozhkin");

    node *current;
    do
    {
        current = start_node;
        while (1)
        {
            if (yes_no(current->question))
            {
                if (current->yes)
                {
                    current = current->yes;
                }
                else
                {
                    printf("Suspect catched!\n");
                    break;
                }
            }
            else if (current->no)
            {
                current = current->no;
            }
            else
            {
                printf("Who's suspect? ");
                fgets(suspect, 40, stdin);
                node *yes_node = create(suspect);
                current->yes = yes_node;

                node *no_node = create(current->question);
                current->no = no_node;

                printf("Ask me a question to detect %s but not %s. ",
                    suspect, current->question);
                fgets(question, 80, stdin);
                free(current->question);
                current->question = strdup(question);

                break;
            }
        }
    }
    while (yes_no("One more time"));

    release(start_node);

    return 0;
}

int yes_no(char *question)
{
    char answer[3];
    printf("%s? (y/n): ", question);
    fgets(answer, 3, stdin);
    return answer[0] == 'y';
}

node* create(char *question)
{
    node *n = malloc(sizeof(node));
    n->question = strdup(question);
    n->no = NULL;
    n->yes = NULL;
    return n;
}

void release(node *n)
{
    if (n)
    {
        if (n->no)
            release(n->no);
        if (n->yes)
            release(n->yes);
        if (n->question)
            free(n->question);
        free(n);
    }
}
