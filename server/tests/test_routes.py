def test_create_entry(client):
    client.post('/auth/register', json={"username": "testuser", "password": "securepass"})
    client.post('/auth/login', json={"username": "testuser", "password": "securepass"})
    
    response = client.post('/api/entries', json={"title": "Workout", "content": "Ran 5 miles"})
    assert response.status_code == 201
    assert b"Entry created" in response.data

def test_get_entries(client):
    client.post('/auth/register', json={"username": "testuser", "password": "securepass"})
    client.post('/auth/login', json={"username": "testuser", "password": "securepass"})

    response = client.get('/api/entries?page=1&per_page=5')
    assert response.status_code == 200

def test_update_entry(client):
    client.post('/auth/register', json={"username": "testuser", "password": "securepass"})
    client.post('/auth/login', json={"username": "testuser", "password": "securepass"})
    client.post('/api/entries', json={"title": "Workout", "content": "Ran 5 miles"})

    response = client.patch('/api/entries/1', json={"title": "Updated Workout"})
    assert response.status_code == 200
    assert b"Entry updated" in response.data

def test_delete_entry(client):
    client.post('/auth/register', json={"username": "testuser", "password": "securepass"})
    client.post('/auth/login', json={"username": "testuser", "password": "securepass"})
    client.post('/api/entries', json={"title": "Workout", "content": "Ran 5 miles"})

    response = client.delete('/api/entries/1')
    assert response.status_code == 200
    assert b"Entry deleted" in response.data