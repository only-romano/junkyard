typedef struct
{
    int width;
    int height;
} rectangle;

enum response_type { DUMP, SECOND_CHANCE, MARRIAGE };

typedef struct
{
    char *name;
    enum response_type type;
} response;

void comprahansion();
int compare_scores(const void* score_a, const void* score_b);
int compare_scores_desc(const void* score_a, const void* score_b);
int compare_areas(const void* a, const void* b);
int compare_areas_desc(const void* a, const void* b);
int compare_names(const void* a, const void* b);
int compare_names_desc(const void* a, const void* b);

void dating();
void dump(response r);
void second_chance(response r);
void marriage(response r);
