
# Documentação do Sistema: VirtuaLTD

## Dados do Cliente

**Projeto:** VirtuaLTD: Uma plataforma de gerenciamento de projetos do Laboratório de Transformação Digital da UniMetrocamp  
**Cliente:** Kesede Rodrigues Julio  
**CNPJ/CPF:** 061.962.968-17  
**Contato:** profkesede64@gmail.com

## Equipe de Desenvolvimento

| Nome                         | Curso                          | Disciplina                                |
|-----------------------------|--------------------------------|-------------------------------------------|
| Giovanni Garcia de Souza    | Ciência da Computação          | Program. Orientada a Objetos em JAVA      |
| Camila Marinho Dourado      | Ciência da Computação          | Program. Orientada a Objetos em JAVA      |
| Victor Ronqui de Souza      | Ciência da Computação          | Program. Orientada a Objetos em JAVA      |
| Gustavo Yan Gonçalves Tavares | Análise e Desenv. de Sistemas | Program. Orientada a Objetos em JAVA      |

**Professor Orientador:** Kesede Rodrigues Julio


## 1. Introdução

O professor Kesede Rodrigues Julio, criador do LTD, solicitou o desenvolvimento de um sistema para gerenciar os projetos e atividades do Laboratório de Transformação Digital da UniMetrocamp. A aplicação deverá conter banco de dados de projetos, calendário interativo, sistema de login com diferentes acessos e interface web.


## 2. Objetivo

Desenvolver uma plataforma que centralize a gestão dos projetos do LTD, melhore a comunicação entre participantes e otimize processos como cadastro de projetos, calendário e gestão de usuários.


## 3. Escopo

- Banco de dados de projetos (em andamento e finalizados)  
- Calendário interativo (edição apenas pelo coordenador)  
- Login com diferentes perfis (cliente, dev, coordenador)  
- Interface provisória funcional


## 4. Backlogs do Produto

- **Banco de dados:** separação entre projetos em andamento e finalizados  
- **Calendário:** apenas o coordenador pode editar  
- **Login:** área exclusiva por tipo de usuário  
- **Interface:** protótipo funcional


## 5. Cronograma

| Atividades                                              | Início        | Término      | Descrição                                                                 |
|----------------------------------------------------------|---------------|--------------|---------------------------------------------------------------------------|
| Divisão de times, decisão tema de projeto e cliente      | 15/02/2025    | 20/03/2025   | Organização inicial dos grupos e escolha do tema e cliente parceiro      |
| Criação de repositório e iniciação ao Jira               | 22/03/2025    | 05/04/2025   | Configuração do ambiente e ferramenta de gestão ágil                     |
| Divisão de papéis (Scrum, Git, funções do time)          | 29/03/2025    | 05/04/2025   | Separação de atividades e definições de projetos                         |
| Inicialização Frontend                                   | 08/04/2025    | 19/04/2025   | Criação inicial das telas com HTML, CSS e estrutura base                 |
| Definição e padronização HTML e CSS                      | 22/04/2025    | 06/05/2025   | Aplicação de estilos padronizados e semântica do código                  |
| Banco de Dados                                           | 22/04/2025    | 05/05/2025   | Estruturação do banco relacional, tabelas e scripts de dados             |
| Testes funcionais e ajustes finais                       | 03/05/2025    | 24/05/2025   | Conexão entre interface e back-end                                       |
| Integração front-end com banco de dados                  | 05/05/2025    | 15/05/2025   | Validação do sistema, identificação e correção de bugs                   |
| Apresentação                                             | 05/06/2025    | 05/06/2025   | Apresentação final                                                       |


## 6. Materiais e Métodos

### Tecnologias Utilizadas

- **Backend:** Python + Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **Banco de Dados:** SQLite

### Modelagem

- Diagrama de caso de uso  
- Modelo Entidade-Relacionamento (MER)

### Estrutura de Código

- Cadastro e login com criptografia SHA256  
- Controle de permissões por tipo de usuário  
- Código para inserção de projetos e pessoas no banco


## 7. Resultados

### Protótipos das Telas

- Tela de login  
- Tela de cadastro  
- Tela inicial com menu e informações da universidade  
- Calendário com agendamentos  
- Projetos anteriores  
- Cadastro de novos projetos (acesso do coordenador)

### Exemplos de Código

- Integração com Google Calendar via `<iframe>`  
- Inserção de projetos e participantes no banco SQLite via Python  
- Criação de usuários e autenticação com hash SHA256


## 8. Conclusão

A plataforma VirtuaLTD melhorou a organização dos projetos do LTD, promoveu colaboração entre alunos e professores e facilitou o acesso às informações.

