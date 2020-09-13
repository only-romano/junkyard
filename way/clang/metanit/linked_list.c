#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int val;
    struct node *next;
} node_t;

void print_list(node_t * head);
void push(node_t * head, int val);
void push_start(node_t ** head, int val);
int pop(node_t ** head);
int remove_last(node_t * head);
int remove_by_index(node_t ** head, int n);
int remove_by_value(node_t ** head, int val);
void free_all(node_t * head);

int main(void)
{
    node_t *head = NULL;
    head = (node_t *) malloc(sizeof(node_t));
    if (head == NULL)
        return 1;

    head->val = 1;
    head->next = (node_t *) malloc(sizeof(node_t));
    head->next->val = 2;
    head->next->next = NULL;

    push(head, 3);
    push(head, 4);
    push(head, 5);
    push(head, 6);
    push_start(&head, 0);
    print_list(head);
    pop(&head);
    remove_last(head);
    remove_by_index(&head, 2);
    remove_by_value(&head, 4);
    print_list(head);
    free_all(head);
}

void push(node_t * head, int val)
{
    node_t * current = head;
    while (current->next != NULL)
        current = current->next;

    current->next = (node_t *) malloc(sizeof(node_t));
    current->next->val = val;
    current->next->next = NULL;
}

void push_start(node_t ** head, int val)
{
    node_t * new_node;
    new_node = (node_t *) malloc(sizeof(node_t));
    new_node->val = val;
    new_node->next = *head;
    *head = new_node;
}

int pop(node_t ** head)
{
    int retval = -1;
    node_t * next_node = NULL;
    if (*head == NULL)
        return -1;

    next_node = (*head)->next;
    retval = (*head)->val;
    free(*head);
    *head = next_node;

    return retval;
}

int remove_last(node_t * head)
{
    int retval = 0;
    if (head->next == NULL)
    {
        retval = head->val;
        free(head);
        return retval;
    }

    node_t * current = head;
    while (current->next->next != NULL)
        current = current->next;

    retval = current->next->val;
    free(current->next);
    current->next = NULL;
    return retval;
}

int remove_by_index(node_t ** head, int n)
{
    int i = 0;
    int retval = -1;
    node_t * current = *head;
    node_t * temp_node = NULL;

    if (n == 0)
        return pop(head);

    for (i = 0; i < n-1; i++)
    {
        if (current->next == NULL)
            return -1;
        current = current->next;
    }

    temp_node = current->next;
    retval = temp_node->val;
    current->next = temp_node->next;
    free(temp_node);

    return retval;
}

int remove_by_value(node_t ** head, int val)
{
    int retval = -1;
    node_t * current = *head;
    node_t * temp_node = NULL;

    if (current->val == val)
        return pop(head);

    while (current->next != NULL)
    {
        if (current->next->val == val)
        {
            retval = current->next->val;
            temp_node = current->next->next;
            break;
        }
        current = current->next;
    }

    if (temp_node == NULL)
        return -1;
    free(current->next);
    current->next = temp_node;
    return retval;
}

void print_list(node_t * head)
{
    node_t * current = head;
    while (current != NULL)
    {
        printf("%d\n", current->val);
        current = current->next;
    }
    printf("\n");
}

void free_all(node_t * head)
{
    node_t * current = head;
    node_t * to_free = NULL;
    while (current != NULL)
    {
        to_free = current;
        current = current->next;
        free(to_free);
    }
}
