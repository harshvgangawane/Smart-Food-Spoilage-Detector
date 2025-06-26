Smart Food Spoilage Detector

##Problem Statement
Food spoilage is a major contributor to food waste globally, leading to economic losses, health risks, and environmental concerns. Traditional methods of detecting spoilage often rely on human senses or manual inspection, which are inconsistent and not scalable for large kitchens, food suppliers, or households.
There is a growing need for an intelligent, automated system that can accurately detect food spoilage at an early stage to reduce waste and ensure food safety.

##Solution
This project presents a Smart Food Spoilage Detector using deep learning . Built with TensorFlow and deployed via Streamlit, the system classifies food items as "Fresh" or "Spoiled" based on image data. It leverages a Convolutional Neural Network (CNN) trained on a curated dataset to make real-time predictions.

#Dataset Used
https://www.kaggle.com/datasets/kritikseth/fruit-and-vegetable-image-recognition

## Tech Stack Used
- Python
- Streamlit
- Scikit-learn

## How to Run
**Step 1. Clone the repository.**
```powershell
git clone https://github.com/harshvgangawane/Smart-Food-Spoilage-Detector
cd "Smart Food Spoilage Detector"
```
**Step 2. (Optional) Create a virtual environment.**
```powershell
python -m venv venv
.\venv\Scripts\activate
```
**Step 3. Install the requirements**
```powershell
pip install -r requirements.txt
```
**Step 4. Run the Streamlit app**
```powershell
streamlit run app.py
```

Project Architecture
Data Layer: Image datasets in data/
Model Layer: Trained Keras model in model.keras
Interface Layer: Streamlit app in app.py
Notebooks: Data exploration and model training in smart_food_spoilage.ipynb

Notebooks
smart_food_spoilage.ipynb: Data exploration, preprocessing, model training, and evaluation


Models Used
Convolutional Neural Network (CNN) for image classification
Data augmentation for robust training## Models Used


## Conclusion
This project provides a complete pipeline for detecting food spoilage using deep learning, from data preparation to deployment. The codebase is modular, extensible, and ready for integration into real-world food supply systems.
