struct exercise
{
    const char *description;
    float duration;
};

struct meal
{
    const char *ingredients;
    float weight;
};

struct preferences
{
    struct meal food;
    struct exercise exercise;
};

typedef struct
{
    const char *name;
    const char *species;
    int teeth;
    int age;
    struct preferences care;
} fish;

typedef struct
{
    int cell_no;
    const char *wallpaper;
    float minutes_of_charge;
} phone;

typedef struct
{
    float tank_capacity;
    int tank_psi;
    const char *suit_material;
} equipment;

typedef struct scuba
{
    const char *name;
    equipment kit;
} diver;

typedef struct
{
    const char *name;
    const char *species;
    int age;
} turtle;

typedef struct
{
    const char *description;
    float value;
} swag;

typedef struct 
{
    swag *swag;
    const char *sequence;
} combination;

typedef struct
{
    combination numbers;
    const char *make;
} safe;

void catalog(fish f);
void label(fish f);
void favorites(fish f);
void cellphone(phone p);
void badge(diver d);
void happy_birthday(turtle *t);
void open_safe(safe *s);
