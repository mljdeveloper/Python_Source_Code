"""
Dunder Name and Dunder Main
Dunder Name  = __name__
Dunder Main = __main__

Em Python, são utilizados dunder para criar funções, atributos, propriedades e etc
utilizando Double Under para não gerar conflito com os nomes desses elementos
na programação

# Na linguagem C, temos um programa da seguinte forma:

int main(){

  return 0
}

# Na linguagem Java, temos um programa da seguinte forma:

public static void main(String[] args){

}

# Em Python, se executarmos um módulo Python diretamente na linha de comando, internamente
o Python atribuirá à variavel __name__ o valor __main__ indicando que este modulo
é o modulo de execução principal
"""

from funcos_com_parametros import soma_impares

import primeiro
import segundo


