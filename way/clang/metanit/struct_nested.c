#include <stdio.h>

struct company
{
    char name[20];
    char country[30];
};

struct smartphone
{
    char title[20];
    int price;
    struct company manufacturer;
};

int main(void)
{
    struct smartphone phone = { "iPhone 8", 56000, "Apple", "USA" };
    printf("\nPhone: %s\nPrice: %d\nManufacturer: %s\n", phone.title, phone.price, phone.manufacturer.name);

    printf("Enter phone title: ");
    scanf("%20s", &phone.title);
    printf("Enter price: ");
    scanf("%d", &phone.price);
    printf("Enter manufacturer: ");
    scanf("%20s", &phone.manufacturer.name);
    printf("Enter country: ");
    scanf("%30s", &phone.manufacturer.country);
    printf("\nPhone: %s\nPrice: %d\nManufacturer: %s", phone.title, phone.price, phone.manufacturer.name);

    return 0;
}
