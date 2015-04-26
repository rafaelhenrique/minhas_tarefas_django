from django.test import TestCase
from django.db.utils import IntegrityError

from tarefas.models import Tarefa
from django.contrib.auth.models import User


class CriaTarefaTesteCase(TestCase):
    def test_cria_tarefa_vazia(self):
        self.assertIsNotNone(Tarefa.objects.create())

    def test_cria_tarefa_sem_nome(self):
        with self.assertRaises(IntegrityError):
            Tarefa.objects.create(nome=None)

    def test_cria_tarefa_com_nome(self):
        self.assertIsNotNone(Tarefa.objects.create(nome="tarefa test"))


class HomeTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='admin', password='123')

    def test_home_access(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Olá')

    def test_home_link_login(self):
        response = self.client.get('/')
        self.assertContains(response, "Login")
        self.client.login(username='admin', password='123')
        response = self.client.get('/')
        self.assertNotContains(response, "Login")
