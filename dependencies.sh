#!/bin/bash

# List of dependencies
DEPS=(pygame pygame_gui networkx)

# Detect OS
if [[ "$(uname)" == "Darwin" ]]; then
    OS="macOS"
elif [[ -f /etc/os-release ]]; then
    . /etc/os-release
    OS=$ID
elif [[ -f /etc/redhat-release ]]; then
    OS="rhel"
elif [[ "$(uname -o)" == "Msys" || "$(uname -o)" == "Cygwin" ]]; then
    OS="windows"
else
    echo "Unsupported OS"
    exit 1
fi

# Function to check if Python is installed
check_python() {
    if which python3 > /dev/null 2>&1; then
        echo "Python is already installed."
        return 0
    else
        echo "Python is not installed."
        return 1
    fi
}

# Function to install Python
install_python() {
    case "$OS" in
        ubuntu|debian)
            echo "Installing Python on Ubuntu/Debian..."
            sudo apt update && sudo apt install -y python3
            ;;
        fedora)
            echo "Installing Python on Fedora..."
            sudo dnf install -y python3
            ;;
        centos|rhel)
            echo "Installing Python on CentOS/RHEL..."
            sudo yum install -y python3
            ;;
        macOS)
            echo "Installing Python on macOS..."
            brew install python3
            ;;
        windows)
            echo "Installing Python on Windows..."
            winget install python3
            ;;
        *)
            echo "Unsupported OS for Python installation."
            exit 1
            ;;
    esac
}

# Function to install dependencies
install_deps() {
    echo "Installing dependencies..."
    python3 -m pip install "${DEPS[@]}"
}

install_pip(){
    case "$OS" in
        ubuntu|debian)
            echo "Installing pip on Ubuntu/Debian..."
            sudo apt update && sudo apt install -y python3-pip
            ;;
        fedora)
            echo "Installing pip on Fedora..."
            sudo dnf install -y python3-pip
            ;;
        centos|rhel)
            echo "Installing pip on CentOS/RHEL..."
            sudo yum install -y python3-pip
            ;;
        macOS)
            echo "Installing pip on macOS..."
            brew install python3-pip
            ;;
        windows)
            echo "Installing pip on Windows..."
            winget install python3-pip
            ;;
        *)
            echo "Unsupported OS for pip installation."
            exit 1
            ;;
    esac
}

# Main script logic
if ! check_python; then
    install_python
fi

# Verify Python installation again
if check_python; then
    install_pip
    install_deps
else
    echo "Failed to install Python. Exiting."
    exit 1
fi
