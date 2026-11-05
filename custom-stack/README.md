# Installing Dependencies
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


# Test Execution
```sh
python -m pytest ./test/* --cov
```

# Exercicio Pratico - Mock Object

Windows (PowerShell): `python -m venv venv` e `venv\Scripts\Activate.ps1`.

Cobertura detalhada: `python -m pytest test --cov=src --cov-report=term-missing`

## Parte 1 - Testes da CustomStack (cobertura 100%)

O teste original cobria apenas um cenario (push de um elemento) e tinha uma
variavel nao utilizada. Ao analisar a efetividade dos testes foi encontrado um
defeito em `push`: a condicao `self.size == self.limit` comparava o *metodo*
`size` com um inteiro, sendo sempre `False`, de modo que `StackFullException`
nunca era lancada e a linha ficava inalcancavel. A condicao foi corrigida para
`self.size() == self.limit` (nenhum metodo novo foi criado).

Testes em `test/custom_stack_test.py`: pilha nova vazia, push, ordem LIFO,
push ate o limite, pilha cheia (`StackFullException`), pop, top e pilha vazia
(`StackEmptyException`).

## Parte 2 - NumberAscOrder

`src/number_asc_order.py`: classe `NumberAscOrder` com o metodo `sort(stack)`,
que recebe uma `CustomStack` com os numeros sorteados da Mega Sena e retorna
uma `list` em ordem ascendente.

Tratamentos: `ValueError` se o parametro for `None`; `TypeError` se nao for
`CustomStack` ou se a pilha contiver valores que nao sejam inteiros; pilha
vazia retorna lista vazia.

Testes em `test/number_asc_order_test.py`, usando **pytest-mock** para simular
a `CustomStack` (`side_effect` com retornos diferentes para chamadas ao mesmo
metodo):

- pilha de 6 posicoes com 6 numeros sorteados aleatoriamente;
- pilha de 6 posicoes vazia;
- cenarios de erro (None, tipo invalido, valores nao inteiros).
