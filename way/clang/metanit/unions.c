#include <stdio.h>

union intParts 
{
    int theInt;
    char bytes[sizeof(int)];
};

struct operator
{
    int type;
    union {
        int intNum;
        float floatNum;
        double doubleNum;
    };
};

union Coins
{
    struct
    {
        int quarter;
        int dime;
        int nickel;
        int penny;
    };
    int coins[4];
};



int main(void)
{
    union intParts parts;
    parts.theInt = 5968145;

    // Union variant
    printf("The int is %i\nThe bytes are [%i, %i, %i, %i]\n",
        parts.theInt, parts.bytes[0], parts.bytes[1], parts.bytes[2], parts.bytes[3]);

    int theInt = parts.theInt;
    // Variant 2
    printf("The int is %i\nThe bytes are [%i, %i, %i, %i]\n",
        theInt, *((char*)&theInt), *((char*)&theInt+1), *((char*)&theInt+2), *((char*)&theInt+3));
    // Variant 3
    char * intChar = (char*)&theInt;
    printf("The int is %i\nThe bytes are [%i, %i, %i, %i]\n",
        theInt, intChar[0], intChar[1], intChar[2], intChar[3]);

    struct operator op;
    op.type = 0;
    op.intNum = 352;
    printf("%d, %f, %d", op.intNum, op.floatNum, op.doubleNum);

    union Coins change;
    for (int i = 0; i < sizeof(change) / sizeof(int); i++)
    {
        scanf("%i", change.coins + i);
    }
    printf("There are %i quarters, %i dimes, %i nickels, and %i pennies\n",
        change.quarter, change.dime, change.nickel, change.penny);

    return 0;
}
