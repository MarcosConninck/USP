import pytest
from uuid import uuid4
from domain.task.task_entity import Task


class TestTask:

    # Test para verificar o construtor da classe Tarefa
    def test_task_init(self):
        task_id = uuid4()
        user_id = uuid4()
        title = "Lavar louça"
        description = "para cozinhar o almoço, caso contrario não terá panela"
        completed = False

        task = Task(
            id=task_id,
            user_id=user_id,
            title=title,
            description=description,
            completed=completed
        )

        assert task.id == task_id
        assert task.user_id == user_id
        assert task.title == title
        assert task.description == description
        assert task.completed == completed

    # Teste para validação do id da tarefa
    def test_task_id_validation(self):
        user_id = uuid4()
        with pytest.raises(Exception, match="id must be an UUID"):
            Task(
                id="invalid task id",
                user_id=user_id,
                title="titulo tarefa",
                description="descrição tarefa",
                completed=False
            )

    # Teste para verificar o ID do usuário
    def test_task_user_id_validation(self):
        task_id = uuid4()
        with pytest.raises(Exception, match="user_id must be an UUID"):
            Task(
                id=task_id,
                user_id="invalid user_id",
                title="titulo tarefa",
                description="descrição tarefa",
                completed=False
            )

    # Teste para verificar o titulo da tarefa
    def test_task_title_validation(self):
        user_id = uuid4()
        task_id = uuid4()
        with pytest.raises(Exception, match="title is required"):
            Task(
                id=task_id,
                user_id=user_id,
                title="",
                description="descrição tarefa",
                completed=False
            )

    # Teste para verificar a descrição da tarefa
    def test_task_description_validation(self):
        user_id = uuid4()
        task_id = uuid4()
        with pytest.raises(Exception, match="description is required"):
            Task(
                id=task_id,
                user_id=user_id,
                title="valid title",
                description="",
                completed=False
            )

    # Teste para verificar do status da tarefa
    def test_task_completed_validation(self):
        user_id = uuid4()
        task_id = uuid4()
        with pytest.raises(Exception, match="invalid completed status: must be bool"):
            Task(
                id=task_id,
                user_id=user_id,
                title="valid title",
                description="valid description",
                completed="not_boolean"
            )

    # Teste para verificar se uma tarefa foi completada com mark_as_completed()
    def test_mark_as_completed(self):
        user_id = uuid4()
        task_id = uuid4()
        task = Task(
            id=task_id,
            user_id=user_id,
            title="titulo tarefa",
            description="descrição tarefa",
            completed=False
        )

        # marcar a tarefa como concluída
        task.mark_as_completed()

        # verificar se o atributo foi atualizado para completed
        assert task.completed is True
