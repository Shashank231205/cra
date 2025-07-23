import random

# Simulated inference (replace with real PyTorch/ONNX model)
def run_inference():
    classes = ["Plastic", "Metal", "Paper", "Organic", "E-waste", "Unknown"]
    label = random.choice(classes)
    confidence = round(random.uniform(75, 99), 2)
    return {"label": label, "confidence": confidence}
