S - Principio da Responsabilidade Única (SRP)
Um módulo deve ser especializado em um único assunto e possuir apenas uma única
responsabilidade dentro do seu software.

O - Principio Aberto/Fechado
Um artefato de software deve estar aberto para extensão, mas fechado para 
modificação.

L - Principio de Substituição de Liskov (LSP)
Objetos podem ser substituidos por seus subtipos sem que isso afete a
execução correta do programa.
Pode e deve ser substituido ao nivel da arquitetura. Um simples violação
de substituição, pode fazer com que a arquitetura de um sistema seja
poluída com uma quantidade significativa de mecanismos extras.

I - Princípio da Segregação de Interfaces (ISP)
Uma classe não deve ser forçada a implementar interfaces que ela não
utiliza. As interfaces devem ser segregadas em conjuntos menores e mais 
específicos de métodos.

D - Princípio da Inversão da Dependência (DIP)
Módulos de lato nível não devem depender diretamente dos módulos de
baixo nível.