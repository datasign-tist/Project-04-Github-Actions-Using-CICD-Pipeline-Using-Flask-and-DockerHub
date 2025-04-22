from app import app

def test_home():
    tester = app.test_client()

    # Test case where name is "Abhishek" (should return "Hello World!" as it starts with 'A')
    response_abhishek = tester.post("/", data={"name": "Abhishek"})
    assert response_abhishek.status_code == 200
    assert b"Hello World!" in response_abhishek.data  # Should match the message for names starting with 'A'

    # Test case where name is "Alice" (should return "Hello World!" as it starts with 'A')
    response_alice = tester.post("/", data={"name": "Alice"})
    assert response_alice.status_code == 200
    assert b"Hello World!" in response_alice.data  # Should match the message for names starting with 'A'

    # Test case where name is "Bob" (should return personalized message "Hello, Bob!")
    response_bob = tester.post("/", data={"name": "Bob"})
    assert response_bob.status_code == 200
    assert b"Hello, Bob!" in response_bob.data  # Should return a personalized greeting

    # Test case where name is "adam" (should return "Hello World!" as it starts with 'a')
    response_adam = tester.post("/", data={"name": "adam"})
    assert response_adam.status_code == 200
    assert b"Hello World!" in response_adam.data  # Should match the message for names starting with 'A'/'a'

    # Test case where name is empty (should return "Hello, !" for no name input)
    response_empty = tester.post("/", data={"name": ""})
    assert response_empty.status_code == 200
    assert b"Hello, !" in response_empty.data  # Should handle empty name input

    # Test case where name is "Charlie" (should return personalized greeting "Hello, Charlie!")
    response_charlie = tester.post("/", data={"name": "Charlie"})
    assert response_charlie.status_code == 200
    assert b"Hello, Charlie!" in response_charlie.data  # Should return a personalized greeting
