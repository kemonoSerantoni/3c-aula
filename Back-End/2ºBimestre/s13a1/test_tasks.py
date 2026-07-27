# test_tasks.py
import pytest
from tasks import criar_tarefa
def test_criar_tarefa_com_sucesso():
# Testa se a tarefa é criada corretamente
    resultado = criar_tarefa("Estudar Python", "Aprender TDD na prática")
    assert resultado["titulo"] == "Estudar Python"
    assert resultado["status"] == "PENDENTE"
def test_criar_tarefa_sem_titulo_deve_dar_erro():
# Testa se o sistema impede a criação sem título lançando um erro
    with pytest.raises(ValueError, match="Título obrigatório"):
        criar_tarefa("", "Minha descrição")