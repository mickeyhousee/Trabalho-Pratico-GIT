# Trabalho-Pratico-Git
Trabalho final prático de GIT

## Grilo

Incialmente Configurei o token para o projeto.
Depois adicionei as pastas principais do projeto e fiz commit para o github para a branch "main".

Criei a branch "Grilo" onde irei fazer as minhas alterações.

![alt text](assets/Grilo/grilo_branch.png)

### Merge

Começei por criar um script chamado  "script_grilo.py" que é um script para calcular a area de um triangulo.

![alt text](assets/Grilo/script_grilo.png)

Depois fiz git commit de todas as alterações e irei realizar o git merge para juntar a branch "Grilo" para o "main".
De seguida fiz o push para o github para a branch "main" 

![alt text](assets/Grilo/git_log.png)

![alt text](<assets/Grilo/git merge.png>)

### Cherry-pick e Tags

Primeiro fiz um commit onde alterei o README.md e depois fiz outro commit onde corrigi o bug do "script_grilo.py"

Adicionei tambem uma tag ao commit onde corri o bug onde meti "tag 1.0"

![alt text](assets/Grilo/tag.png)

Depois voltei para a branch main e fiz cherry-pick apenas do commit "Bug fix in script_grilo.py" 

![alt text](<assets/Grilo/git cherrypick.png>)