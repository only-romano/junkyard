typedef struct island
{
    char *name;
    char *opens;
    char *closes;
    struct island *next;
} island;

void islands();
island* create_island(char *name);
void display_islands(island *start);
void release(island *start);
