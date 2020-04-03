# Flex + Docker

Esta App recebe dados públicos através de uma api e usa seus dados.

### Pré-requisitos 📋

Para o bom funcionamento desta app as seguintes bibliotecas são necessárias.

Python 3.5 ou superior

Postgresql-11 ou superior

Psycopg2

PyQt5

### Instalação 🔧

N.B: Esta versão foi testada somente com ubuntu
   
  Nesta versão eu uso dois serviços (postgres + adminer) e um container (ubuntu + python + pyqt5)
  
  - Baixa o repositório que deve vir no nome de Flex3.zip 
  - Descompacta o arquivo .zip e renomea a pasta 'Flex-Flex3' para 'Flex3'
  - Executa o arquivo docker-compose.yaml
    ```
    docker-compose up
    ```
    que resultará à ativação dos serviços postgres e adminer (na porta 8080, cuide que esta porta não seja usada por um outro serviço no seu computador).
    
    docker cria automaticamente uma rede para a comunicação dos dois serviços mencionados em cima no nome 'flex_default'.
    
    - Construa a imagem que vai ser usada para o container
      ```
      docker build -t app_image .
      ```
    
    
### Para executar todo o sistema

```
docker run -it --network flex3_default --name andy_app -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -u qtuser -p 8000:8000 app_image python3 main.py
```

## Autor ✒️

* **Andy Kiaka** - *Trabalho Completo* - [detona115](https://github.com/detona115)

---
⌨️ com ❤️ por [detona115](https://github.com/detona115) 😊


