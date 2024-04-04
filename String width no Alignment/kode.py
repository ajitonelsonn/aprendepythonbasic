nome = "Jedy"
idade = 21
# Alinhamentu left, center, no right
print("{:<10}".format(nome))   # Sai "Ana       "
print("{:^10}".format(idade))  # Sai "   30    "
print("{:>10}".format(idade))  # Sai "        30"