### Melhorias Futuras

- Integração com SAVA e SIA  
- Recuperação de senha via e-mail


## 9. Homologação do MVP junto ao Cliente

MVP foi apresentado e aprovado pelo cliente em reunião com os desenvolvedores.  
**Participantes:** Kesede Rodrigues, Camila Marinho, Gustavo Yan, Victor Ronqui


## 10. Divulgação

- Apresentação no LinkedIn  
- Seminário de Projetos de Software (vídeo + fotos)  
- FENETEC - Feira de Negócios em Tecnologia (vídeo e fotos previstos)


## 11. Carta de Apresentação

Apresentação formal do grupo de alunos e objetivos do projeto como parte da disciplina ARA0075, sob orientação do Prof. Kesede.


## 12. Carta de Autorização

Autorizada por Kesede Rodrigues Julio para atividades de levantamento de requisitos e desenvolvimento com os seguintes alunos:

- Camila Marinho Dourado  
- Gustavo Yan Gonçalves Tavares  
- Giovanni Garcia de Souza  
- Victor Ronqui de Souza


## 13. Relato Individual do Processo

Cada integrante do time compartilha a seguir suas experiências e aprendizados durante o desenvolvimento do projeto **VirtuaLTD**.

**Camila Marinho Dourado**

> A participação neste projeto representou uma vivência enriquecedora, tanto no âmbito acadêmico quanto profissional. Trata-se de uma jornada repleta de aprendizados, na qual fui constantemente desafiada a sair da zona de conforto e a desenvolver competências essenciais para minha formação. Ao longo das diversas fases do desenvolvimento, enfrentei situações inéditas que demandaram o uso de tecnologias até então desconhecidas para mim. Esse contexto me motivou a pesquisar, entender novas ferramentas e aplicá-las de forma prática na resolução de demandas concretas. A cada obstáculo superado, ampliei minha capacidade de diagnóstico, tomada de decisão e adaptação frente aos objetivos do grupo e às necessidades dos usuários. Sobretudo, considero que esse trabalho foi decisivo para fortalecer minha postura autônoma, minha persistência diante de adversidades e minha habilidade de refletir criticamente sobre os processos. Tive a oportunidade de exercitar a escuta ativa, o trabalho colaborativo e a clareza na troca de informações com a equipe, fatores indispensáveis para a fluidez e o sucesso das entregas.

**Gustavo Yan Gonçalves Tavares**

>A participação no projeto contribuiu de forma significativa para o aprimoramento de habilidades técnicas, me permitindo explorar novas ferramentas e aprofundar meus conhecimentos na área de desenvolvimento de software. Um dos principais avanços foi na compreensão dos conceitos e aplicações de banco de dados, o que favoreceu uma visão mais clara sobre a estruturação e o gerenciamento de informações em sistemas reais. Além disso, o projeto possibilitou uma reflexão sobre seu potencial de impacto, tanto no ambiente acadêmico quanto no profissional, evidenciando como iniciativas práticas podem agregar valor ao processo de aprendizagem e contribuir para a formação integral do estudante.

**Giovanni Garcia de Souza**

>Participar deste projeto foi muito interessante, pois descobri que o que pensava ser fácil era mais difícil do que parecia. Percebi a importância de uma boa organização e da divisão de tarefas para estudar e executar o projeto de forma eficiente. Apesar dos desafios, evoluí bastante em programação e aprendi coisas novas que não conhecia. A apresentação final também foi marcante, pois me fez refletir sobre como me comunicar melhor em público e buscar aprimorar minha postura profissional.

**Victor Ronqui de Souza**

> A realização deste projeto representou não apenas uma oportunidade de aprendizado acadêmico, mas também uma imersão significativa no universo profissional. Ao longo do desenvolvimento, tive contato com ferramentas e práticas amplamente utilizadas no mercado de trabalho, o que me permitiu compreender melhor os padrões de exigência e organização presentes no ambiente corporativo. Enfrentamos diversos desafios técnicos e operacionais, que exigiram comprometimento, planejamento e colaboração entre os membros da equipe. Cada obstáculo superado fortaleceu nossa capacidade de trabalhar em grupo, tomar decisões estratégicas e buscar soluções eficientes e criativas para os problemas apresentados. Além disso, vivenciei na prática a importância da divisão de tarefas, da escuta ativa e da construção coletiva, elementos essenciais para o sucesso de qualquer projeto em equipe. Ao final, a concretização do sistema e a entrega das funcionalidades propostas resultaram em uma grande satisfação pessoal e profissional.
