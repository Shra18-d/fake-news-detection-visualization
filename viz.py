"""
Visualization module for Fake News Detection
Generates matplotlib plots and saves them as images
"""

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for Flask
import matplotlib.pyplot as plt
import pandas as pd
import os


def generate_plots(fake_df, true_df, accuracy, output_dir='static'):
    """
    Generate visualization plots and save them as PNG files
    
    Parameters:
    - fake_df: DataFrame with fake news
    - true_df: DataFrame with true news
    - accuracy: Model accuracy value (0-100)
    - output_dir: Directory to save plots (default: 'static')
    """
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # ============= PLOT 1: Fake vs True News Count (Bar Chart) =============
    plot1_path = os.path.join(output_dir, 'fake_vs_true.png')
    
    fig, ax = plt.subplots(figsize=(8, 6))
    categories = ['Fake News', 'True News']
    counts = [len(fake_df), len(true_df)]
    colors = ['#ff6b6b', '#51cf66']
    
    bars = ax.bar(categories, counts, color=colors, edgecolor='black', linewidth=2)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    ax.set_ylabel('Count', fontsize=12, fontweight='bold')
    ax.set_title('Fake vs True News Distribution', fontsize=14, fontweight='bold')
    ax.set_ylim(0, max(counts) * 1.1)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.savefig(plot1_path, dpi=100, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Plot saved: {plot1_path}")
    
    # ============= PLOT 2: Text Length Distribution (Histogram) =============
    plot2_path = os.path.join(output_dir, 'text_length_distribution.png')
    
    # Calculate text lengths
    fake_lengths = fake_df['title'].str.len()
    true_lengths = true_df['title'].str.len()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create histograms with some transparency so overlapping bars are visible
    ax.hist(fake_lengths, bins=40, alpha=0.6, label='Fake News', color='#ff6b6b', edgecolor='black')
    ax.hist(true_lengths, bins=40, alpha=0.6, label='True News', color='#51cf66', edgecolor='black')
    
    ax.set_xlabel('Text Length (characters)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
    ax.set_title('Distribution of News Title Length', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.savefig(plot2_path, dpi=100, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Plot saved: {plot2_path}")
    
    # ============= PLOT 3: Model Performance (Accuracy Gauge) =============
    plot3_path = os.path.join(output_dir, 'model_accuracy.png')
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Create a simple bar showing accuracy
    accuracy_remaining = 100 - accuracy
    values = [accuracy, accuracy_remaining]
    labels = [f'Accurate\n{accuracy}%', f'Error Rate\n{accuracy_remaining}%']
    colors_accuracy = ['#51cf66', '#ff6b6b']
    
    wedges, texts, autotexts = ax.pie(values, labels=labels, colors=colors_accuracy,
                                        autopct='%1.1f%%', startangle=90,
                                        textprops={'fontsize': 11, 'fontweight': 'bold'})
    
    # Style the percentage text
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(12)
        autotext.set_fontweight('bold')
    
    ax.set_title(f'Model Accuracy: {accuracy}%', fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig(plot3_path, dpi=100, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Plot saved: {plot3_path}")
    
    # Return paths for reference
    return {
        'fake_vs_true': plot1_path,
        'text_length': plot2_path,
        'accuracy': plot3_path
    }


if __name__ == '__main__':
    # For testing purposes
    fake = pd.read_csv('Fake.csv')
    true = pd.read_csv('True.csv')
    generate_plots(fake, true, accuracy=85.5)
    print("\n✓ All plots generated successfully!")
