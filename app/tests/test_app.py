import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Note

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def create_notes():
    Note.objects.create(title="Test Note 1", body="body for test note 1")
    Note.objects.create(title="Test Note 2", body="body for test note 2")
    Note.objects.create(title="Sample Note", body="Sample body")

@pytest.mark.django_db
def test_list_notes(client, create_notes):
    url = reverse('notes')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3
    
@pytest.mark.django_db
def test_list_notes_bad_method(client, create_notes):
    url = reverse('notes')
    response = client.put(url)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    
@pytest.mark.django_db
def test_create_note(client):
    url = reverse('notes')
    data = {'title': 'New Note', 'body': 'This is a new note.'}
    response = client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Note.objects.count() == 1

@pytest.mark.django_db
def test_retrieve_single_note(client, create_notes):
    note = Note.objects.first()
    url = reverse('get-single-note', kwargs={'pk': note.pk})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == note.title

@pytest.mark.django_db
def test_search_notes(client, create_notes):
    url = reverse('note-search') + '?title=Sample'
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['title'] == 'Sample Note'

@pytest.mark.django_db
def test_update_note(client, create_notes):
    note = Note.objects.first()
    url = reverse('notes-update', kwargs={'pk': note.pk})
    data = {'title': 'Updated Note Title', 'body': note.body}
    response = client.put(url, data)
    assert response.status_code == status.HTTP_200_OK
    note.refresh_from_db()
    assert note.title == 'Updated Note Title'
