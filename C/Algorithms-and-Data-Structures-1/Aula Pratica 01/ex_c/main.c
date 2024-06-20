#include <stdio.h>
#include <stdlib.h>

/*Escreva um programa que recebe um operador aritm�tico
e dois operandos e calcule a opera��o indicada.
As opera��es poss�veis s�o soma(+), subtra��o(-),
multiplica��o(*)e divis�o(/).*/

int main()
{
    char op;
    float num1,num2;
    float resultado;
    printf("Digite um operador aritmetico: (+,-,*,/)\n");
    scanf("%c",&op);
    printf("Digite um numero:");
    setbuf(stdin,NULL);
    scanf("%f",&num1);
    printf("Digite outro numero:");
    scanf("%f",&num2);
    switch (op){
        case '+':
            resultado = num1 + num2;
            break;
        case '-':
            resultado =  num1 - num2;
            break;
        case '*':
            resultado = num1 * num2;
            break;
        case '/':
            if(num2 == 0){
                printf("Impossivel realizar operacao!");
                return 0;
            }
            resultado = num1 / num2;
            break;
        default:
            printf("Operador aritmetico desconhecido!");
            return 0;
    }
    printf("O resultado da operacao eh: %.2f",resultado);
    return 0;
}
