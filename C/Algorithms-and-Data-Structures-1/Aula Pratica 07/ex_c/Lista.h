
typedef struct aluno{
    int mat;
    char nome[30];
    float n1;
}Aluno;

typedef struct lista Lista;

Lista *criar(int num);

void limpar(Lista *l);

int inserirInicio(Lista *l, Aluno it,int num);
int inserirFim(Lista *l, Aluno it, int num);
int inserirPosicao(Lista *l, Aluno it, int pos);

int removerInicio(Lista *l);
int removerFim(Lista *l);
int removerPosicao(Lista *l, int pos);
int removerItem(Lista *l, Aluno it);

int buscarItemChave(Lista *l, int chave, Aluno *retorno);
int buscarPosicao(Lista *l, int posicao, Aluno *it);

int listaVazia(Lista *l);
int listaCheia(Lista *l,int num);

int tamanho(Lista *l);

void mostrar(Lista *l);

int ContemItem(Lista *l, int num);

Lista *reversa(Lista *l,int num);

int contaItem(Lista *l, int num);