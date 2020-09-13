#include <stdio.h>

int min(int *nums, int size);
int max(int *nums, int size);

int main(void)
{
    int ar[] = { 5, 2, 1, 7, 14, 2, -3, 8 };
    printf("Max element is %i\nMin element is %i\n", max(ar, 8), min(ar, 8));
    
    return 0;
}
// (y<5) { x++; y(<3) x--; } y+=2;
// (x < 5)
// x+1;y=y+x    2       4       6       8       7
// print(xy)    
// x = x+1      1       2       4       5       5

// 00      11      21      32      42
// 00      11      23      36      410
// 02      14      25      36      47
// 11      34      59
// 02      14      36      48

int max(int *nums, int size)
{
    int result = nums[0];
    for (int i = 1; i < size; i++)
        if (nums[i] > result)
            result = nums[i];
    return result;
}

int min(int *nums, int size)
{
    int result = nums[0];
    for (int i = 1; i < size; i++)
        if (nums[i] < result)
            result = nums[i];
    return result;
}
