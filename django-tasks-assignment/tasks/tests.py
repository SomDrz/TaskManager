from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task


class TaskAPITestCase(APITestCase):
      
    def setUp(self):
        self.task = Task.objects.create(title="Sample Task", description="Sample Description")

    def test_create_task(self):
        data = {"title": "New Task", "description": "New Description"}
        response = self.client.post("/api/tasks/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], data["title"])

    def test_get_tasks(self):
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

   
    def test_update_task(self):
        data = {"title": "Updated Title"}
        response = self.client.patch(f"/api/tasks/{self.task.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, data["title"])

    def test_delete_task(self):
        response = self.client.delete(f"/api/tasks/{self.task.id}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_search_by_title(self):
        response = self.client.get("/api/tasks/?search=Sample")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
