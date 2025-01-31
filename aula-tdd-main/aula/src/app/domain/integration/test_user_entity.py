from domain.user.user_entity import User
from domain.task.task_entity import Task
from uuid import uuid4


class TestUserWithTasks:

    # Testa para adicionar tarefas ao usuário
    def test_collect_tasks(self):

        user = User(id=uuid4(), name='Marcos')
        task1 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Estudar Testes unitários",
            description="Description 2",
            completed=False,
        )
        task2 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Estudar Integração",
            description="Description 2",
            completed=False,
        )

        user.collect_task([task1, task2])

        assert len(user.tasks) == 2
        assert task1 in user.tasks
        assert task2 in user.tasks

    # Teste para contabilizar tarefas pendentes de um usuário

    def test_count_pending_tasks(self):
        user = User(id=uuid4(), name='Marcos')
        task3 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Estudar Testes unitários",
            description="Description 2",
            completed=False,
        )
        task4 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Estudar Integração",
            description="Description 2",
            completed=False,
        )
        task5 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Estudar sobre testes end to end",
            description="Description 3",
            completed=False,
        )

        user.collect_task([task3, task4, task5])
        # user.task -> 3 tarefas
        # percorrer as tarefas com um for e contar aquelas que estão marcadas
        # como completed == false
        # deve retornar 3
        pending_counting = user.count_pending_tasks()

        assert pending_counting == 3

    # Testa a quantidade de tarefas pendentes quando o user é criado
    def test_count_pending_tasks_empty(self):
        user = User(id=uuid4(), name='Vinicius')
        count_pending_tasks = user.count_pending_tasks()
        assert count_pending_tasks == 0

    # Testar quando todas as tarefas do user estão completadas
    def test_all_tasks_completed(self):
        user = User(id=uuid4(), name='Marcos')
        task1 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Estudar Testes unitários",
            description="Description 2",
            completed=False,
        )
        task2 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Estudar Integração",
            description="Description 2",
            completed=False,
        )

        user.collect_task([task1, task2])

        user.tasks[0].mark_as_completed()
        user.tasks[1].mark_as_completed()

        # coletar o retorno da função count_pending_tasks -> 0
        count_pending_tasks = user.count_pending_tasks()

        assert count_pending_tasks == 0
