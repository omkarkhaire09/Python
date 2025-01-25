#include <stdio.h>
#include <string.h>

void calculateParityBits(char *codeword)
{
    codeword[0] = (codeword[2] + codeword[4] + codeword[6]) % 2 + '0';
    codeword[1] = (codeword[2] + codeword[5] + codeword[6]) % 2 + '0';
    codeword[3] = (codeword[4] + codeword[5] + codeword[6]) % 2 + '0';
}

void encodeHammingCode(char *data)
{
    char codeword[8];
    codeword[0] = '0';
    codeword[1] = '0';
    codeword[2] = data[0];
    codeword[3] = '0';
    codeword[4] = data[1];
    codeword[5] = data[2];
    codeword[6] = data[3];
    codeword[7] = '\0';
    calculateParityBits(codeword);
    printf("Encoded Hamming(7,4) codeword: %s\n", codeword);
}

void decodeHammingCode(char *received)
{
    int error_position = 0;
    int p1 = (received[2] - '0' + received[4] - '0' + received[6] - '0') % 2;
    int p2 = (received[2] - '0' + received[5] - '0' + received[6] - '0') % 2;
    int p3 = (received[4] - '0' + received[5] - '0' + received[6] - '0') % 2;
    error_position = p1 * 1 + p2 * 2 + p3 * 4;
    if (error_position == 0)
    {
        printf("No error detected.\n");
    }
    else
    {
        printf("Error detected at position: %d\n", error_position);
        if (received[error_position - 1] == '0')
            received[error_position - 1] = '1';
        else
            received[error_position - 1] = '0';
        printf("Corrected codeword: %s\n", received);
    }
    printf("Decoded data: ");
    printf("%c%c%c%c\n", received[2], received[4], received[5], received[6]);
}

int main()
{
    char data[5];
    printf("Enter 4 data bits: ");
    scanf("%s", data);
    encodeHammingCode(data);
    char received[8];
    strcpy(received, "0000000");
    printf("Enter received codeword (7 bits): ");
    scanf("%s", received);
    decodeHammingCode(received);
    return 0;
}
