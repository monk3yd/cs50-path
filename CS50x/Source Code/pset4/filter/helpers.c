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
            if (image[i][j].rgbtRed != image[i][j].rgbtGreen || image[i][j].rgbtRed != image[i][j].rgbtBlue
                || image[i][j].rgbtGreen != image[i][j].rgbtBlue)
            {
                //which value to set it? for lighter color lighter grey and viceversa
                int x = image[i][j].rgbtRed;
                int y = image[i][j].rgbtGreen;
                int z = image[i][j].rgbtBlue;

                //calculate color average value with the 3 colors.
                float average = (float)(x + y + z) / (float) 3;
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



//Reflect image horizontally
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
    
    //declare array with exactly the same memory of original grid
    RGBTRIPLE tmp[height][width];
    
    
    //get original grid
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float redcount = 0.0;
            float greencount = 0.0;
            float bluecount = 0.0;
            float counter = 0.0;
            
            //tmp[i][j] = image[i][j];
            
            //iterate through 3x3 grid, with i and j as reference
            for (int x = i - 1; x <= i + 1; x++)
            {
                for (int y = j - 1; y <= j + 1; y++)
                {
                    //check if each of the pixels in a 3x3 sub-grid are valid. if they are take RGB value from original pixel, add it to counter. 
                    if ((x >= 0 && x < height) && (y >= 0 && y < width))
                    {
                        redcount = redcount + image[x][y].rgbtRed;
                        greencount = greencount + image[x][y].rgbtGreen;
                        bluecount = bluecount + image[x][y].rgbtBlue;
                        counter++;          //counts how many diff pixels you have taken RGB values from
                    }
                }
            }
            //when finish iteration. pass average RGB values to copy of original pixels. you can't change original's value yet, you need it for calculating the rest.
            tmp[i][j].rgbtRed = round(redcount / counter);
            tmp[i][j].rgbtGreen = round(greencount / counter);
            tmp[i][j].rgbtBlue = round(bluecount / counter);
        }
    }
    
    //copy values of tmp to original pixel.
    for (int k = 0; k < height; k++)
    {
        for (int m = 0; m < width; m++)
        {
            image[k][m].rgbtRed = tmp[k][m].rgbtRed;
            image[k][m].rgbtGreen = tmp[k][m].rgbtGreen;
            image[k][m].rgbtBlue = tmp[k][m].rgbtBlue;
        }
    }
    return;
}