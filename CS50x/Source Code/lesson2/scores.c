#include <cs50.h>
#include <stdio.h>

//D. default working. BEST DESIGNED.
//Hardcode variable you don't want to change.
const int N = 3; // global variable

int main(void)
{

    int scores[N];
    scores[0] = 72;
    scores[1] = 73;
    scores[2] = 33;

    printf("Average: %i\n", (scores[0] + scores[1] + scores[2]) / N);


//A. dangerously close to just copying and pasting the same code again and again.

    //int score1 = 72;
    //int score2 = 73;
    //int score3 = 33;

    //printf("Average: %i\n", (score1 + score2 + score3) / 3 );

//both codes are equivalent (giving me three variables)
//B. opportunity for better design.

    //int scores[3];  //this tells de computer "give me enough memory for three integer values in one variable named scores".
    //scores[0] = 72; //arrays are 0 index.
    //scores[1] = 73;
    //scores[2] = 33;

    //printf("Average: %i\n", (scores[0] + scores[1] + scores[2]) / 3);

//C. a little bit better down here

    //int n = 3; //we can have variables that just have numbers.
    //int scores[n];
    //scores[0] = 72;
    //scores[1] = 73;
    //scores[2] = 33;

    //printf("Average: %i\n", (scores[0] + scores[1] + scores[2]) / n);

//even though still it can be better designed. FIRST EXAMPLE.

}