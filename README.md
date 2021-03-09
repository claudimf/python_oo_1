# Orientação a Objetos com Python

👋 Olá, Seja Bem-vindo(a) ao 'Orientação a Objetos com Python'.

# Projeto 'Orientação a Objetos com Python' do curso:

## [Python 3: Introdução a Orientação a objetos](https://cursos.alura.com.br/course/python-3-intro-orientacao-objetos)

### Aulas

<details>
    <summary>O problema do paradigma procedural Ver primeiro vídeo</summary>
    <ul>
        <li>Introdução ao curso</li>
        <li>Dados da conta</li>
        <li>Dados e comportamento</li>
        <li>O paradigma OO</li>
        <li>Procedural ou OO?</li>
        <li>Boas-vindas?</li>
        <li>Mãos na massa: Primeiros passos do projeto</li>
        <li>O que aprendemos?</li>
        <li>Arquivos do projeto atual</li>
    </ul>
</details>

<details>
    <summary>Classes e Objetos</summary>
    <ul>
        <li>Classe e Objeto</li>
        <li>Definindo uma classe</li>
        <li>Construtor</li>
        <li>Características de uma classe</li>
        <li>Definindo valores para os atributos da classe Conta</li>
        <li>Para saber mais: construtores com valores padrão</li>
        <li>Acessando atributos</li>
        <li>Mãos na massa: Criando a classe Conta</li>
        <li>O que aprendemos?</li>
        <li>Arquivos do projeto atual</li>
    </ul>
</details>

<details>
    <summary>Implementando Métodos</summary>
    <ul>
        <li>Usando métodos</li>
        <li>O problema de Chalita</li>
        <li>Melhoria necessária</li>
        <li>Revisão do conteúdo</li>
        <li>None e Coletor de lixo</li>
        <li>Resultado final</li>
        <li>Especificando uma classe</li>
        <li>Mãos na massa: Definindo o comportamento da classe</li>
        <li>Desafio Opcional</li>
        <li>O que aprendemos?</li>
        <li>Arquivos do projeto atual</li>
    </ul>
</details>

<details>
    <summary>Encapsulamento</summary>
    <ul>
        <li>Atributos privados</li>
        <li>Atributo __</li>
        <li>A classe Retangulo e encapsulamento</li>
        <li>Encapsulamento</li>
        <li>Coesão</li>
        <li>Quais vantagens?</li>
        <li>Mãos na massa: Atributos privados e transferência de valores entre contas</li>
        <li>Para saber mais: SOLID</li>
        <li>O que aprendemos?</li>
        <li>Arquivos do projeto atual</li>
    </ul>
</details>

<details>
    <summary>Usando Propriedades</summary>
    <ul>
        <li>Getters e Setters</li>
        <li>Acesso a atributos privados</li>
        <li>Alterando atributos privados</li>
        <li>Propriedades</li>
        <li>Melhorando o acesso aos atributos</li>
        <li>Melhorando a alteração de atributos</li>
        <li>Mãos na massa: Criando getters e setters</li>
        <li>Mãos na massa: Criando propriedades</li>
        <li>O que aprendemos?</li>
        <li>Arquivos do projeto atual</li>
    </ul>
</details>

<details>
    <summary>Métodos privados e estáticos</summary>
    <ul>
        <li>Métodos privados</li>
        <li>O desenvolvedor inspirado</li>
        <li>Membros privados</li>
        <li>Métodos da classe</li>
        <li>Sintaxe para métodos privados</li>
        <li>Chamar método estático</li>
        <li>Quando usar método estáticos?</li>
        <li>Python OO vs Java OO</li>
        <li>Mãos na massa: Verificando o saque e métodos estáticos</li>
        <li>Revisão e Conclusão do curso</li>
        <li>Para saber mais: Atributo estático</li>
        <li>O que aprendemos?</li>
        <li>E agora?</li>
        <li>Arquivos do projeto atual</li>
    </ul>
</details>

# Notas das aulas:

Para executar um script python, faça conforme o exemplo abaixo:
```sh
docker-compose run --rm app python aulas/01.py
```
Ou com muito subníveis, exemplo:
```sh
docker-compose run --rm app python aulas/02/teste.py
```

## Sobre o projeto:

### Permissões de arquivos:

Ao se criar migrações, adicionar libs ou qualquer outro comando que crie arquivos dentro do contâiner Docker o proprietário para edição se torna o contâiner, sendo assim você precisará rodar o comando abaixo para alterar essas permissões e você poder editar:

```sh
sudo chown -R $USER:$USER .
```

# Exigências

**:warning: Atenção:** É necessário que os desenvolvedores usem o Docker no seu ambiente de desenvolvimento.

- **🛠 Modo Desenvolvimento Docker**
    - :computer: [Linux Ubuntu LTS](https://ubuntu.com/download/desktop)
    - 🐳 [Docker](https://docs.docker.com/engine/installation/) Deve estar instalado.
    - 🐳 [Docker Compose](https://docs.docker.com/compose/) Deve estar instalado.
    - **💡 Dica:** [Documentação do Docker](https://docs.docker.com/)

# Instalando

## 🐳 Modo Desenvolvimento com Docker

Após instalar o docker e docker-compose, estando na pasta raiz do projeto, execute:

```sh
docker-compose up
```

Para se certificar que os seus containers subiram corretamente, todos os containers deve estar com o status `UP`, execute:

```sh
docker-compose ps -a
```

Para acessar o container da aplicação, execute:

```sh
docker-compose run --rm app bash
```

Para derrubar e subir a instância do docker novamente, execute:

```sh
docker-compose down && docker-compose up
```

# Referências utilizadas

[1° Conteinerização de scripts em Python](https://github.com/claudimf/containerized_python)

[2° Exemplos de formatação de strings](https://docs.python.org/3/library/string.html#formatexamples)

[3° Built-in Functions](https://docs.python.org/3/library/functions.html)

[4° Garbage Collection in Python](https://www.geeksforgeeks.org/garbage-collection-python/)

[5° Library Garbage Collector](https://docs.python.org/3/library/gc.html)

[6° Using Garbage Collector](https://pymotw.com/2/gc/)