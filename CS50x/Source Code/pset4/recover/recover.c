#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;


int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("command line argument error\n");
        return 1;
    }

    //open memory card

    FILE *mcfile = fopen(argv[1], "r");
    if (mcfile == NULL) //if(!ptr)
    {
        printf("forensic image cannot be opened\n");
        return 1;
    }

    int jpeg_count = 0; //see video for syntax format
    char name[] = "%03i.jpg";
    int x = 512;
    //int y = 512;

//repeat until end of card:
    while (x == 512)
    {
        //heap if you don't know exactly how much data you will need at runtime or if you need to allocate a lot of data.
        BYTE *buffer = malloc(512 * sizeof(BYTE));

        //read 512 bytes into a buffer.
        x = fread(buffer, sizeof(BYTE), 512, mcfile); //look and see

        //if start of new JPEG
        if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && ((buffer[3] & 0xf0) == 0xe0))
        {
            //if first JPEG
            if (jpeg_count == 0)
            {

                sprintf(name, "%03i.jpg", jpeg_count); //store the name of the file you are making (###.jpg) in a string variable called name
                jpeg_count++;
                FILE *img = fopen(name, "w");    //open filename ###.jpg //fopen creater file (as long as there is no existing file with its name.)
                if (img == NULL)
                {
                    printf("img file %s cannot be opened\n", name);
                    return 1;
                }

                //writes 512 bytes chunks into openned file
                fwrite(buffer, sizeof(BYTE), x, img);
                fclose(img);
            }
            else    //you already found first JPEG
            {
                //close file you're writing to
                sprintf(name, "%03i.jpg", jpeg_count);
                jpeg_count++;

                FILE *img = fopen(name, "w");       //open new file to write to.
                if (img == NULL)
                {
                    printf("img file %s cannot be opened\n", name);
                    return 1;
                }

                fwrite(buffer, sizeof(BYTE), x, img);
                fclose(img);
            }
        }
        else  //if not start of new JPEG
        {
            if (jpeg_count != 0)
            {
                FILE *img = fopen(name, "a");
                //keep writing already found JPEG
                fwrite(buffer, sizeof(BYTE), x, img);
                fclose(img);
            }
        }
        free(buffer);
    }
//reach end of memory card, close remaining files
    fclose(mcfile);
}