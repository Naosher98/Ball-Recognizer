## Ball-Recognizer
Our image classification model is a comprehensive solution that covers the entire process from data collection, cleaning, model training, deployment, and API integration. This cutting-edge model is specifically designed to classify 20 different types of sports balls, including: <br/>
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

# Data Preparation:
Dataset Preparation is a crucial step in the development of any image classification model. Great care is taken to ensure the highest quality of data for training and testing the model.<br/>

Data Collection: The dataset is collected by downloading images from DuckDuckGo using the sport ball's name as the search term.
DataLoader: To set up the DataLoader, the fastai DataBlock API is used which is a powerful and flexible library for loading and preprocessing data.
Data Augmentation: To further improve the model's performance, built-in data augmentation techniques from fastai which operate on the GPU for faster processing is utilized.<br/>
For more details on the dataset preparation process, please refer to the notebook 'notebooks/data_prep.ipynb' which provides a step-by-step guide and in-depth explanations of the techniques used.<br/>