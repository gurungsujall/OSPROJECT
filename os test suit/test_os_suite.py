import pytest
from main import LinuxTestSuite  # Changed from WindowsTestSuite

@pytest.fixture
def test_suite():
    return LinuxTestSuite()  # Changed from WindowsTestSuite

def test_cpu_stress(test_suite):
    assert test_suite.test_cpu_stress(duration=5) == True

def test_cpu_stress_longer_duration(test_suite):
    assert test_suite.test_cpu_stress(duration=10) == True

def test_memory_allocation(test_suite):
    assert test_suite.test_memory_allocation(size_mb=50) == True

def test_memory_allocation_large(test_suite):
    assert test_suite.test_memory_allocation(size_mb=200) == True

def test_file_operations(test_suite):
    assert test_suite.test_file_operations() == True

def test_process_info(test_suite):  # Changed from test_windows_registry
    assert test_suite.test_process_info() == True

def test_multiple_operations(test_suite):
    """Test multiple operations in sequence"""
    assert all([
        test_suite.test_cpu_stress(duration=2),
        test_suite.test_memory_allocation(size_mb=50),
        test_suite.test_file_operations(),
        test_suite.test_process_info()
    ])