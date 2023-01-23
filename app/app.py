from fastai.vision.all import load_learner
import gradio as gr

# import pathlib
# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath


model = load_learner("ball-recognizer-v5.pkl")

ball_labels = ('american football ball',
               'baseball ball',
               'basketball ball',
               'bocce ball',
               'bowling ball',
               'cricket ball',
               'field hockey ball',
               'golf ball',
               'handball ball',
               'lacrosse ball',
               'pool ball',
               'rugby ball',
               'soccer ball',
               'softball ball',
               'squash ball',
               'table tennis ball',
               'tennis ball',
               'volleyball ball',
               'water polo ball',
               'wiffleball ball')

def recognize_image(image):
  pred, idx, probs = model.predict(image)
  return dict(zip(ball_labels, map(float, probs)))

image = gr.inputs.Image(shape = (192, 192))
label = gr.outputs.Label(num_top_classes=5)
examples = [
    'unknown_00.jpg',
    'unknown_01.jpg',
    'unknown_02.jpg',
    'unknown_03.jpg',
    'unknown_04.jpg',
]

iface = gr.Interface(fn= recognize_image, inputs=image, outputs=label, examples = examples,  title = "Sports Ball Recognition App", description = "This app can recognize types of sports balls.")
iface.launch(inline = False)

# inline = False, share = True