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
    echo -e "Unsupported OS"
    exit 1
fi

# Function to check if Python is installed
check_python() {
    if which python3 > /dev/null 2>&1; then
        return 0
    else
        echo -e "Python is not installed."
        return 1
    fi
}

check_pip(){
    if which pip > /dev/null 2>&1; then
        echo -e "Pip already installed, skipping instalation."
        return 0
    else 
        echo -e "Pip not installed!"
        return 1
    fi
}
# Function to install Python
install_python() {
    case "$OS" in
        ubuntu|debian)
            echo -e "Installing Python on Ubuntu/Debian..."
            sudo apt update && sudo apt install -y python3
            ;;
        fedora)
            echo -e "Installing Python on Fedora..."
            sudo dnf install -y python3
            ;;
        centos|rhel)
            echo -e "Installing Python on CentOS/RHEL..."
            sudo yum install -y python3
            ;;
        macOS)
            echo -e "Installing Python on macOS..."
            brew install python3
            ;;
        windows)
            echo -e "Installing Python on Windows..."
            winget install python3
            ;;
        *)
            echo -e "Unsupported OS for Python installation."
            exit 1
            ;;
    esac
}

# Function to install dependencies
install_deps() {
    echo -e "Installing dependencies..."

    if [[ "$(uname -o)" == "Msys" || "$(uname -o)" == "Cygwin" ]]; then
    pip install "${DEPS[@]}"
    else
    python3 -m pip install "${DEPS[@]}"
    fi

}

install_pip(){
    case "$OS" in
        ubuntu|debian)
            echo -e "Installing pip on Ubuntu/Debian..."
            sudo apt update && sudo apt install -y python3-pip
            ;;
        fedora)
            echo -e "Installing pip on Fedora..."
            sudo dnf install -y python3-pip
            ;;
        centos|rhel)
            echo -e "Installing pip on CentOS/RHEL..."
            sudo yum install -y python3-pip
            ;;
        macOS)
            echo -e "Installing pip on macOS..."
            brew install python3-pip
            ;;
        windows)
            echo -e "Installing pip on Windows..."
            winget install python3-pip
            ;;
        *)
            echo -e "Unsupported OS for pip installation."
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
    if ! check_pip; then
        echo -e "Python already installed."
        install_pip
    else
        install_deps
    fi

    echo -e ""
    read -p "Press any button to close the window"
else
    echo -e -e "Failed to install Python. Exiting."
    exit 1
fi
