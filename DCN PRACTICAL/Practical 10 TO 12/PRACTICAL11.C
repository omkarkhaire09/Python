#include <stdio.h>
#include <string.h>

void xorOperation(char *data, int len, char *divisor, int m)
{
    for (int i = 0; i < m; i++)
    {
        data[i] = (data[i] == divisor[i]) ? '0' : '1';
    }
    for (int i = 1; i < len; i++)
    {
        data[i - 1] = data[i];
    }
}

void calculateCRC(char *data, int n, char *divisor, int m, char *remainder)
{
    char temp[n];
    strncpy(temp, data, n);
    for (int i = 0; i <= n - m; i++)
    {
        if (temp[i] == '1')
        {
            xorOperation(temp + i, m, divisor, m);
        }
    }
    strncpy(remainder, temp + n - m + 1, m - 1);
    remainder[m - 1] = '\0';
}

void appendCRC(char *data, int n, char *remainder, int m)
{
    for (int i = 0; i < m - 1; i++)
    {
        data[n + i] = remainder[i];
    }
    data[n + m - 1] = '\0';
}

int main()
{
    char data[100], divisor[100], remainder[100];
    int n, m;

    printf("Enter the data (binary): ");
    scanf("%s", data);
    printf("Enter the divisor (binary): ");
    scanf("%s", divisor);

    n = strlen(data);
    m = strlen(divisor);

    calculateCRC(data, n, divisor, m, remainder);
    appendCRC(data, n, remainder, m);

    printf("\nData after appending CRC: %s\n", data);

    char transmittedData[100];
    strcpy(transmittedData, data);

    int receivedLen = strlen(transmittedData);
    calculateCRC(transmittedData, receivedLen - m + 1, divisor, m, remainder);

    if (remainder[0] == '0')
    {
        printf("No error detected. CRC check passed!\n");
    }
    else
    {
        printf("Error detected in transmitted data.\n");
    }

    return 0;
}
