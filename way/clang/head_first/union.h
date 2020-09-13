typedef enum
{
    COUNT, POUNDS, PINTS
} unit_of_measure;

typedef union
{
    short count;
    float weight;
    float volume;
} quantity;

typedef struct
{
    const char *name;
    const char *country;
    quantity amount;
    unit_of_measure units;
} fruit_order;

typedef union
{
    float lemon;
    int lime_pieces;
} lemon_lime;

typedef struct
{
    float tequila;
    float cointreaau;
    lemon_lime citrus;
} margarita;

typedef struct
{
    unsigned int first_visit:1;
    unsigned int come_again:1;
    unsigned int fingers_lost:4;
    unsigned int shark_attack:1;
    unsigned int days_a_week:3;
} survey;

void get_fruits();
void get_margarita();
void display_margarita(margarita m, char c);
void measure_fruits();
void display(fruit_order f);
