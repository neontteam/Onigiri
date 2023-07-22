from typing import Any, Mapping

import pytest
import requests

BASE_URL = "http://localhost:8000/"


def test_root():
    # Arrange
    url = BASE_URL
    # Act
    response = requests.get(url)
    # Assert
    assert response.status_code == 418
    assert response.json() == dict(msg="I'm a teapot")


def test_health_check():
    # Arrange
    url = BASE_URL + "health-check"
    # Act
    response = requests.get(url)
    # Assert
    assert response.status_code == 200
    assert response.json() == dict(msg="Server is healthy!")


def test_waitlist_subscribe():
    # Type=Success
    # Arrange
    url = BASE_URL + "waitlist/subscribe"
    data = dict(email="some1@example.com")
    # Act
    response = requests.post(url, json=data)
    # Assert
    assert response.status_code == 200
    assert response.json() == dict(msg="Added to waitlist!")

    # Type=Invalid Email
    # Arrange
    data = dict(email="invalidemail-example.com")
    # Act
    response = requests.post(url, json=data)
    # Assert
    assert response.status_code == 422

    # Type=Already Exists
    # Arrange
    data = dict(email="some2@example.com")
    # Act
    response = requests.post(url, json=data)
    response = requests.post(url, json=data)
    # Assert
    assert response.status_code == 400
    assert response.json() == dict(msg="Email already exists in waitlist!")


def test_login():
    # Type=Success
    # Arrange
    url = BASE_URL + "login"
    user = dict(username="admin", password="admin")
    # Act
    response = requests.post(url, json=user)
    # Assert
    assert response.status_code == 200
    assert response.json() == dict(msg="Login successful!")

    # Type=Failed
    # Arrange
    user = dict(username="admin", password="wrong-password")
    # Act
    response = requests.post(url, json=user)
    # Assert
    assert response.status_code == 401
    assert response.json() == dict(msg="Login failed!")


def test_new_chat():
    # Arrange
    url = BASE_URL + "chats/new"
    # Act
    response = requests.post(url)
    content = response.json()
    # Assert
    assert response.status_code == 200
    assert isinstance(content, Mapping)
    assert content.keys() == {"chat_id", "messages"}
    assert isinstance(content["messages"], list)
    assert len(content["messages"]) == 0


def test_list_chat():
    # Arrange
    url = BASE_URL + "chats/list"
    # Act
    response = requests.get(url)
    content = response.json()
    # Assert
    assert response.status_code == 200
    assert isinstance(content, list) and all(isinstance(item, str) for item in content)


def test_chat():
    # Arrange
    url = BASE_URL + "chats/dummy-test-id/chat"
    # Act
    response = requests.get(url)
    content = response.json()
    # Assert
    assert response.status_code == 200
    assert isinstance(content, Mapping)
    assert content.keys() == {"chat_id", "messages"}
    assert isinstance(content["messages"], list)
    assert content["chat_id"] == "dummy-test-id"
    assert len(content["messages"]) > 0


def test_chat_input():
    # Arrange
    url = BASE_URL + "chats/dummy-test-id/chat/input"
    data = dict(
        author="user",
        sent_timestamp="2021-10-01T00:00:00.000Z",
        message="Hello, world!",
    )
    # Act
    response = requests.post(url, json=data)
    content = response.json()
    # Assert
    assert response.status_code == 200
    assert isinstance(content, Mapping)
    assert content.keys() == {"chat_id", "message"}
    assert isinstance(content["message"], Mapping)
    assert content["message"].keys() == {"id", "receive_timestamp", "sent_timestamp", "author", "message"}
    assert content["chat_id"] == "dummy-test-id"
    assert content["message"]["message"] == "Hello, User!"


def test_chat_delete():
    # Arrange
    url = BASE_URL + "chats/dummy-test-id/delete"
    # Act
    response = requests.delete(url)
    # Assert
    assert response.status_code == 200
    assert response.json() == dict(chat_id="dummy-test-id", message="Done!")
