#include <assert.h>

const short FLAG_ON             = 1 << 0;
const short FLAG_MOVEMENT       = 1 << 1;
const short FLAG_TRANSPARENT    = 1 << 2;
const short FLAG_ALIVE          = 1 << 3;
const short FLAG_BROKEN         = 1 << 4;
const short FLAG_EDIBLE         = 1 << 5;

int main(void)
{
    short attributes = 0;

    attributes |= FLAG_ON;
    attributes |= FLAG_TRANSPARENT;
    attributes |= FLAG_BROKEN;
    assert(attributes == FLAG_ON | FLAG_TRANSPARENT | FLAG_BROKEN);

    attributes |= FLAG_ALIVE;
    attributes ^= FLAG_TRANSPARENT;
    attributes &= ~FLAG_BROKEN;
    assert(attributes == FLAG_ON | FLAG_ALIVE);

    assert(attributes & FLAG_ALIVE);
    assert(!(attributes & FLAG_BROKEN));

    attributes = FLAG_EDIBLE;
    assert(attributes == FLAG_EDIBLE);

    //00010101
    //00000000
    //00001001
    return 0;
}