// Credit Problem using Luhn's Algorithm
#include <cs50.h>
#include <stdio.h>

void checksum(long value);

int main(void)
{
    long CardNum; // We were needed to use long here bcz int doesnt support above 10 digits of value
                  // apparently.
    do
    {
        CardNum = get_long("Number: ");
    }
    while (CardNum <= 0);
    checksum(CardNum);
}

// If the CardNum follows Luhn's algorithm and the final number ends with 0 then it is a valid
// number
void checksum(long value)
{
    // We must use modulus operator - % which will help us find remainder which we can use to check
    // each number by finding the remainder of 10^x. Lets declare digits from end We have to
    // basically do thing like this but more efficiently using a loop or else we will need tor right
    // lots of such statements - checksum(CardNum); int digit1 = CardNum%10; printf("%i\n", digit1);
    // int digit2 = ((CardNum%100)-CardNum%10)/10;
    // printf("%i\n", digit2);
    // int digit3 = ((CardNum%1000)-CardNum%100)/100;
    // printf("%i\n", digit3);
    // This is highly inefficent for large number but logic remains the same

    // We can use while loop or something similar to do this thing more efficiently and then we can
    // perhaps use value % 2 == 1 to check if its perhaps second to last and then multiply those
    // digits by 2 like in Codewithharry python problem
    int sum = 0;
    int position = 0;
    long OrignalValue = value; // To use this value when checking the type of card bcz the problem
                               // was it was updating the value which was then not able to check
                               // whether it's visa,mastercard,etc

    // forgot to use long here so it was giving error again.

    while (value > 0)
    {
        int digit = value % 10;

        // for digits starting from second-last
        if (position % 2 == 1)
        {
            digit = digit * 2;
            if (digit > 9)
            {
                digit = digit / 10 + digit % 10;
            }
        }
        sum += digit;
        value = value / 10;
        position++;
    }
    // Now we must determine the card company like whether it's american express, Visa , mastercard
    // or just INVALID
    int length = position; // check50 was throwing error bcz card length also matter like visa
                           // should be 13 or 15 digits only like those errors
    if (sum % 10 == 0)
    {
        // printf("VALID"); //For debugging
        long StartingDigits = OrignalValue; // To check the card number directly bcz it was getting
                                            // updated and was giving invalid again and again
        while (StartingDigits > 100)
        {
            StartingDigits = StartingDigits / 10;
        }
        if ((StartingDigits / 10 == 4) && (length == 13 || length == 16))
        {
            printf("VISA\n");
        }
        else if ((StartingDigits == 34 || StartingDigits == 37) && (length == 15))
        {
            printf("AMEX\n");
        }
        else if ((StartingDigits == 51 || StartingDigits == 52 || StartingDigits == 53 ||
                  StartingDigits == 54 || StartingDigits == 55) &&
                 (length == 16))
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

// Formatted using style50 and written by Prathamesh. Took about 2hrs to fully solve. watched lots
// of videos and googled some stuff
