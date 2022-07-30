from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_book():
    response = client.get("/books/2")
    assert response.status_code == 200
    found_book = response.json()
    assert found_book["id"] == 2
    assert found_book["title"] == "Whom daughter provide pick drive."


# def test_read_book_bad_token():
#     response = client.get("/books/foo", headers={"X-Token": "hailhydra"})
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Invalid X-Token header"}


# def test_read_inexistent_book():
#     response = client.get("/books/0")
#     assert response.status_code == 404
#     assert response.json() == {"detail": "Book not found"}


# def test_create_book():
#     response = client.post(
#         "/books/",
#         headers={"X-Token": "coneofsilence"},
#         json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
#     )
#     assert response.status_code == 200
#     assert response.json() == {
#         "id": "foobar",
#         "title": "Foo Bar",
#         "description": "The Foo Barters",
#     }


# def test_create_book_bad_token():
#     response = client.post(
#         "/books/",
#         headers={"X-Token": "hailhydra"},
#         json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
#     )
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Invalid X-Token header"}


# def test_create_existing_book():
#     response = client.post(
#         "/books/",
#         headers={"X-Token": "coneofsilence"},
#         json={
#             "id": "foo",
#             "title": "The Foo ID Stealers",
#             "description": "There goes my stealer",
#         },
#     )
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Book already exists"}
