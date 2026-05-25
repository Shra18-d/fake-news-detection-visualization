# 📚 Documentation Index

## Main Files

- **README.md** - Project overview and quick start
- **app.py** - Flask application with ML model
- **viz.py** - Matplotlib visualization module
- **requirements.txt** - Python dependencies

## Templates

- **templates/index.html** - Main detector page
- **templates/stats.html** - Statistics dashboard

## Documentation

- **GETTING_STARTED.md** - Quick start guide
- **VISUALIZATION_GUIDE.md** - Technical documentation
- **QUICK_REFERENCE.md** - Quick reference card
- **ARCHITECTURE_DIAGRAMS.md** - Visual diagrams

## Dataset

- **Fake.csv** - 23,481 fake news articles
- **True.csv** - 21,417 true news articles

## Key Routes

- `GET /` - Main page
- `POST /news` - Detection
- `GET /stats` - Statistics

## Visualizations

1. **Fake vs True Count** - Bar chart
2. **Text Length Distribution** - Histogram
3. **Model Accuracy** - Pie chart

All plots are generated at startup and saved to `/static/` folder.
