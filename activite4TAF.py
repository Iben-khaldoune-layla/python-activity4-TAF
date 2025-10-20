def print_multiplication_table() :
  text = 'les tables de multiplication de 1 a 10 : \n'
  for i in range(1,11):
    text += f"la table de multiplication de {i} : \n"
    for j in range(1,11):
      text += f" {i} * {j} = {i*j} \n"
  return text
file = open("table_de_multiplication.txt","w+",encoding="utf-8")
file.write(print_multiplication_table())
file.close()