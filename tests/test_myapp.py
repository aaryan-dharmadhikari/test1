def test_hello(client):
    response = client.get("/")
    assert response.data == b"Hello, world! I am testing if the pipeline works!"
