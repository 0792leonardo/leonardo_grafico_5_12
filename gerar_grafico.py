#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gráfico 5.12 – MP10 – Evolução das concentrações médias anuais – Interior UGRHIs 4, 13, 15, 19, 21 e 22
================================================================================

Este script gera um gráfico interativo em HTML mostrando a evolução temporal
das concentrações médias anuais de MP₁₀ (material particulado) para 12 cidades
do interior do estado de São Paulo.

O gráfico exibe:
- Séries temporais para cada cidade (2016-2025)
- Cores e símbolos personalizados para cada estação
- Dados carregados de um arquivo CSV
- Layout otimizado para visualização e análise

Autor: Leonardo Rocha
Data: 2026-09-09
Versão: 1.0.0
"""

# =============================================================================
# IMPORTAÇÃO DAS BIBLIOTECAS
# =============================================================================

from pathlib import Path  # Para manipulação de caminhos de arquivos de forma segura
import pandas as pd       # Para leitura e manipulação de dados em tabelas (DataFrames)
import plotly.graph_objects as go  # Para criação de gráficos interativos


# =============================================================================
# LEITURA DOS DADOS
# =============================================================================

# Define o caminho do arquivo CSV com os dados
# O arquivo deve estar na mesma pasta do script
CSV = Path("Dd_grafico_5_12.csv")

# Lê o arquivo CSV com configurações específicas:
# - sep=None: detecta automaticamente o separador (vírgula, ponto-e-vírgula, etc.)
# - engine="python": usa o parser Python para maior flexibilidade
# - encoding="utf-8-sig": lida com arquivos UTF-8 com BOM (comum em Excel)
df = pd.read_csv(CSV, sep=None, engine="python", encoding="utf-8-sig")


# =============================================================================
# CONFIGURAÇÃO DOS PARÂMETROS
# =============================================================================

# Nome da coluna que contém os nomes das estações de monitoramento
# IMPORTANTE: O nome deve corresponder EXATAMENTE ao que está no CSV
station_col = "estacao"

# Define o período de anos a ser considerado no gráfico
# O range(2016, 2026) gera anos de 2016 a 2025 (inclusive)
years = list(range(2016, 2026))


# =============================================================================
# DEFINIÇÃO DAS ESTAÇÕES E ESTILOS PERSONALIZADOS
# =============================================================================

# Lista de estações de monitoramento (cidades do interior paulista)
# A ordem define a ordem de plotagem e aparição na legenda
# (A) = Automática, (M) = Manual
stations = [
    "Ribeirão Preto (A)",           # Ribeirão Preto - Estação Automática
    "Ribeirão Preto-C.Elíseos (M)", # Ribeirão Preto - C. Elíseos - Manual
    "Franca-Cid.Nova (M)",          # Franca - Cidade Nova - Manual
    "Jaboticabal-Jd.Kennedy (M)",   # Jaboticabal - Jd. Kennedy - Manual
    "Araraquara (A)",               # Araraquara - Automática
    "Bauru (A)",                    # Bauru - Automática
    "Jaú (A)",                      # Jaú - Automática
    "Catanduva (A)",                # Catanduva - Automática
    "São José do Rio Preto (A)",    # São José do Rio Preto - Automática
    "Araçatuba (A)",                # Araçatuba - Automática
    "Marília (A)",                  # Marília - Automática
    "Presidente Prudente (A)",      # Presidente Prudente - Automática
]

# Dicionário de estilos personalizados para cada estação
# Cada estação recebe uma combinação específica de cor e símbolo
# Isso garante consistência visual e facilita a identificação
style = {
    "Ribeirão Preto (A)": ("#FF00E6", "square"),           # Rosa choque - Quadrado
    "Ribeirão Preto-C.Elíseos (M)": ("#E87500", "circle"), # Laranja - Círculo
    "Franca-Cid.Nova (M)": ("#00A651", "square-open"),    # Verde - Quadrado vazado
    "Jaboticabal-Jd.Kennedy (M)": ("#00E600", "circle"),  # Verde claro - Círculo
    "Araraquara (A)": ("#354B8C", "triangle-up"),         # Azul escuro - Triângulo
    "Bauru (A)": ("#FF0000", "diamond"),                  # Vermelho - Losango
    "Jaú (A)": ("#6B8730", "circle"),                     # Verde militar - Círculo
    "Catanduva (A)": ("#FFB000", "circle-open"),          # Amarelo - Círculo vazado
    "São José do Rio Preto (A)": ("#D100A8", "circle-open"), # Rosa - Círculo vazado
    "Araçatuba (A)": ("#111111", "diamond"),              # Preto - Losango
    "Marília (A)": ("#7139A8", "square-open"),            # Roxo - Quadrado vazado
    "Presidente Prudente (A)": ("#C75C55", "diamond-open"), # Terracota - Losango vazado
}


# =============================================================================
# CRIAÇÃO DO GRÁFICO
# =============================================================================

# Inicializa uma figura vazia
fig = go.Figure()

# Itera sobre cada estação na lista predefinida
for station in stations:
    # Busca a linha no DataFrame que corresponde à estação atual
    # astype(str).str.strip() garante que a comparação ignore espaços extras
    match = df.loc[df[station_col].astype(str).str.strip() == station]
    
    # Se a estação não for encontrada no CSV, pula para a próxima
    # Isso evita erros caso o nome da estação no CSV seja diferente
    if match.empty:
        continue
    
    # Pega a primeira linha encontrada (deve ser única)
    row = match.iloc[0]
    
    # Extrai os valores para os anos especificados (2016-2025)
    # Converte para numérico, transformando valores inválidos em NaN
    y = pd.to_numeric(row[[str(year) for year in years]], errors="coerce").tolist()
    
    # Obtém a cor e o símbolo predefinidos para esta estação
    color, symbol = style[station]
    
    # Adiciona uma série (traço) ao gráfico para esta estação
    fig.add_trace(go.Scatter(
        # Dados do eixo X (anos) e eixo Y (valores de MP₁₀)
        x=years, 
        y=y,
        
        # Modo: linha conectando pontos + marcadores nos pontos
        mode="lines+markers",
        
        # Nome da estação (aparece na legenda e no hover)
        name=station,
        
        # Não conecta pontos onde há valores ausentes (NaN)
        connectgaps=False,
        
        # Configuração da linha
        line=dict(
            color=color,          # Cor definida no dicionário style
            width=2               # Espessura da linha em pixels
        ),
        
        # Configuração dos marcadores
        marker=dict(
            color=color,          # Cor do marcador (mesma da linha)
            symbol=symbol,        # Símbolo definido no dicionário style
            size=9                # Tamanho do marcador em pixels
        ),
        
        # Template para o tooltip (informações ao passar o mouse)
        hovertemplate=(
            "<b>%{fullData.name}</b><br>"  # Nome da estação em negrito
            "MP₁₀: %{y:.0f} µg/m³<extra></extra>"  # Valor sem casas decimais
        )
    ))


# =============================================================================
# CONFIGURAÇÃO DO LAYOUT (APARÊNCIA DO GRÁFICO)
# =============================================================================

# Configura o layout do gráfico (títulos, tamanhos, cores, eixos, legenda, etc.)
fig.update_layout(
    # Tema de fundo branco com grade leve
    # Outras opções: "plotly", "ggplot2", "seaborn", "simple_white"
    template="plotly_white",
    
    # Altura da figura em pixels
    height=790,
    
    # Margens ao redor do gráfico (esquerda, direita, topo, base)
    # Margem inferior maior (245px) para acomodar a legenda horizontal
    margin=dict(l=90, r=35, t=25, b=245),
    
    # Cor de fundo do papel (área externa ao gráfico)
    # Branco - suave e profissional
    paper_bgcolor="#ffffff",
    
    # Cor de fundo da área do gráfico (onde os dados são plotados)
    # Branco
    plot_bgcolor="#ffffff",
    
    # Modo de hover: exibe informações de todas as séries simultaneamente
    # quando o mouse passa sobre um ano específico
    hovermode="x unified",
    
    # Configuração do eixo X (horizontal)
    xaxis=dict(
        tickmode="linear",           # Ticks em intervalos regulares
        dtick=1,                     # Intervalo de 1 em 1 ano
        range=[2016, 2025],          # Limites: 2016 a 2025
        showgrid=False,               # Sem linhas de grade verticais
        ticks="inside",                        # Marcadores  do eixo
        showline=True,                         # Mostra a linha do eixo
        linecolor="#B8B8B8"
    ),
    
    # Configuração do eixo Y (vertical)
    yaxis=dict(
        title="MP₁₀ (µg/m³)",        # Título do eixo com subscrito
        range=[0, 100],              # Limites fixos: 0 a 100 µg/m³
        dtick=20,                    # Intervalo de 20 em 20 µg/m³
        gridcolor="rgba(130,130,130,0.35)",  # Cor das linhas de grade (cinza com 35% opacidade)
        griddash="dash",              # Linhas de grade tracejadas
        ticks="outside",                        # Marcadores  do eixo
        showline=True,                         # Mostra a linha do eixo
        linecolor="#B8B8B8"
    ),
    
    # Configuração da legenda
    legend=dict(
        orientation="h",             # Orientação horizontal (em vez de vertical)
        yanchor="top",               # Âncora no topo da legenda
        y=-0.13,                     # Posiciona abaixo do gráfico (valor negativo)
        xanchor="center",            # Centralizado horizontalmente
        x=0.5,                       # Centro do eixo X (50%)
        font=dict(size=12)           # Tamanho da fonte da legenda
    )
)


# =============================================================================
# EXPORTAÇÃO DO GRÁFICO
# =============================================================================

# Salva o gráfico em um arquivo HTML (autônomo, com Plotly embutido)
fig.write_html(
    "index.html",                    # Nome do arquivo de saída
    include_plotlyjs=True,           # Inclui a biblioteca Plotly (não precisa de internet)
    full_html=True,                  # Gera um documento HTML completo
    config={                         # Configurações do gráfico
        "responsive": True,          # Gráfico se adapta ao tamanho da tela
        "displaylogo": False,        # Remove o logo da Plotly da barra de ferramentas
        "scrollZoom": True           # Permite zoom com scroll do mouse
    }
)


# =============================================================================
# MENSAGEM DE CONFIRMAÇÃO
# =============================================================================

# Exibe informações no console sobre o arquivo gerado
print("=" * 70)
print("✅ GRÁFICO GERADO COM SUCESSO!")
print("=" * 70)
print(f"📊 Arquivo: index.html")
print(f"📍 Local: {Path.cwd()}")
print(f"📈 Cidades: {len(stations)}")
print(f"📅 Período: {min(years)} a {max(years)}")
print(f"🎨 Estilos personalizados: {len(style)} estações configuradas")
print("=" * 70)
print("🌐 Abra o arquivo no navegador para visualizar o gráfico interativo.")