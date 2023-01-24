# Ball Recognizer
An image classification model is a comprehensive solution that covers the entire process from data collection, cleaning, model training, deployment, and API integration. This cutting-edge model is specifically designed to classify 20 different types of sports balls, including: <br/>
1. Soccer Ball
2. Cricket Ball
3. Basketball Ball
4. Field Hockey Ball
5. Volleyball 
6. Tennis Ball
7. Rugby Ball
8. Baseball
9. Table Tennis Ball (Ping Pong)
10. American Football 
11. Golf Ball
12. Handball
13. Pool Ball
14. Water Polo Ball
15. Softball
16. Bocce Ball
17. Bowling Ball
18. Squash Ball
19. Lacrosse Ball
20. Wiffleball

## Data Preparation:
Dataset Preparation is a crucial step in the development of any image classification model. Great care is taken to ensure the highest quality of data for training and testing the model.<br/>

**Data Collection**: The dataset is collected by downloading images from DuckDuckGo using the sport ball's name as the search term.<br/>
**DataLoader**: To set up the DataLoader, the fastai DataBlock API is used which is a powerful and flexible library for loading and preprocessing data.<br/>
**Data Augmentation**: To further improve the model's performance, built-in data augmentation techniques from fastai which operate on the GPU for faster processing is utilized.<br/>
For more details on the dataset preparation process, please refer to the notebook `notebooks/data_prep.ipynb` which provides a step-by-step guide and in-depth explanations of the techniques used.<br/>

## Model Optimization and Data Processing
**Training**: A resnet34 model was fine-tuned for 5 epochs, repeated 3 times resulting in an accuracy of approximately 95%.<br/>
**Data Cleaning**: Data cleaning was an integral and time-consuming aspect of the model development process. Since the data was collected from the internet, there were many irrelevant and noisy images. Furthermore, some images contained errors. The fastai ImageClassifierCleaner was used to clean and update the data after each training or fine-tuning iteration, except for the final iteration which was used to train the final model.

## Model Deployment:
The model was deployed to the HuggingFace Spaces Gradio App, where it can be accessed and tested by users. The implementation details and code can be found in the `deployment` folder or by this [link](https://huggingface.co/spaces/Naosher/Ball-recognizer).<br/>
<img src = "deployment\gradio_app.png" width = "900" height = "450">

## Deployment of API on GitHub Pages Website
The deployed model API has been integrated into this [GitHub Pages Website](https://naosher98.github.io/Ball-Recognizer/), allowing users to easily access and test the model's capabilities. The implementation details, usage instructions, and other relevant information can be found in the `docs` folder for reference.
