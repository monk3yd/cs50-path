//Learn to implement your own function.
//e.g of functions: printf(""); get_int(""); get_string(""); get_float("");

#include <stdio.h>

void cough(void);            //anticipation for C to look at the end of the program for the function.


int main(void)  //this is your main function. Human convention says to generally have the main function at the top of your file.
{
    for (int i = 0; i < 3; i++)
    {
        cough();        //use custom function cough
    }
    
}

//implementation of your own custom function cough
void cough(void)
{
    printf("cough\n");
}