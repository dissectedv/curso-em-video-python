# SINTAXE ANSI: \033[style;text;backm
# Exemplo: \033[0;33;44m (Texto amarelo com fundo azul)

# --- STYLE (Estilo) ---
# 0: None (Sem estilo)
# 1: Bold (Negrito)
# 4: Underline (Sublinhado)
# 7: Negative (Invertido)

# --- TEXT (Cor do Texto) ---
# 30: Branco (Em muitos terminais é Preto)
# 31: Vermelho
# 32: Verde
# 33: Amarelo
# 34: Azul
# 35: Roxo (Magenta)
# 36: Ciano
# 37: Cinza (Em muitos terminais é Branco)

# --- BACK (Cor do Fundo) ---
# 40: Branco (Em muitos terminais é Preto)
# 41: Vermelho
# 42: Verde
# 43: Amarelo
# 44: Azul
# 45: Roxo (Magenta)
# 46: Ciano
# 47: Cinza (Em muitos terminais é Branco)

print('\033[35mHello, World!')