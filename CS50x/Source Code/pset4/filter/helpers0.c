#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

//for each pixel de RGB values must be the same.
//iterate through each pixel of the grid.
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //extract value of each color of a pixel, if pixel isn't grey.
            if (image[i][j].rgbtRed != image[i][j].rgbtGreen || image[i][j].rgbtRed != image[i][j].rgbtBlue || image[i][j].rgbtGreen != image[i][j].rgbtBlue)
            {

        // which value to set it? for lighter color lighter grey and viceversa
                int x = image[i][j].rgbtRed;
                int y = image[i][j].rgbtGreen;
                int z = image[i][j].rgbtBlue;

        //calculate color average value with the 3 colors.
                float average = (float) (x + y + z) / (float) 3;
                int faverage = round(average);

        //change pixel's color value to average grey value
                image[i][j].rgbtRed = faverage;
                image[i][j].rgbtGreen = faverage;
                image[i][j].rgbtBlue = faverage;
            }
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{

//iterate thrpugh each pixel of the grid.
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int x = image[i][j].rgbtRed;
            int y = image[i][j].rgbtGreen;
            int z = image[i][j].rgbtBlue;

            float sepiaRed = (0.393 * x) + (0.769 * y) + (0.189 * z);
            float sepiaGreen = (0.349 * x) + (0.686 * y) + (0.168 * z);
            float sepiaBlue = (0.272 * x) + (0.534 * y) + (0.131 * z);

            x = round(sepiaRed);
            y = round(sepiaGreen);
            z = round(sepiaBlue);

            if (x > 255)
            {
                x = 255;
            }

            if (y > 255)
            {
                y = 255;
            }

            if (z > 255)
            {
                z = 255;
            }

            image[i][j].rgbtRed = x;
            image[i][j].rgbtGreen = y;
            image[i][j].rgbtBlue = z;
        }
    }
    return;
}



// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{

     //move pixels around the grid.
     //use tmp for swapping.

     RGBTRIPLE tmp;
     for (int i = 0; i < height; i ++)
     {
         for (int j = 0; j < width; j++)
         {
            if (j < (width / 2))
            {
                tmp = image[i][j];
                image[i][j] = image[i][(width - 1) - j];
                image[i][(width - 1) - j] = tmp;
            }
         }
     }
     return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    
    RGBTRIPLE copy[height][width];
    
    int redcount = 0;
    int greencount = 0;
    int bluecount = 0;
    
    int counter = 0;
    
    //photo grid
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
            
            //pixel value grid
            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    if (copy[i - k][j - l] != 0)
                    {
                        redcount = copy[i - k][j - l].rgbtRed;
                        greencount = copy[i - k][j - l].rgbtGreen;
                        bluecount = copy[i - k][j - l].rgbtBlue;
                        counter++;
                    }
                }    
            }
            
            float average_red = (float) redcount / (float) counter;
            float average_green = (float) greencount / (float) counter;
            float average_blue = (float) bluecount / (float) counter;
            
            int r = round(average_red);
            int g = round(average_green);
            int b = round(average_blue);
            
            r = image[i][j].rgbtRed;
            g = image[i][j].rgbtGreen;
            b = image[i][j].rgbtBlue;
        }
    }
    return;
}
