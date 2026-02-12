from assignment import accept_text_input

def test_accept_text_input(monkeypatch, capsys):
    # Fake user input
    inputs = ["Ada", "Lovelace"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))

    # Call the function
    result = accept_text_input()

    # Capture printed output
    captured = capsys.readouterr()

    # Test return value
    assert result == ("Ada", "Lovelace")

    # Test printed output
    assert "My name is Ada Lovelace" in captured.out
