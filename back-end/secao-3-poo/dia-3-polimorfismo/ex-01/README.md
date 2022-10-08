# Trybe - exercício 27.3

#### Instalação das Dependências


<details>
  <summary><strong>Trybe</strong></summary><br />
    
  -Criação do manifesto de configuração de compilação
  ```sh
  npx tsc -t es5 ./index.ts
  ```
</details>

<details>
  <summary><strong>Alternativo</strong></summary><br />

  - TypeScript (desenvolvimento)
    ```sh
    npm i -D typescript
    ```

  - Criação do manifesto de configuração de compilação
    - configurar através do tsconfig.json
    ```sh
    npx tsc --init
    ```
      
  - ts-node (global)
    ```sh
    npm i -g ts-node
    ```
  
- types do node (desenvolvimento)
    ```sh
    npm install --save @types/node
    ```

</details>

#### Execução

<details>
  <summary><strong>Linha de comando</strong></summary><br />
  
  <details>
    <summary><em>Executar com o node</em></summary><br />
    
  - Executar com o Node o arquivo gerado 

   ```sh
    node index.js
   ```
  
  </details>
  
  <details>
    <summary><em>Executar com o ts-node</em></summary><br />
    
  - O ts-node evita a necessidade de ter que gerar um dist pra que só dopois seja rodado com o node

   ```sh
    ts-node nome-do-arquivo.ts
   ```
  
  </details>

</details> 


---


<details>
  <summary><strong></strong></summary><br />


</details>

