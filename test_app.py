import json
from fastapi.testclient import TestClient
from app import app, get_db

client = TestClient(app)

def test_get_books():
    response = client.get("/api/v1/books")
    assert response.status_code == 200
    assert response.json() == []

def test_get_book():
    response = client.get("/api/v1/books/1")
    assert response.status_code == 404

def test_create_book():
    book = {
        "title": "Test Book",
        "author": "Test Author",
        "year": 2022,
        "is_published": True
    }
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == 201
    assert response.json()["title"] == "Test Book"

def test_update_book():
    book_id = 1
    book = {
        "title": "Updated Book",
        "author": "Updated Author",
        "year": 2023,
        "is_published": False
    }
    response = client.patch(f"/api/v1/books/{book_id}", json=book)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Book"

def test_delete_book():
    book_id = 1
    response = client.delete(f"/api/v1/books/{book_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Book deleted successfully"}
