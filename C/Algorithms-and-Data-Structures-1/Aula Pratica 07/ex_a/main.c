#include <stdio.h>
#include <stdlib.h>
#include "Lista.h"

typedef struct lista
{
    int total;
    Aluno valores[MAX];
} Lista;

Lista *criar(){
    Lista *l = (Lista *)malloc(sizeof(Lista));
    if (l != NULL)
        l->total = 0;
    return l;
}

void limpar(Lista *l){
    if (l != NULL)
        l->total = 0;
}

int inserirInicio(Lista *l, Aluno it){
    int i;
    if (l == NULL)
        return 2;
    if (listaCheia(l) == 0)
        return 1;
    for (i = l->total; i > 0; i--)
    {
        l->valores[i] = l->valores[i - 1];
    }
    l->valores[0] = it;
    l->total++;
    return 0;
}

int inserirFim(Lista *l, Aluno it){
    if (l == NULL)
        return 2;
    if (listaCheia(l) == 0)
        return 1;
    l->valores[l->total] = it;
    l->total++;
    return 0;
}

int buscarItemChave(Lista *l, int chave, Aluno *retorno){
    int i;
    if (l == NULL)
        return 2;
    if (listaVazia(l) == 0)
        return 1;
    for (i = 0; i < l->total; i++)
        if (l->valores[i].mat == chave)
        {
            *retorno = l->valores[i];
            return 0;
        }
    return -1;
}

int listaVazia(Lista *l){
    if (l == NULL)
        return 2;
    if (l->total == 0)
        return 0;
    else
        return 1;
}

int removerInicio(Lista *l){
    int i;
    if (l == NULL)
        return 2;
    if (listaVazia(l) == 0)
        return 1;
    for (i = 0; i < l->total - 1; i++)
        l->valores[i] = l->valores[i + 1];
    l->total--;
    return 0;
}

int removerFim(Lista *l){
    if (l == NULL)
        return 2;
    if (listaVazia(l) == 0)
        return 1;
    l->total--;
    return 0;
}

int listaCheia(Lista *l){
    if (l == NULL)
        return 2;
    if (l->total == MAX)
        return 0;
    else
        return 1;
}

void mostrar(Lista *l){
    int i;
    if (l != NULL)
    {
        printf("[");
        for (i = 0; i < l->total; i++)
        {
            printf(" {%d, ", l->valores[i].mat);
            printf("%s, ", l->valores[i].nome);
            printf("%.2f} ", l->valores[i].n1);
        }
        printf("]\n");
    }
}

int inserirPosicao(Lista *l, Aluno it, int pos){
    if(l == NULL) return 1;
    if(pos > l->total || pos < 0) return 2;
    else{
        l->valores[pos] = it;
        return 0;
    }
}

int removerPosicao(Lista *l, int pos){
    int i;
    if(l == NULL) return 1;
    if(pos > l->total || pos < 0) return 2;
    if(listaVazia(l) == 0) return 3;
    else{
        for(i = pos;i < l->total;i++){
            l->valores[i] =  l->valores[i+1];
        }
        l->total--;
        return 0;
    }
}

int removerItem(Lista *l, Aluno it){
    int i,j;
    if(l == NULL) return 1;
    if(listaVazia(l) == 0) return 2;
    else{
        for(i = 0;i < l->total;i++){
            if(l->valores[i].mat == it.mat){
                for(j = i; j < l->total;j++){
                    l->valores[j] = l->valores[j+1];
                }
                l->total--;
                i--;
            }
        }
        return 0;
    }
}

int buscarPosicao(Lista *l, int posicao, Aluno *it){
    int i,j;
    if(l == NULL) return 1;
    if(listaVazia(l) == 0) return 2;
    if(posicao > l->total || posicao < 0) return 3;
    else{
        *it = l->valores[posicao];
    }
}

