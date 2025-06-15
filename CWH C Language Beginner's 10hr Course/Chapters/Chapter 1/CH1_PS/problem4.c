// Write a program to calculate simple interest using principal, rate of interest, years

#include <stdio.h>

int main(){
    float interest,principal,years,simple_interest;
    printf("Enter the Principal Value: ");
    scanf("%f",&principal);
    printf("Enter the Interest rate in \%: ");
    scanf("%f",&interest);
    printf("Enter the Number of years: ");
    scanf("%f",&years);
    simple_interest = (interest*principal*years)/100;
    printf("The simple interest for the following terms is %f\n", simple_interest);
    return 0;
}