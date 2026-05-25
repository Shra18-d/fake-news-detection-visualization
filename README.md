# 📰 Fake News Detection with Matplotlib Visualizations

A Flask-based web application that detects fake news using Machine Learning and provides professional data visualizations using Matplotlib.

## ✨ Features

- **🤖 ML-Powered Detection**: Uses TF-IDF vectorization and PassiveAggressiveClassifier
- **📊 Data Visualizations**: Three matplotlib plots (bar chart, histogram, pie chart)
- **🎨 Beautiful Dashboard**: Responsive HTML5 interface with modern CSS
- **🧪 Easy Testing**: Includes verification scripts
- **📚 Comprehensive Docs**: 10 documentation files
- **🚀 Production-Ready**: Can be deployed with Gunicorn

## 📊 Visualizations

1. **Fake vs True News Count** - Bar chart showing dataset distribution
2. **Text Length Distribution** - Histogram comparing title lengths
3. **Model Accuracy** - Pie chart showing model performance

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip

### Installation

```bash
# Clone repository
git clone https://github.com/Shra18-d/fake-news-detection-visualization.git
cd fake-news-detection-visualization

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

```bash
# Development
python app.py

# Visit in browser:
# Main page:  http://localhost:10000/
# Stats page: http://localhost:10000/stats
```

### Running Tests

```bash
python test_plots.py
```

## 📁 Project Structure

```
fake-news-detection-visualization/
├── app.py                          # Main Flask application
├── viz.py                          # Visualization module
├── test_plots.py                   # Verification script
├── requirements.txt                # Python dependencies
├── Fake.csv                        # Fake news dataset (23,481 articles)
├── True.csv                        # True news dataset (21,417 articles)
├── templates/
│   ├── index.html                  # Main detector page
│   └── stats.html                  # Statistics dashboard
├── static/                         # Generated plot images
│   ├── fake_vs_true.png
│   ├── text_length_distribution.png
│   └── model_accuracy.png
└── docs/
    ├── README_VISUALIZATION.md     # Detailed technical guide
    ├── VISUALIZATION_GUIDE.md      # In-depth guide
    ├── QUICK_REFERENCE.md          # Quick reference
    ├── ARCHITECTURE_DIAGRAMS.md    # Visual diagrams
    └── ... (more documentation)
```

## 🔧 Technical Stack

- **Backend**: Flask 2.x
- **Data Processing**: Pandas, Scikit-learn
- **ML Model**: PassiveAggressiveClassifier with TF-IDF
- **Visualization**: Matplotlib 3.x
- **Frontend**: HTML5, CSS3, Jinja2
- **Server**: Gunicorn (production)

## 📊 Dataset

- **Fake.csv**: 23,481 fake news articles
- **True.csv**: 21,417 real news articles
- **Features**: Title, text, subject, date, class

## 🎯 Routes

- `GET /` - Main fake news detector page
- `POST /news` - Process news detection
- `GET /stats` - Statistics and visualizations dashboard

## 📚 Documentation

- **START_HERE.md** - Main entry point (read this first!)
- **EXECUTIVE_SUMMARY.md** - Executive overview
- **README_VISUALIZATION.md** - Complete technical guide
- **VISUALIZATION_GUIDE.md** - Detailed technical documentation
- **QUICK_REFERENCE.md** - Quick reference card
- **ARCHITECTURE_DIAGRAMS.md** - 7 visual diagrams
- **HTML_SNIPPETS.html** - Reusable code examples
- **DOCUMENTATION_INDEX.md** - Navigation guide

## 🚀 Production Deployment

```bash
pip install gunicorn
gunicorn app:app -w 4 -b 0.0.0.0:10000
```

## 🔧 Customization

### Change Plot Colors

Edit `viz.py`:
```python
colors = ['#your_color', '#another_color']
```

### Change Plot Size

```python
fig, ax = plt.subplots(figsize=(12, 8))
```

### Add New Visualizations

Add functions to `generate_plots()` in `viz.py`

## 📊 Model Performance

The ML model achieves ~85%+ accuracy on test data using:
- TF-IDF vectorization
- PassiveAggressiveClassifier
- 75/25 train-test split

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

## 📝 License

MIT License - Feel free to use this project for learning and development

## 👨‍💻 Author

Created with ❤️ by Shra18-d

## 🙏 Acknowledgments

- Flask documentation
- Scikit-learn community
- Matplotlib documentation
- Fake news dataset providers

## 📞 Support

For questions or issues:
1. Check the documentation files
2. Review code comments
3. Run `python test_plots.py` for verification

---

**Happy Data Visualizing!** 📊✨
