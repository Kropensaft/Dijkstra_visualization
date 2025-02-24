#!/bin/bash

# List of dependencies
DEPS=(pygame pygame_gui networkx python3)

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

# Install dependencies based on OS
install_deps() {
    case "$OS" in
        ubuntu|debian)
            sudo apt update && sudo apt install -y python3 && python3 -m pip install "${DEPS[@]}"
            ;;
        fedora)
            sudo dnf install -y python3 && python3 -m pip install "${DEPS[@]}"
            ;;
        centos|rhel)
            sudo yum install -y python3 && python3 -m pip install "${DEPS[@]}"
            ;;
        macOS)
            python3 -m pip install "${DEPS[@]}"
            ;;
        windows)
            winget install python3
            pip install "${DEPS[@]}"
            ;;
        *)
            echo "Unsupported OS"
            exit 1
            ;;
    esac
}

# Run installation
install_deps
