#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int x = get_int("x: ");
    int tmp;
    int arr[x];
    
    for (int j = 0; j < x; < j++)
    {
        
    }
    
    for (int i = 0; i < 9; i++)
    {
        if (9 % 2 == 1 && i < (9 / 2))
        {
            tmp = arr[i];
            arr[i] = arr[8 - i];
            arr[8 - i] = tmp;
            
        }
        printf("%i", arr[i]);
    }
    printf("\n");
    return 0;
}