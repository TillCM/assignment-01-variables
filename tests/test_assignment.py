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

    #---------------------------------------------------------------------------------------------------
from assignment import accept_alphanumeric_input

def test_accept_alphanumeric_input(monkeypatch, capsys):
    # Fake user input
    inputs = ["Ada", "Lovelace", "20"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))

    # Call the function
    result = accept_alphanumeric_input()

    # Capture printed output
    captured = capsys.readouterr()

    # Check return value
    assert result == ("Ada", "Lovelace", 20)

    # Check printed output
    expected_output = "My name is Ada Lovelace and I am 20 years old"
    assert expected_output in captured.out
#-----------------------------------------------------------------------------------------------------------------from assignment import accept_alphanumeric_input_convert

def test_accept_alphanumeric_input_convert(monkeypatch, capsys):
    # Fake user input
    inputs = ["Ada", "Lovelace", "20"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))

    # Call the function
    result = accept_alphanumeric_input_convert()

    # Capture printed output
    captured = capsys.readouterr()

    # Check return value
    # We expect age to be returned as a STRING after conversion
    assert result == ("Ada", "Lovelace", 20)

    # Check printed output
    expected_output = "My name is Ada Lovelace and I am 20 years old"
    assert expected_output in captured.out
#------------------------------------------------------------------------------------------------------
from assignment import add_two_numbers

def test_add_two_numbers(monkeypatch, capsys):
    # Fake user input
    inputs = ["5", "7"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))

    # Call function
    result = add_two_numbers()

    # Capture output
    captured = capsys.readouterr()

    # Check return value
    assert result == 12

    # Check printed output
    assert "12" in captured.out
#--------------------------------------------------------------------------------------------------------
from assignment import floor_division

def test_floor_division(monkeypatch, capsys):
    # Fake input
    inputs = ["7", "2"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))

    result = floor_division()
    captured = capsys.readouterr()

    # Floor division check
    assert result == 3

    # Make sure printed output includes the result
    assert "3" in captured.out
#-----------------------------------------------------------------------------------------------------

def test_compare_numbers(capsys):
    result = compare_numbers()
    captured = capsys.readouterr()

    assert result is False
    assert "False" in captured.out

#_---------------------------------------------------------------------------------------------------------
from assignment import calc_bmi

def test_calc_bmi(capsys):
    result = calc_bmi()
    captured = capsys.readouterr()

    # Check BMI calculation (allow small float tolerance)
    assert round(result, 2) == 16.98

    # Check classification
    assert "Normal BMI" in captured.out
