import pytest
from test_Matrix_info import Matrix_info  # Replace 'your_module' with the actual module name

'''to run in terminal
pytest test_matrix_info.py
'''

# Test case for physical_matrix_info
def test_physical_matrix_info():
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    rows, cols, phys_total = Matrix_info.physical_matrix_info(matrix)
    assert rows == 2
    assert cols == 3
    assert phys_total == 6

# Test case for cyber_matrix_info
def test_cyber_matrix_info():
    matrix = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    rows, cols, cyber_total = Matrix_info.cyber_matrix_info(matrix)
    assert rows == 2
    assert cols == 3
    assert cyber_total == 6

# Test case for cps_matrix_info
def test_cps_matrix_info():
    phys_total = 6
    cyber_total = 6
    overall_total = Matrix_info.cps_matrix_info(phys_total, cyber_total)
    assert overall_total == 12

'''# If you have any setup or teardown tasks, you can use pytest fixtures

# Example of a fixture for setup
@pytest.fixture
def setup_example():
    # Perform setup tasks if needed
    yield
    # Perform teardown tasks if needed

# Usage of the fixture in a test
def test_example_with_fixture(setup_example):
    # Test code using the fixture
    assert True  # Example assertion
'''
