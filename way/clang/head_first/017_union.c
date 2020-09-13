#include <stdio.h>
#include <string.h>
#include "union.h"

int main(void)
{
    get_fruits();
    get_margarita();
    measure_fruits();

    return 0;
}

void get_fruits()
{
    fruit_order apples = {"apple", "England", .amount.weight=4.2};
    printf("This order contains %2.2f pounds of %s from %s\n\n", 
        apples.amount.weight, apples.name, apples.country);
}

void get_margarita()
{
    margarita m1 = {2.0, 1.0, {0.5}};
    margarita m2 = {2.0, 1.0, .citrus.lemon=2};
    margarita m3 = {2.0, 1.0, 0.5};
    margarita m4 = {2.0, 1.0, {.lime_pieces=1}};
    margarita m5 = {2.0, 1.0, {1}};
    margarita m6 = {2.0, 1.0, {2}};

    display_margarita(m2, 'A');
    display_margarita(m1, 'A');
    display_margarita(m4, 'L');
}

void display_margarita(margarita m, char c)
{
    if (c == 'L')
        printf("%2.1f tequila\n%2.1f cointreaau\n%i lime pieces\n\n", 
            m.tequila, m.cointreaau, m.citrus.lime_pieces);
    else
        printf("%2.1f tequila\n%2.1f cointreaau\n%2.1f juice\n\n", 
            m.tequila, m.cointreaau, m.citrus.lemon);
}

void measure_fruits()
{
    fruit_order apples = {"apples", "England", .amount.count=144, COUNT};
    fruit_order swb = {"strawberries", "Spain", .amount.weight=17.6, POUNDS};
    fruit_order oj = {"orange juice", "USA", .amount.volume=10.5, PINTS};
    display(apples);
    display(swb);
    display(oj);
}

void display(fruit_order f)
{
    printf("This order contains ");
    if (f.units == PINTS)
        printf("%2.2f pints of %s\n", f.amount.volume, f.name);
    else if (f.units == POUNDS)
        printf("%2.2f pounds of %s\n", f.amount.weight, f.name);
    else
        printf("%i %s\n", f.amount.count, f.name);
}
