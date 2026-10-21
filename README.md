# Gráfico 5.12 — MP10

Gráfico interativo em Python + Plotly baseado nos dados do CSV fornecido e reproduzindo o enquadramento visual da imagem de referência.

## Fonte

`Dd_grafico_5_12.csv`

Campo das estações:

```text
estacao
```

O CSV contém 17 estações e dados de 2005 a 2025. Para reproduzir a imagem fornecida, o gráfico apresenta as 12 estações que aparecem na legenda da imagem e o período 2016–2025.

## Arquivos

- `index.html` — gráfico Plotly autocontido.
- `Dd_grafico_5_12.csv` — CSV original utilizado.
- `dados_grafico.csv` — somente as 12 séries apresentadas.
- `gerar_grafico.py` — código Python.
- `.github/workflows/pages.yml` — publicação automática.
- `.nojekyll`
- `publicar_github.bat`
- `README.md`

## Instalação

```bash
pip install pandas plotly
```

## Gerar

```bash
python gerar_grafico.py
```

## Publicar no GitHub Pages

```bash
git init
git add .
git commit -m "Adicionar grafico MP10 5.12"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
git push -u origin main
```

No GitHub, selecione:

**Settings → Pages → Build and deployment → Source → GitHub Actions**

A URL será:

```text
https://SEU_USUARIO.github.io/SEU_REPOSITORIO/
```

## Atualização

Substitua `Dd_grafico_5_12.csv`, execute `python gerar_grafico.py` e faça `git add`, `git commit` e `git push`.
