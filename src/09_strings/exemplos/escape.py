# \N{nome}: Consulta um caractere específico pelo seu nome Unicode.
print("\N{GREEK CAPITAL LETTER DELTA}")  # Saída: Δ

# \uxxxx: Representa um caractere Unicode com um valor hexadecimal de 16 bits.
print("\u03A9")  # Saída: Ω

# \Uxxxxxxxx: Representa um caractere Unicode com um valor hexadecimal de 32 bits.
print("\U0001F600")  # Saída: 😀

# \ooo: Representa um caractere com um valor octal.
print("\141")  # Saída: a

# \xhh: Representa um caractere com um valor hexadecimal.
print("\x41")  # Saída: A
