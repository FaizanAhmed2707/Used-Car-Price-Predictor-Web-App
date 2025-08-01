#!/usr/bin/env python3
"""
Cleanup script for the Car Price Prediction project.
This script removes files that should not be pushed to GitHub.
"""

import os
import shutil
from pathlib import Path

def cleanup_project():
    """Remove files that should not be pushed to GitHub."""
    
    # Files to remove
    files_to_remove = [
        'main2.py',
        'test_api.py', 
        'verify_installation.py',
        'car_price_predictor',  # Large duplicate file
        'new_model.json',
        'xgb_model.json',
        'car data.xls'
    ]
    
    # Directories to remove
    dirs_to_remove = [
        'myenv',
        '__pycache__',
        '.ipynb_checkpoints'
    ]
    
    print("🧹 Starting cleanup process...")
    
    # Remove files
    for file in files_to_remove:
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f"✅ Removed file: {file}")
            except Exception as e:
                print(f"❌ Error removing {file}: {e}")
        else:
            print(f"⚠️  File not found: {file}")
    
    # Remove directories
    for dir in dirs_to_remove:
        if os.path.exists(dir):
            try:
                shutil.rmtree(dir)
                print(f"✅ Removed directory: {dir}")
            except Exception as e:
                print(f"❌ Error removing {dir}: {e}")
        else:
            print(f"⚠️  Directory not found: {dir}")
    
    print("\n🎉 Cleanup completed!")
    print("\n📋 Files that will be kept:")
    keep_files = [
        'main.py',
        'home.py', 
        'predict.py',
        'compare.py',
        'recommend.py',
        'car_data_new.csv',
        'car_price_predictor.pkl',
        'Car Price Prediction Using Machine Learning.ipynb',
        'requirements.txt',
        '.gitignore',
        'README.md'
    ]
    
    for file in keep_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"⚠️  Missing: {file}")
    
    print("\n🚀 Your project is now ready for GitHub!")
    print("💡 Don't forget to:")
    print("   1. Create a .env file with your API keys")
    print("   2. Initialize git repository: git init")
    print("   3. Add files: git add .")
    print("   4. Commit: git commit -m 'Initial commit'")
    print("   5. Push to GitHub!")

if __name__ == "__main__":
    cleanup_project() 