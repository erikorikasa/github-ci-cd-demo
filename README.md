# github-ci-cd-demo

Projeto de exemplo para aprender GitHub Actions na prática. O repositório
só aceita merge de Pull Requests que:

1. Vêm de uma branch cujo nome começa com `feature/` (ex.: `feature/minha-mudanca`).
2. Têm cobertura de testes total **acima de 90%**.

## Como funciona

O GitHub Actions por si só não "aceita" ou "rejeita" um PR — ele só roda
checks e reporta o status (sucesso/falha) de cada um. Quem de fato bloqueia
o merge é a **branch protection rule** da branch `main`, configurada para
exigir que os checks abaixo passem antes de permitir o merge.

O workflow [`.github/workflows/ci.yml`](.github/workflows/ci.yml) roda em
todo PR aberto contra `main` e tem dois jobs independentes:

- **`check-branch-name`**: falha se a branch de origem do PR não começar
  com `feature/`.
- **`test-coverage`**: instala as dependências, roda a suíte de testes com
  `pytest-cov` e falha se a cobertura total ficar abaixo de 90%
  (`--cov-fail-under=90`).

Com a branch protection exigindo os dois checks, um PR só pode ser
mesclado quando ambas as condições são satisfeitas.

## Rodando localmente

```bash
pip install -r requirements.txt
pytest --cov=src --cov-report=term-missing --cov-fail-under=90
```

## Estrutura

```
src/calculator.py        # código de exemplo
tests/test_calculator.py # testes cobrindo o código acima
.github/workflows/ci.yml # workflow de CI
```
# concurrency demo commit 1
# concurrency demo commit 2
