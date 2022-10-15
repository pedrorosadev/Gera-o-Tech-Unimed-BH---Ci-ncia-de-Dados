contatos = {
    'guilherme@gmail.com': {'nome':'Guilherme', 'telefone':'3333-2221'}
}

#contatos['chave'] #KeyError

print(contatos.get('chave')) #None
print(contatos.get('chave', {})) #{}
print(contatos.get('guilherme@gmail.com', {}))