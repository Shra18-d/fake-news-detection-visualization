# 🚀 Fake News Detection - Quick Start

## Installation

```bash
git clone https://github.com/Shra18-d/fake-news-detection-visualization.git
cd fake-news-detection-visualization
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

Then visit:
- Main page: `http://localhost:10000/`
- Statistics: `http://localhost:10000/stats`

## Testing

```bash
python test_plots.py
```

## Features

✅ Detect fake news using ML
✅ View beautiful data visualizations
✅ Check model accuracy
✅ Responsive design
✅ Production-ready

## Documentation

- **README.md** - Main overview
- **VISUALIZATION_GUIDE.md** - Detailed technical guide
- **QUICK_REFERENCE.md** - Quick reference
- **ARCHITECTURE_DIAGRAMS.md** - Visual diagrams

## Project Structure

```
.
├── app.py                    # Main Flask app
├── viz.py                    # Visualization module
├── test_plots.py            # Test script
├── requirements.txt         # Dependencies
├── Fake.csv                 # Fake news data
├── True.csv                 # True news data
├── templates/
│   ├── index.html          # Main page
│   └── stats.html          # Stats page
└── static/                 # Generated plots
    ├── fake_vs_true.png
    ├── text_length_distribution.png
    └── model_accuracy.png
```

## Production Deployment

```bash
gunicorn app:app -w 4 -b 0.0.0.0:10000
```

## License

MIT License
