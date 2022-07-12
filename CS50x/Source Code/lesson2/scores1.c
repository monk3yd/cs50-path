#include <cs50.h>
#include <stdio.h>

float average(int length, int array[]); //prototype

int main(void)
{
//E. add suggestion that we do this dynamically,, using arrays.

    int n = get_int("Number of scores: ");  //prompt for input

    int scores[n];  //give myself an array of size n

    for (int i = 0; i < n; i++)
    {
//operator just makes the program to tell the human the score it wants from them.
        scores[i] = get_int("Score %i: ", i + 1); // + 1 is just aesthetics for prompt.
    }
//how to compute the average in a way thats dynamic?
//call function average and give inputs: length of the array (n). name of the array (scores)
    printf("Average: %.1f\n", average(n, scores));

//you could but don't. nested is better.
    //float avg = average(n, scores);
    //printf("Average: %f\n", avg);
}

//F. function called average.
//if i want to average the numbers the human typed in, we need to know
//the length of the array that they've been accumulating and the array itself (in this case named array).
float average(int length, int array[])
{
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += array[i]; //sum = sum + array[i];
    }
    return (float) sum /(float) length; //you're dividing int/int. math bug, you want to see youre fraction part.
                //FIX cast float. only one is necesarry but for consistency we cast both.
}