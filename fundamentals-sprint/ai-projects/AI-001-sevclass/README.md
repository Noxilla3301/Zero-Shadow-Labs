# AI-001 — Advisory Severity Classifier (v0.1)
Classify short security advisory snippets into {low, medium, high}.

## Setup
```bash
pip install scikit-learn pandas joblib
```

## Data
Edit `data/labeled.csv` and add rows: `text,label` with labels in {low, medium, high}.

## Train
```bash
python src/train.py
```

## Inference
```bash
echo "Unauthenticated RCE in core service" | python src/infer.py
# -> class=high confidence=0.92
```
