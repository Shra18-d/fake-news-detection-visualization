"""
Quick Test Script for Matplotlib Visualizations
Run this to verify all plots generate correctly
"""

import pandas as pd
from viz import generate_plots
import os

print("🔍 Testing Matplotlib Visualization Integration...\n")

# Check if CSV files exist
if not os.path.exists('Fake.csv'):
    print("❌ Error: Fake.csv not found!")
    exit(1)
if not os.path.exists('True.csv'):
    print("❌ Error: True.csv not found!")
    exit(1)

print("✓ CSV files found")

# Load data
fake = pd.read_csv('Fake.csv')
true = pd.read_csv('True.csv')

print(f"✓ Loaded {len(fake)} fake news articles")
print(f"✓ Loaded {len(true)} true news articles")
print(f"  Total: {len(fake) + len(true)} articles\n")

# Test visualization generation
print("📊 Generating plots...")
try:
    result = generate_plots(fake, true, accuracy=85.5)
    print("\n✅ All plots generated successfully!\n")
    
    # Check if files were created
    for name, path in result.items():
        if os.path.exists(path):
            size_kb = os.path.getsize(path) / 1024
            print(f"  ✓ {name}: {path} ({size_kb:.2f} KB)")
        else:
            print(f"  ❌ {name}: File not found!")
            
except Exception as e:
    print(f"❌ Error generating plots: {e}")
    exit(1)

print("\n" + "="*60)
print("🎉 SUCCESS! Your visualizations are ready.")
print("="*60)
print("\nNext steps:")
print("  1. Run: python app.py")
print("  2. Open: http://localhost:10000")
print("  3. Click: '📊 View Statistics & Graphs'")
print("\n" + "="*60)
