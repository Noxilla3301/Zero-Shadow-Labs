# infer.py — simple CLI inference
import sys, joblib, os

pipe = joblib.load(os.path.join('models','model.joblib'))
text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else sys.stdin.read().strip()
pred = pipe.predict([text])[0]
proba = pipe.predict_proba([text])[0].max()
print(f'class={pred} confidence={proba:.2f}')
