import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    # Arrange
    # (Pas de préparation nécessaire ici)
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    # Arrange
    activity = "Chess Club"
    email = "testuser@mergington.edu"
    # Act
    signup = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert signup.status_code == 200 or signup.status_code == 400
    # Act
    unregister = client.post(f"/activities/{activity}/unregister?email={email}")
    # Assert
    assert unregister.status_code == 200 or unregister.status_code == 404

def test_signup_duplicate():
    # Arrange
    activity = "Programming Class"
    email = "duplicate@mergington.edu"
    client.post(f"/activities/{activity}/signup?email={email}")
    # Act
    duplicate = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert duplicate.status_code == 400
    assert "already signed up" in duplicate.json()["detail"]
