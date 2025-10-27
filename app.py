from flask import Flask, jsonify, request, render_template 
import os
from flask_cors import CORS, cross_origin 
from cnnClassifier.utils.common import decodeImage 
from cnnClassifier.pipeline.predict import PredictionPipeline 
from llm_agent.agent import get_llm_explanation
from src.cnnClassifier.utils.report_generator import generate_health_report

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(filename=self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')



@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully!"


    
@app.route("/predict", methods=['POST'])
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)

    dl_result = clApp.classifier.predict()
    print("DL Result:", dl_result, type(dl_result))  # <- add this to debug

    # Safely access prediction
    if isinstance(dl_result, list) and len(dl_result) > 0 and 'image' in dl_result[0]:
        prediction_text = dl_result[0]['image']
    elif isinstance(dl_result, dict) and 'image' in dl_result:
        prediction_text = dl_result['image']
    else:
        prediction_text = "Unknown"

    llm_resp = get_llm_explanation(prediction_text)

    return jsonify([
        dl_result,
        {
            "llm_response": llm_resp,
            "image_base64": image
        }
    ])





if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080, debug= True)