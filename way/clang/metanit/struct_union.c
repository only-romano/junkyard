#include <stdio.h>

typedef union
{
    int digit;
    char letter;
} code;

int main(void)
{
    code id;
    id.digit = 120;
    printf("%d - %c\n%d - %d\n", id.digit, id.letter, id.digit, id.letter);

    id.letter = 87;
    printf("%d - %c\n", id.digit, id.letter);

    id.digit = 47;
    code * p_id = &id;
    printf("%d - %c\n", p_id->digit, p_id->letter);
    p_id->digit = 89;
    printf("%d - %c\n", p_id->digit, p_id->letter);

    return 0;
}
