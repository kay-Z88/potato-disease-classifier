# 🥔 Potato Disease Classifier

A web app that classifies potato leaf images as **Early Blight** or **Late Blight** using a custom-trained CNN, built and deployed as a class assignment.

(https://potato-disease-classifier-dawhvhkqzfcgv3v6vejv2g.streamlit.app/)

---

## Overview

This project trains a convolutional neural network to distinguish between two potato leaf diseases — Early Blight and Late Blight — using the [PlantVillage dataset](https://www.kaggle.com/datasets/emmarex/plantdisease). The trained model is deployed as an interactive web app using Streamlit, where users can upload a leaf image and get a prediction with confidence scores.

## Dataset

- **Source:** PlantVillage dataset (provided as the fixed dataset for this assignment)
- **Classes used:** Early Blight, Late Blight only (Healthy class excluded per assignment scope)
- **Training set:** 3,878 images (1,939 per class)

## Model

- Custom CNN: 3 convolutional blocks with BatchNormalization and Dropout, followed by Dense layers
- ~322,000 parameters
- Trained for 30 epochs with EarlyStopping and ReduceLROnPlateau
- Input size: 224x224x3, includes built-in data augmentation and rescaling layers
- Achieved 100% accuracy on the PlantVillage test split

## How to Run Locally

```bash
git clone <your-repo-url>
cd <repo-folder>
pip install -r requirements.txt
streamlit run app.py
```

Requires Python 3.11 (see `runtime.txt`).

## Project Structure

```
├── app.py                      # Streamlit web app
├── potato_disease_model.keras  # Trained model
├── requirements.txt
├── runtime.txt
├──
├── notebooks/                  # Training notebook (Colab)
└── README.md
```

## Known Limitations

- **Trained on two classes only.** The model was never shown "Healthy" leaves during training, so it will always classify any image — including healthy leaves — as either Early or Late Blight.
- **Limited generalization to real-world images.** The model reaches 100% accuracy on PlantVillage's own test images, but performs poorly on independent images sourced from the web. This is a known consequence of PlantVillage's controlled studio photography (plain background, consistent lighting) — the model likely learned some visual shortcuts tied to that photography style rather than fully general disease features.
- **Manual visual inspection using standard diagnostic criteria** (contained dark spots on green tissue = Early Blight; spreading, irregular discoloration often with purple/black blotching = Late Blight) correctly classified cases where the model failed, suggesting a gap between the model's learned features and true diagnostic markers.
- Improving real-world performance would require training on a more visually diverse dataset (varied backgrounds, lighting, angles) and reintroducing a Healthy class — both outside the scope of the dataset provided for this assignment.

## Team

| Reg. Number | Name |
|---|---|
| 23/EG/CV/058 | Akpan, Uwakmfonabasi Godwin |
| 23/EG/CV/018 | Isokobo, John Sampson |
| 23/EG/CV/088 | Pius, Hepheziah Theodore 
| 23/EG/CV/038 | Imoh, Godswill okon 
| 23/EG/CV/008 | Simon, Godswill Emmanuel| 
|23/EG/CV/028| Samuel Franklyn Lawrence |
|23/EG/CV/068| Edward, Godspower Akaninyene |

## License

MIT
