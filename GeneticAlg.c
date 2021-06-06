#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float Verifica_cross_prob(int *indv_3, int *cross_1, int *cross_2, float p, int n);

int main(){

    int rep, i, j, k, n, corte, *indv_1, *indv_2, *indv_3, *cross_1, *cross_2;
    float prob, prob_final;
    char *s;

    scanf("%d", &rep);

    for(k = 0; k<rep; k++){
        scanf("%d", &n);
        scanf("%d %f", &corte, &prob);

        indv_1 = malloc(n * sizeof(int));
        indv_2 = malloc(n * sizeof(int));
        indv_3 = malloc(n * sizeof(int));
        cross_1 = malloc(n * sizeof(int));
        cross_2 = malloc(n * sizeof(int));
        s = malloc(n * sizeof(char));

        scanf("%s", s);
        for(i = 0; i<n; i++){
            indv_1[i] = s[i] - '0';
        }
        scanf("%s", s);
        for(i = 0; i<n; i++){
            indv_2[i] = s[i] - '0';
        }
        scanf("%s", s);
        for(i = 0; i<n; i++){
            indv_3[i] = s[i] - '0';
        }

        for(i = 0; i<corte; i++){
            cross_1[i] = indv_1[i];
            cross_2[i] = indv_2[i];
        }
        for(j = corte; j<n; j++){
            cross_1[j] = indv_2[j];
            cross_2[j] = indv_1[j];
        }

        prob_final = Verifica_cross_prob(indv_3, cross_1, cross_2, prob, n);
        printf("%.7f", prob_final);
        free(indv_1);
        free(indv_2);
        free(indv_3);
        free(cross_1);
        free(cross_2);
        free(s);
    }

    return 0;
}

float Verifica_cross_prob(int *indv_3, int *cross_1, int *cross_2, float p, int n){
    float prob_1, prob_2, prob_erro;
    int count_1 = 0;
    int count_2 = 0;
    int i;

    for(i=0; i<n; i++){
        if(indv_3[i] != cross_1[i])
            count_1 += 1;
    }
    prob_1 = 1 * pow(p, count_1) * pow((1-p), (n - count_1));

    for(i=0; i<n; i++){
        if(indv_3[i] != cross_2[i])
            count_2 += 1;
    }
    prob_2 = 1 * pow(p, count_2) * pow((1-p), (n - count_2));

    prob_erro =  (1-prob_1) * (1-prob_2);
    return (1 - prob_erro);

}
