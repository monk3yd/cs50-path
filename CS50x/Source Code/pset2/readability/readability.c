#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

const int X = 1;

int main(int argc, string argv[])
{
    //prompt text from user.
    string text = get_string("Text: ");

    int letters = 0;
    int words = 0 + X;
    int sentences = 0;

    //iterate through texts length for counting letters.
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if ((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z'))
        {
            letters++;
            //printf("%c", text[i]);
        }
        else if (text[i] == ' ') // bug if double space is typed. fix it later.
        {
            words++;
        }
        else if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
    }

    float x = 0.0588;
    float y = 0.296;

// index = 0.0588 * L - 0.296 * S - 15.8
// L is the average number of letters per 100 words in the text.
// S is the average number of sentences per 100 words in the text.

    float index = x * (100 * (float) letters / (float) words) - y * (100 * (float) sentences / (float) words) - 15.8;

    index = roundf(index);
    //print output
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %.0f\n", index);
    }
    //printf("%i letter(s), %i word(s), %i sentence(s)\n", letters, words, sentences);
}