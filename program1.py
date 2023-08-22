# tests/test_module_2.py
def test_name(setup_data):
    assert setup_data['name'] == 'John'

def test_age(setup_data):
    assert setup_data['age'] == 30
