#include <stdio.h>

/**
 * I decided to hate myself, and try this 100% in C for the easier bit manipulation.
 * ... I forgot how much I hated the low level part of C... 
 * I do like trying the bit manipulation part of it, instead of stringing it.
 */

int count = 1000;

int main(){

    // Only defining Gamma here. See later for the magic...
    unsigned int gamma = 0;

    int in[1000];

    FILE * file = fopen("day3.txt","r");
    char line[24];
    int curr = 0;
    while(fgets(line,24,file)){
        in[curr] = 0;
        for(int i=0;i<12;i++){
            in[curr] = (in[curr] << 1) + line[i] - '0';
        }
        curr++;
    }

    // Going from the MSB to the LSB
    for(int i=11;i>=0;i--){

        int count = 0;
        // Generating the mask
        int mask = 1 << i;

        for(int j=0;j<1000;j++){
            // mask the valid bit, shift bit into the unit position, and add to count (1 or 0)
            count += (in[j] & mask) >> i;
            if(count > 500){
                // quick escape
                break;
            }
        }
        // if the count is higher than half the size of the list, the bit is 1
        if(count > 500){
            gamma += mask;
        }
    }
    // A unique property of epsillon is that it is the NOT of gamma.
    // Please remember to mask out the unused bits, otherwise you will end up unhappy 
    unsigned int epsillon = ~gamma & ((1<<12) -1);

    // Get the final product
    unsigned long fuel = gamma * epsillon;
    printf("Gamma: %u, Epsillon: %u\n",gamma, epsillon);
    printf("Fuel Consumption: %u", fuel);
}