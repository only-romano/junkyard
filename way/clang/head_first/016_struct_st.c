#include <stdio.h>
#include "struct_st.h"

int main(void)
{
    fish snappy = {"Wolffish", "piranha", 69, 4, {
        {"meat", 0.09}, {"swim in jakuzzi", 7.5}}};
    phone iphone = {5557879, "sinatra.png", 1.35};
    diver randy = {"Randy", {5.5, 3500, " undefined"}};
    turtle myrtle = {"Tortille", "Chitine Turtle", 99};
    swag gold = {"Gold!", 1000000.0};
    combination numbers = {&gold, "6502"};
    safe s = {numbers, "RAMCON250"};

    catalog(snappy);
    favorites(snappy);
    label(snappy);
    cellphone(iphone);
    badge(randy);
    happy_birthday(&myrtle);
    printf("%s lived %i ages\n\n", myrtle.name, myrtle.age);
    open_safe(&s);

    return 0;
}

void catalog(fish f)
{
    printf("%s is %s with %i teeth. He's %i age old.\n", 
        f.name, f.species, f.teeth, f.age);
}

void label(fish f)
{
    printf("Name: %s\nSpecies: %s\nAge: %i\nTeeth: %i\n", 
        f.name, f.species, f.age, f.teeth);
    printf("To give a %.2f pounds of %s and let %s for a %.1f hours per day\n\n",
        f.care.food.weight, f.care.food.ingredients,
        f.care.exercise.description, f.care.exercise.duration);
}

void favorites(fish f)
{
    printf("%s loves to eat %s\n", f.name, f.care.food.ingredients);
    printf("%s trains %.1f hours per day\n\n", f.name, f.care.exercise.duration);
}

void cellphone(phone p)
{
    printf("Phone #%i with wallpeper image %s and charge of %.2f\n\n", 
        p.cell_no, p.wallpaper, p.minutes_of_charge);
}

void badge(diver d)
{
    printf("Name: %s\nReservour: %2.2f(%i)\nSuit: %s\n\n", 
        d.name, d.kit.tank_capacity, d.kit.tank_psi, d.kit.suit_material);
}

void happy_birthday(turtle *t)
{
    (*t).age = (*t).age + 1;
    printf("Happy Birthday, %s! Now you're %i age old!\n", (*t).name, (*t).age);
}

void open_safe(safe *s)
{
    printf("%s\n\n", s->numbers.swag->description);
}