int main(){
    Lista *l;
    Aluno *it;
    int op,op2;
    int pos,retorno,mat;
    do{
        printf("Digite um opcao:\n");
        printf("1 - Criar\t\n2 - Inserir\t\n3 - Remover\t\n4 - Buscar\t\n5 - Mostrar\t\n0 - Sair\n");
        setbuf(stdin,NULL);
        scanf("%d",&op);
        if(op == 1){//criar
            l = criar();
            printf("Lista criada!\n");
        }
        if(op == 2){//inserir
            do{
            printf("Digite um opcao:\n");
            printf("1 - Inicio\t\n2 - Fim\t\n3 - Posicao\t\n 5 - Sair\n");
            setbuf(stdin,NULL);
            scanf("%d",&op2);
            if(op2 == 1){
                it = (Aluno *) malloc(sizeof(Aluno));
                printf("Digite a matricula do aluno:");
                setbuf(stdin,NULL);
                scanf("%d",&it->mat);
                printf("Digite o nome do aluno:");
                setbuf(stdin,NULL);
                fgets(it->nome,30,stdin);
                printf("Digite a nota do aluno:");
                setbuf(stdin,NULL);
                scanf("%f",&it->n1);
                retorno = inserirInicio(l,*it);
                free(it);
                if(retorno == 2){
                    printf("Lsita nao foi criada!\n");
                }
                if(retorno == 1){
                    printf("lista cheia!\n");
                }
                if(retorno == 0){
                    printf("Inserido com sucesso!\n");
                }
            }
            if(op2 == 2){
                it = (Aluno *) malloc(sizeof(Aluno));
                printf("Digite a matricula do aluno:");
                setbuf(stdin,NULL);
                scanf("%d",&it->mat);
                printf("Digite o nome do aluno:");
                setbuf(stdin,NULL);
                fgets(it->nome,30,stdin);
                printf("Digite a nota do aluno:");
                setbuf(stdin,NULL);
                scanf("%f",&it->n1);
                inserirFim(l,*it);
                free(it);
                if(retorno == 2){
                    printf("Lsita nao foi criada!\n");
                }
                if(retorno == 1){
                    printf("lista cheia!\n");
                }
                if(retorno == 0){
                    printf("Inserido com sucesso!\n");
                }
            }
            if(op2 == 3){
                it = (Aluno *) malloc(sizeof(Aluno));
                printf("Digite a matricula do aluno:");
                setbuf(stdin,NULL);
                scanf("%d",&it->mat);
                printf("Digite o nome do aluno:");
                setbuf(stdin,NULL);
                fgets(it->nome,30,stdin);
                printf("Digite a nota do aluno:");
                setbuf(stdin,NULL);
                scanf("%f",&it->n1);
                printf("Digite a posicao:");
                setbuf(stdin,NULL);
                scanf("%d",&pos);
                inserirPosicao(l,*it,pos);
                free(it);
                if(retorno == 1){
                    printf("Lsita nao foi criada!\n");
                }
                if(retorno == 2){
                    printf("Posicao invalida!\n");
                }
                if(retorno == 0){
                    printf("Inserido com sucesso!\n");
                }
            }
            }while(op2 != 5);       
        }
        if(op == 3){//remover
            do{
                printf("Digite uma opcao:\n");
                printf("1 - Inicio\t\n2 - Fim\t\n3 - Posicao\t\n4 - Item\t\n 5 - Sair\n");
                setbuf(stdin,NULL);
                scanf("%d",&op2);
                if(op2 == 1){
                    retorno = removerInicio(l);
                    if(retorno == 1){
                        printf("Lista vazia!\n");
                    }
                    if(retorno == 2){
                        printf("Lista nao existe!\n");
                    }
                    if(retorno == 0){
                        printf("Aluno inicial removido!\n");
                    }
                }
                if(op2 == 2){
                    retorno = removerFim(l);
                    if(retorno == 1){
                        printf("Lista vazia!\n");
                    }
                    if(retorno == 2){
                        printf("Lista nao existe!\n");
                    }
                    if(retorno == 0){
                        printf("Aluno final removido!\n");
                    }
                }
                if(op2 == 3){
                    printf("Digite a posicao:");
                    setbuf(stdin,NULL);
                    scanf("%d",&pos);
                    retorno = removerPosicao(l,pos);
                    if(retorno == 3){
                        printf("Lista vazia!\n");
                    }
                    if(retorno == 2){
                        printf("Posicao invalida!\n");
                    }
                    if(retorno == 1){
                        printf("Lista nao existe!\n");
                    }
                    if(retorno == 0){
                        printf("Aluno da posicao %d removido!\n",pos);
                    }
                }
                if(op2 == 4){
                    it = (Aluno *) malloc(sizeof(Aluno));
                    printf("Digite a matricula do aluno:");
                    setbuf(stdin,NULL);
                    scanf("%d",&it->mat);
                    removerItem(l,*it);
                    free(it);
                }
            }while(op2 != 5);
        }
        if(op == 4){//Buscar
            do{
            printf("Digite um opcao:\n");
            printf("1 - Item Chave\t\n2 - Posicao\t\n3 - Sair\n");
            setbuf(stdin,NULL);
            scanf("%d",&op2);
            if(op2 == 1){
                printf("Digite a matricula:");
                scanf("%d",&mat);
                it = (Aluno *) malloc(sizeof(Aluno));
                retorno = buscarItemChave(l,mat,it);
                if(retorno == 1){
                    printf("Lista vazia!\n");
                }
                if(retorno == 2){
                    printf("Lista nao existe!");
                }
                if(retorno == 0){
                    printf("Aluno encontrado:\n");
                    printf("Matricula: %d\n",it->mat);
                    printf("Nome: %s\n",it->nome);
                    printf("Nota: %f\n",it->n1);
                }
                free(it);
            }
            if(op2 == 2){
                printf("Digite uma posicao:");
                setbuf(stdin,NULL);
                scanf("%d",&pos);
                it = (Aluno *) malloc(sizeof(Aluno));
                retorno = buscarPosicao(l,pos,it);
                if(retorno == 1){
                    printf("Lista nao exite!\n");
                }
                if(retorno == 2){
                    printf("Lista vazia!\n");
                }
                if(retorno == 3){
                    printf("Posicao invalida!\n");
                }
                if(retorno == 0){
                    printf("Aluno encontrado:\n");
                    printf("Matricula: %d\n",it->mat);
                    printf("Nome: %s\n",it->nome);
                    printf("Nota: %f\n",it->n1);
                }
                free(it);
            }
            }while(op2 != 3);
        }
        if(op == 5){//Mostrar
            mostrar(l);
        }
    }while(op != 0);
}