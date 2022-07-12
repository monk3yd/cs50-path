#include <stdio.h>

int main(void)
{
    int tmp;
    int arr[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    
    for (int i = 0; i < 10; i++)
    {
        if (10 % 2 == 0 && i < (10 / 2))
        {
            tmp = arr[i];
            arr[i] = arr[9 - i];
            arr[9 - i] = tmp;
            
        }
        printf("%i", arr[i]);
    }
    printf("\n");
    return 0;
}