# Declarando as lista
usuario = []
clientes = []

# Adicionando os dados
while True:
  usuario.append(input('Qual o nome do cliente? '))
  usuario.append(input('Qual o e-mail do cliente? '))
  usuario.append(input('Qual o telefone do cliente? '))
  usuario.append(int(input('Qual o idade do cliente? ')))
  clientes.append(usuario[:])
  usuario.clear()
  start = input('Deseja cadastrar outro cliente? [s/n] ')
  if start == 'n':
    break


print()
print('{:-^34}'.format(' Consulta de Clientes '))
email_localizar = input('Qual o e-mail do cliente? ')

for i in clientes:
  if email_localizar in i[1]:
    print('''Nome: {}
    E-mail: {}
    Telefone: {}
    Idade: {}'''.format(i[0], i[1], i[2], i[3]))
print('Fim')