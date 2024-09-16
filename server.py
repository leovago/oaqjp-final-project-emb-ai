''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows multiple emotions, 
        their confidence scores and the dominant emotion 
        for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return_text = "For the given statement, the system response is "
    return_text += f"'anger': {anger_score}, "
    return_text += f"'disgust' {disgust_score}, "
    return_text += f"'fear' {fear_score}, "
    return_text += f"'joy' {joy_score}, "
    return_text += f"'sadness' {sadness_score}. "
    return_text += f"The dominant emotion is <b>{dominant_emotion}</b>."

    if dominant_emotion is None:
        return "Invalid text! Please try again!."
    return return_text

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
