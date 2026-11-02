#!/usr/bin/env python
"""Setup script for Django CV project"""
import os
import subprocess
import sys

def main():
    print("=" * 60)
    print("Django CV - Setup Script")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("Error: Please run this script from the django_cv directory")
        sys.exit(1)
    
    print("\n1. Creating virtual environment...")
    subprocess.run([sys.executable, '-m', 'venv', '.venv'])
    
    # Determine the activate command based on OS
    if sys.platform == 'win32':
        activate_cmd = '.\.venv\Scripts\activate'
    else:
        activate_cmd = 'source .venv/bin/activate'
    
    print(f"\n2. Activating virtual environment...")
    print(f"   Run: {activate_cmd}")
    
    print("\n3. Installing dependencies...")
    if sys.platform == 'win32':
        subprocess.run(['.venv\Scripts\python', '-m', 'pip', 'install', '-r', 'requirements.txt'])
    else:
        subprocess.run(['.venv/bin/python', '-m', 'pip', 'install', '-r', 'requirements.txt'])
    
    print("\n4. Copying .env.example to .env...")
    if not os.path.exists('.env'):
        with open('.env.example', 'r') as f:
            content = f.read()
        with open('.env', 'w') as f:
            f.write(content)
        print("   Done!")
    else:
        print("   .env already exists, skipping...")
    
    print("\n5. Running migrations...")
    subprocess.run([sys.executable, 'manage.py', 'migrate'])
    
    print("\n6. Loading initial data...")
    subprocess.run([sys.executable, 'manage.py', 'loaddata', 'cv/fixtures/initial_data.json'])
    
    print("\n" + "=" * 60)
    print("Setup complete!")
    print("=" * 60)
    print("\nTo start the development server:")
    print(f"  1. Activate the virtual environment: {activate_cmd}")
    print("  2. Run: python manage.py runserver")
    print("  3. Open your browser to: http://localhost:8000")
    print("=" * 60)

if __name__ == '__main__':
    main()
