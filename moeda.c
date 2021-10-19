#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int coin_toss()

int main(){
    int c;
    // set random seed
    srand(time(NULL));

    printf("Jogo da moeda \n");
    while (1)
    {
        printf("1- joga a moeda\n 0 - sair\n");
        // read from stdin
        scanf("%d", &c);

        switch(c){
            case 1:
                switch(coin_toss()){
                    case 0:
                        printf("\n cara \n");
                        break;
                    case 1:
                        printf("\n coroa \n");
                        break;
                }
                break;
            case 0:
                printf("saindo");
                return 0;
                break;
            default:
                printf("opcao invalida");
                return 0;
                break;
        }
    }    
    return 0;
}

int coin_toss(){

    // generate random number between 0 and 1
    double random_number = (double)rand() / (double)RAND_MAX;

    if (random_number < 0.5) return 0;
    else return 1;

}
