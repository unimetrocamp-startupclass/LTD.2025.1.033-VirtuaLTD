from lab_academico.config import criar_tabela, criar_conta, criar_conta_admin

# Criar tabela
criar_tabela()

# Criar coordenador (uma vez)
criar_conta('Carlos Coordenador', 'coordenador@email.com', 'admin123', 'coordenador')

# Criar aluno (usuário comum pode fazer isso)
criar_conta('Ana Aluna', 'ana@email.com', 'senha123', 'aluno')

# Criar professor via coordenador
criar_conta_admin('Prof João', 'joao@email.com', 'prof123', 'professor',
                  'coordenador@email.com', 'admin123')
