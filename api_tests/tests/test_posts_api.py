import pytest

def test_get_all_posts(api_client):
    """Positive Test: Validate /posts returns 200 and has expected fields."""
    response = api_client.get_posts()
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data, list)
    assert "userId" in json_data[0]
    assert "title" in json_data[0]
    assert "body" in json_data[0]

@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_get_post_by_id(api_client, post_id):
    """Positive Test: Validate specific post retrieval."""
    response = api_client.get_post_by_id(post_id)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["id"] == post_id

def test_get_post_invalid_id(api_client):
    """Negative Test: Validate 404 for non-existent post."""
    response = api_client.get_post_by_id(9999)
    assert response.status_code == 404
