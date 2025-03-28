import os
import psutil
import subprocess
import time
import platform
import shutil

class LinuxTestSuite:
    def __init__(self):
        self.results = {}

    def test_cpu_stress(self, duration=10):
        """Test CPU under stress"""
        try:
            subprocess.run(['stress-ng', '--cpu', '1', '--timeout', str(duration)], check=True)
            return True
        except Exception:
            return False

    def test_memory_allocation(self, size_mb=100):
        """Test memory allocation"""
        try:
            # Allocate memory
            _ = bytearray(size_mb * 1024 * 1024)
            return True
        except MemoryError:
            return False

    def test_file_operations(self):
        """Test file operations"""
        try:
            test_file = '/tmp/test.txt'
            # Create test file
            with open(test_file, 'w') as f:
                f.write('Test content')
            
            # Read test file
            with open(test_file, 'r') as f:
                content = f.read()
            
            # Clean up
            os.remove(test_file)
            return content == 'Test content'
        except Exception:
            return False

    def test_process_info(self):
        """Test process information retrieval"""
        try:
            current_process = psutil.Process()
            _ = current_process.cpu_percent()
            _ = current_process.memory_info()
            return True
        except Exception:
            return False

    def test_disk_operations(self, size_mb=10):
        """Test disk write and read speeds"""
        try:
            test_file = '/tmp/disk_test.dat'
            data = b'0' * (size_mb * 1024 * 1024)
            
            # Write test
            start_time = time.time()
            with open(test_file, 'wb') as f:
                f.write(data)
            write_time = time.time() - start_time
            
            # Read test
            start_time = time.time()
            with open(test_file, 'rb') as f:
                _ = f.read()
            read_time = time.time() - start_time
            
            os.remove(test_file)
            return True
        except Exception:
            return False

    def test_system_info(self):
        """Get system information"""
        try:
            info = {
                'cpu_count': psutil.cpu_count(),
                'memory_total': psutil.virtual_memory().total,
                'disk_usage': psutil.disk_usage('/').percent,
                'platform': platform.platform(),
                'python_version': platform.python_version()
            }
            return True
        except Exception:
            return False

    def test_network_connectivity(self):
        """Test basic network connectivity"""
        try:
            result = subprocess.run(['ping', '-c', '1', '8.8.8.8'], 
                                  capture_output=True, timeout=5)
            return result.returncode == 0
        except Exception:
            return False

    def run_all_tests(self):
        """Run all available tests"""
        self.results.update({
            'cpu_stress': self.test_cpu_stress(),
            'memory_allocation': self.test_memory_allocation(),
            'file_operations': self.test_file_operations(),
            'process_info': self.test_process_info(),
            'disk_operations': self.test_disk_operations(),
            'system_info': self.test_system_info(),
            'network_connectivity': self.test_network_connectivity()
        })
        return self.results

if __name__ == "__main__":
    test_suite = LinuxTestSuite()
    results = test_suite.run_all_tests()
    print("Test Results:")
    for test, result in results.items():
        print(f"{test}: {'PASS' if result else 'FAIL'}")