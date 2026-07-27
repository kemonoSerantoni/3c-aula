def criar_tarefa(titulo, descricao):
# Regra de negócio: impede título vazio ou cheio de espaços
    if not titulo or titulo.strip() == "":
        raise ValueError("Título obrigatório")
    return {
        "titulo": titulo,
        "descricao": descricao,
        "status": "PENDENTE"
    }