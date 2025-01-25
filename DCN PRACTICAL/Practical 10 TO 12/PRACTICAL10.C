#include <stdio.h>
#include <string.h>

void checkParity(char *data, char parityType)
{
    int count = 0;
    for (int i = 0; i < strlen(data); i++)
    {
        if (data[i] == '1')
        {
            count++;
        }
    }
    if (parityType == 'e')
    {
        if (count % 2 == 0)
        {
            printf("No error detected (Even Parity).\n");
        }
        else
        {
            printf("Error detected (Even Parity).\n");
        }
    }
    else if (parityType == 'o')
    {
        if (count % 2 != 0)
        {
            printf("No error detected (Odd Parity).\n");
        }
        else
        {
            printf("Error detected (Odd Parity).\n");
        }
    }
    else
    {
        printf("Invalid parity type selected.\n");
    }
}

int main()
{
    char data[100];
    char parityType;
    printf("Enter the data (binary): ");
    scanf("%s", data);
    printf("Enter the parity type (e for even, o for odd): ");
    scanf(" %c", &parityType);
    checkParity(data, parityType);
    return 0;
}
