#!/usr/bin/env python3
"""
Setup script for AI Support Bot
This script helps initialize the environment and check dependencies.
"""

import os
import sys
import subprocess

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        return False
    print("✅ Python version is compatible")
    return True

def install_requirements():
    """Install required packages"""
    try:
        print("📦 Installing requirements...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements")
        return False

def check_openai_key():
    """Check if OpenAI API key is set"""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("⚠️  OPENAI_API_KEY environment variable not set")
        print("   Please set your OpenAI API key:")
        print("   Windows: set OPENAI_API_KEY=your_key_here")
        print("   Linux/Mac: export OPENAI_API_KEY=your_key_here")
        return False
    print("✅ OpenAI API key is set")
    return True

def create_directories():
    """Create necessary directories"""
    directories = ['templates', 'chroma_db']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"📁 Created directory: {directory}")

def main():
    """Main setup function"""
    print("🚀 AI Support Bot Setup")
    print("=" * 30)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Install requirements
    if not install_requirements():
        sys.exit(1)
    
    # Check OpenAI key
    openai_key_set = check_openai_key()
    
    print("\n" + "=" * 30)
    if openai_key_set:
        print("🎉 Setup complete! You can now run: python app.py")
    else:
        print("⚠️  Setup mostly complete, but please set your OpenAI API key")
        print("   Then run: python app.py")

if __name__ == "__main__":
    main()



