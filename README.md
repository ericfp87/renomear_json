# renomear_json
 Renomear arquivos .json de acordo com o código da cidade

Aqui está um exemplo de um `README.md` para o seu projeto no GitHub:

```markdown
# Renomeação de Arquivos JSON com Base em Código de Municípios

Este script em Python lê um arquivo CSV contendo códigos de municípios de Minas Gerais e renomeia arquivos JSON em um diretório específico com base no código do município. Se o código do município estiver presente no nome do arquivo JSON, o arquivo é renomeado para o nome do município correspondente.

## Pré-requisitos

- Python 3.x
- Pandas

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/ericfp87/renomear_json.git
```

2. Navegue até o diretório do projeto:

```bash
cd seu-repositorio
```

3. Instale as dependências necessárias:

```bash
pip install pandas
```

## Uso

1. Certifique-se de que o arquivo CSV (`COD_MUNICIPIOS_MG.csv`) está localizado em `C:\Files\INDICADORES DE LEITURAS - COPASA\DATABASE\`.

2. Certifique-se de que os arquivos JSON estão localizados em `C:\Files\INDICADORES DE LEITURAS - COPASA\DATABASE\MG`.

3. Execute o script:

```bash
python renomear_arquivos.py
```

O script renomeará os arquivos JSON de acordo com o nome do município correspondente ao código encontrado no arquivo CSV e exibirá o nome do município no console.

## Estrutura do Projeto

```
├── C:\Files\INDICADORES DE LEITURAS - COPASA\
│   ├── DATABASE\
│   │   ├── COD_MUNICIPIOS_MG.csv
│   │   ├── MG\
│   │   │   ├── <arquivos JSON>
├── renomear_arquivos.py
```

## Código

```python
import os
import pandas as pd
import json

# Lê o arquivo CSV com os códigos dos municípios
df = pd.read_csv("C:\\Files\\INDICADORES DE LEITURAS - COPASA\\DATABASE\\COD_MUNICIPIOS_MG.csv", delimiter=";")

# Converte a coluna de códigos para string
df["COD_MUNICIPIO"] = df["COD_MUNICIPIO"].astype(str)

# Percorre os arquivos JSON no diretório especificado
for filename in os.listdir("C:\\Files\\INDICADORES DE LEITURAS - COPASA\\DATABASE\\MG"):
    if filename.endswith(".json"):
        code = filename[:7]
        if code in df["COD_MUNICIPIO"].values:
            municipio = df[df["COD_MUNICIPIO"] == code]["MUNICIPIO"].values[0]
            os.rename(
                f"C:\\Files\\INDICADORES DE LEITURAS - COPASA\\DATABASE\\MG\\{filename}",
                f"C:\\Files\\INDICADORES DE LEITURAS - COPASA\\DATABASE\\MG\\{municipio}.json"
            )
            print(f"{municipio}")
print("Concluído")
```

## Contribuições

Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request para melhorias.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```

Se precisar de mais alguma informação ou quiser personalizar alguma parte do `README.md`, sinta-se à vontade para avisar!