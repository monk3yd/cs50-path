#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{

    int height = 3;
    int width = 3;

//prints a 3x3 grid from ints 1 to 9 inclusive.
    int arr[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int tmp[3][3];
    int counter = 0;
    int average = 0;
    float a = 0.0;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            tmp[i][j] = arr[i][j];
            //printf("%i", tmp[i][j]);
            
            for (int k = i - 1; k <= i + 1; k++)
            {
                for (int m = j - 1; m <= j + 1; m++)
                {
                    if ((k >= 0 || k <= height - 1) && (m >= 0 || m <= width - 1)) 
                    {
                       average = average + tmp[k][m];
                       counter++;
                    }
                }
            }
            a = (float) average / (float) counter;
            printf("%f", a);
        }
        printf("\n");
    }
}


//blur correctly filters pixel in corner
((k == 0 && m == 0) || (k == 1 && m == 0) || (k == 0 && m == 1) || (k == 1 && m == 1)) 



for (int ii = -1; ii <= 1; ii++)
{
    for (int jj = 1; jj <= 1; jj++)
    {
                    //check if each of the pixels in a 3x3 grid are valid. if they are take RGB value from original pixel, add it to counter. 
        if (i + ii >= 0 && i + ii < height && j + jj >= 0 && j + jj < width)
        {
        redcount = redcount + image[i + ii][j + jj].rgbtRed;
        greencount = greencount + image[i + ii][j + jj].rgbtGreen;
        bluecount = bluecount + image[i + ii][j + jj].rgbtBlue;
        counter++;          //counts how many diff pixels you have taken RGB values from
        }
    }   
}
