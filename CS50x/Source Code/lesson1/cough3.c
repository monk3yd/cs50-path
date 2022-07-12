#include <stdio.h>

void cough(int n); //prototype. copy/paste of first line of actual function


int main(void)
{
    cough(3);       //cough 3 times.
}

//make function of cough more versatile by coughing n number for times.
void cough(int n)
{
    for (int i = 0; i < n; i++)     //not hardcoded anymore. cough has been parameterized: it now takes input of integer called n, and it uses that input n a variable number of times n.
    {
        printf("cough\n");
    }
}