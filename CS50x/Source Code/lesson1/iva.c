//calcula el iva pagado del monto total ingresado en CLP.
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    float total = get_float("What's the total?\n");
    printf("You paid %.0f\n", total * 0.19);
}
