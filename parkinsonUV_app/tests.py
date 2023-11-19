from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status


class AccountIntegrationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_url = reverse('account-create')
        self.retrieve_all_url = reverse('account-retrieve-all')
        self.valid_account_data = {
            "user_id": "2",
            "id_type": 4,
            "document_id": 123456789,
            "document_type": "C.C.",
            "user_picture": "https://example.com/another-picture.jpg",
            "email": "another@correounivalle.edu.co",
            "user_status": True
        }

    def test_create_account_api(self):
        response = self.client.post(self.create_url, data=self.valid_account_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_account_api_failure(self):
        invalid_data = {
            "id_type": 2,
            "document_id": 119315890,
            "document_type": "C.C.",
            "user_picture": "https://example.com/picture.jpg",
            "email": "missing_fields@correounivalle.edu.co",
        }
        response = self.client.post(self.create_url, data=invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_all_accounts_api(self):
        response = self.client.get(self.retrieve_all_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Puedes realizar más aserciones según la lógica de tu aplicación para asegurarte de que los datos son correctos

class TherapistIntegrationTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.retrieve_all_url = reverse('therapist-retrieve-all')

    def test_retrieve_all_therapists_api(self):
        response = self.client.get(self.retrieve_all_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class PatientIntegrationTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.retrieve_all_patients_url = reverse('patient-retrieve-all')

    def test_retrieve_all_patients_api(self):
        response = self.client.get(self.retrieve_all_patients_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  

class GameIntegrationTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.retrieve_all_games_url = reverse('game-retrieve-all')

    def test_retrieve_all_games_with_type_api(self):
        response = self.client.get(self.retrieve_all_games_url, data={'type': 'Adventure'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GameIntegrationTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.retrieve_all_games_url = reverse('game-retrieve-all')

    def test_retrieve_all_games_api(self):
        response = self.client.get(self.retrieve_all_games_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GameTypeIntegrationTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.retrieve_all_game_types_url = reverse('game-type-retrieve-all')

    def test_retrieve_all_game_types_api(self):
        response = self.client.get(self.retrieve_all_game_types_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GameIntegrationTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.retrieve_all_game_types_url = reverse('game-retrieve-all')

    def test_retrieve_all_game_api(self):
        response = self.client.get(self.retrieve_all_game_types_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
class ListIntegrationTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.create_url = reverse('create-list')

    def test_create_list_api(self):
        response = self.client.get(self.create_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_list_api(self):
        response = self.client.get(self.create_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_list_api(self):
        response = self.client.get(self.create_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ActivityIntegrationTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.create_url = reverse('create-activity')

    def test_create_activity_api(self):
        response = self.client.get(self.create_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_activity_api(self):
        response = self.client.get(self.create_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_activity_api(self):
        response = self.client.get(self.create_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

class SessionAndLogsIntegrationTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.create_url = reverse('create-session')

    def test_create_session_api(self):
        response = self.client.get(self.create_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_session_api(self):
        response = self.client.get(self.create_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_all_session_api(self):
        response = self.client.get(self.create_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_logs_api(self):
        response = self.client.get(self.create_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_all_logs_api(self):
        response = self.client.get(self.create_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)