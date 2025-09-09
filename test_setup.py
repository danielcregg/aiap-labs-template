"""
Basic tests to verify the AI programming template setup
Run with: python -m pytest test_setup.py
"""

import sys
import subprocess
import importlib
from pathlib import Path


def test_python_version():
    """Test that we have Python 3.11 or later."""
    assert sys.version_info >= (3, 11), f"Python 3.11+ required, got {sys.version}"


def test_required_packages():
    """Test that essential packages are importable."""
    required_packages = [
        'numpy',
        'pandas',
        'matplotlib',
        'sklearn',
        'jupyter',
        'flask',
        'requests'
    ]
    
    for package in required_packages:
        try:
            importlib.import_module(package)
        except ImportError:
            assert False, f"Required package {package} not found"


def test_directory_structure():
    """Test that the expected directory structure exists."""
    base_path = Path(__file__).parent
    expected_dirs = [
        'labs',
        'labs/lab01',
        'labs/lab02', 
        'labs/lab03',
        'notebooks',
        'examples',
        'solutions',
        '.devcontainer'
    ]
    
    for dir_path in expected_dirs:
        full_path = base_path / dir_path
        assert full_path.exists(), f"Expected directory {dir_path} not found"


def test_lab_files_exist():
    """Test that lab files exist."""
    base_path = Path(__file__).parent
    expected_files = [
        'labs/lab01/README.md',
        'labs/lab01/hello_ai.py',
        'labs/lab02/README.md',
        'labs/lab02/algorithms.py',
        'labs/lab03/README.md',
        'notebooks/lab03_ml_with_ai.ipynb',
        'examples/ai_programming_example.py'
    ]
    
    for file_path in expected_files:
        full_path = base_path / file_path
        assert full_path.exists(), f"Expected file {file_path} not found"


def test_devcontainer_config():
    """Test that devcontainer configuration exists."""
    base_path = Path(__file__).parent
    devcontainer_path = base_path / '.devcontainer' / 'devcontainer.json'
    assert devcontainer_path.exists(), "devcontainer.json not found"
    
    # Basic validation that it's valid JSON
    import json
    with open(devcontainer_path) as f:
        config = json.load(f)
    
    assert 'name' in config, "devcontainer.json missing 'name' field"
    assert 'customizations' in config, "devcontainer.json missing VS Code customizations"


def test_requirements_file():
    """Test that requirements.txt exists and has expected content."""
    base_path = Path(__file__).parent
    req_path = base_path / 'requirements.txt'
    assert req_path.exists(), "requirements.txt not found"
    
    with open(req_path) as f:
        content = f.read()
    
    # Check for some essential packages
    essential = ['numpy', 'pandas', 'matplotlib', 'scikit-learn', 'jupyter']
    for package in essential:
        assert package in content, f"Package {package} not found in requirements.txt"


if __name__ == "__main__":
    # Run tests manually if pytest not available
    test_functions = [
        test_python_version,
        test_directory_structure,
        test_lab_files_exist,
        test_devcontainer_config,
        test_requirements_file
    ]
    
    print("Running setup verification tests...")
    passed = 0
    total = len(test_functions)
    
    for test_func in test_functions:
        try:
            test_func()
            print(f"✓ {test_func.__name__}")
            passed += 1
        except Exception as e:
            print(f"✗ {test_func.__name__}: {e}")
    
    print(f"\nResults: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Template is ready to use.")
    else:
        print("⚠️  Some tests failed. Please check the setup.")