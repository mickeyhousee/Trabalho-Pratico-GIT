# Trabalho-Pratico-Git
Trabalho final prático de GIT


# Indice
- [Objetivos](#Objetivos)
- [Grilo](#Grilo)
- [Abreu](#Abreu)

# Objetivos
Operações essenciais do Git/GitHub:

- Clone
- Branch
- Commit
- Merge
- Rebase
- Cherry-pick
- Tags
- Pulls
- Pull requests
- Resolução de conflitos

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

### Rebase
Entrei na branch Grilo fiz as alterações ao README.md.

Primeiro fiz um commit onde alterei o README.md, depois voltei a branch main e fiz o rebase.
Basicamente o rebase server para fazer com que os commits "pareçam que venham da branch main" e não da branch Grilo

![alt text](assets/Grilo/rebase.png)

### Cherry-pick e Tags

Primeiro fiz um commit onde alterei o README.md e depois fiz outro commit onde corrigi o bug do "script_grilo.py"

Adicionei tambem uma tag ao commit onde corri o bug onde meti "tag 1.0"

![alt text](assets/Grilo/tag.png)

Depois voltei para a branch main e fiz cherry-pick apenas do commit "Bug fix in script_grilo.py" 

![alt text](<assets/Grilo/git cherrypick.png>)

## Abreu

Inicialmente criei um script em python em que o erro se situa na linha 6 em que o numero2 está registado como 0, sendo impossivel a divisão.

![alt text](assets/Abreu/img_script_abreu.png)

De seguida criei uma branch, nomeadamente "branch_abreu" onde vou começar a trabalhar.

![alt text](assets/Abreu/img_branch_abreu.png)

Dei git merge para juntar a branch "abreu_branch" para o main".

![alt text](assets/Abreu/img_merge_abreu.png)

Corrigi o script 

![alt text](assets/Abreu/script_corrigido.png)

Vou criar este texto de modo a mudar o conteúdo do ficheiro e fazer o primeiro commit para dar inicio ao cherry pick

![alt text](assets/Abreu/primeiro_commit.png)

Śegundo commit

![alt text](assets/Abreu/segundo_commit.png)

De seguida tive um erro em que tive que mudar para a branch "main" para fazer o cherry-pick

![alt text](assets/Abreu/mudar_main.png)

Mudei então para a main

![alt text](assets/Abreu/main.png)

E fiz a cherry-pick

![alt text](assets/Abreu/git_cherry_pick.png)

Fiz git status

![alt text](assets/Abreu/git_status.png)

Git rebase

![alt text](assets/Abreu/rebase.png)

Dei push para o Git Hub

![alt text](assets/Abreu/push.png)

Dei push para enviar as informações para o nosso github.

![alt text](assets/Abreu/img_push_abreu.png)

E enviei as informações de novo a partir do comando git push.

![alt text](assets/Abreu/img_push_abreu.png)

## Antunes

Inicialmente comecei por fazer GIT Clone, onde de seguida dei fork no Github. Daqui criei o meu repositório onde introduzi um script com erros "script_antunes"

![Screenshot at 2024-03-15 09-46-25](https://github.com/andremantunes/Trabalho-Pratico-Git/assets/144716954/727560e7-5aa4-418c-a4ed-3a3deb713576)

![Screenshot at 2024-03-15 09-38-21](https://github.com/andremantunes/Trabalho-Pratico-Git/assets/144716954/51a9af0f-6d37-402b-9c33-9b8f11dc737f)

![Screenshot at 2024-03-15 09-38-57](https://github.com/andremantunes/Trabalho-Pratico-Git/assets/144716954/a26f7f8d-8d24-435e-8160-4a4d475b0f9f)

De seguida corrigi o script "script_antunes", adicionei o script, seguido de um commit e de um rebase

![Screenshot at 2024-03-15 09-39-36](https://github.com/andremantunes/Trabalho-Pratico-Git/assets/144716954/86768049-c94e-45c7-bcc3-5cea78a20e77)

![Screenshot at 2024-03-15 09-40-03](https://github.com/andremantunes/Trabalho-Pratico-Git/assets/144716954/aa5dd674-8057-4c34-bb96-c16af9af2497)

Agora vou fazer um cherry-pick, para isto editei o script_antunes duas vezes onde dei dois commits, o "first" e o "second"

![Screenshot at 2024-03-15 09-40-19](https://github.com/andremantunes/Trabalho-Pratico-Git/assets/144716954/0ce670a1-c42d-443e-8d61-bf972caf9bdd)

![Screenshot at 2024-03-15 09-40-42](https://github.com/andremantunes/Trabalho-Pratico-Git/assets/144716954/ccae3c19-8ecc-4f25-b6ca-3f7353a35652)

![Screenshot at 2024-03-15 09-41-08](https://github.com/andremantunes/Trabalho-Pratico-Git/assets/144716954/c3c23a35-5687-452f-93ea-b157bc3426dd)

Efetuei agora o cherry-pick onde vou tentar puxar o primeiro "first"

![Screenshot at 2024-03-15 09-41-24](https://github.com/andremantunes/Trabalho-Pratico-Git/assets/144716954/07fc25b8-ab2b-4011-9790-80b0aa344da7)

![Screenshot at 2024-03-15 09-41-40](https://github.com/andremantunes/Trabalho-Pratico-Git/assets/144716954/76dfb075-062e-4a34-956b-4832b8466d17)

De seguida adicionei tags, e dei push às mesmas

![Screenshot at 2024-03-15 09-41-53](https://github.com/andremantunes/Trabalho-Pratico-Git/assets/144716954/cfcb9dad-0143-415a-aa8c-1978483b8df6)

Para finalizar corrigi um conflito que me apareceu neste processo

![Screenshot at 2024-03-15 09-42-05](https://github.com/andremantunes/Trabalho-Pratico-Git/assets/144716954/e4695084-a331-4828-a92b-ca6155e913a6)














