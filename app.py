from flask import Flask,render_template,request 
import numpy as np 
import pickle 
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

app = Flask(__name__)

with open('scaled.pkl', 'rb') as file:
    scaler = pickle.load(file)
with open('pca.pkl', 'rb') as f:
    pca = pickle.load(f)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
    

    
@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/predict', methods =['POST','GET'])
def pedict():
    int_features = [float(x) for x in request.form.values()]
    final = np.array(int_features)
    scaled_data = scaler.transform([final])
    pca_data = pca.transform(scaled_data)
    prediction = model.predict(pca_data)
    if (prediction>0 and prediction<49):
       return render_template('predict.html', 
                           pred=f'<strong>The SDG Index is: </strong>{prediction}<br>'
                                f'<strong>Category:</strong> Aspirant<br>'
                                f'<strong>ESG Rating:</strong> Low ESG<br>'
                                f'<p><i>This indicates that the SDG performance is still in the early stages of development and requires significant improvement.</i></p>'
                                f'<p><i><strong>Investment Advice:</strong> Countries in this category carry higher risks and may not be ideal for risk-averse investors. However, they could offer high-reward potential for speculative or impact-focused investments if they improve their ESG practices.</i></p>')
    elif (prediction>49 and prediction<64):
        return render_template('predict.html', 
                           pred=f'<strong>The SDG Index is: </strong>{prediction}<br>'
                                f'<strong>Category:</strong> Performer<br>'
                                f'<strong>ESG Rating:</strong> Moderate ESG<br>'
                                f'<p><i>This indicates that the SDG performance is on a stable trajectory with room for growth and improvement in sustainability practices.</i></p>'
                                f'<p><i><strong>Investment Advice:</strong> Countries in this category carry moderate risks and opportunities. They may be suitable for investors willing to take a balanced approach, expecting moderate returns.</i></p>')
    elif (prediction>64 and prediction<99):
        return render_template('predict.html', 
                           pred=f'<strong>The SDG Index is: </strong>{prediction}<br>'
                                f'<strong>Category:</strong> Front Runner<br>'
                                f'<strong>ESG Rating:</strong> Good ESG<br>'
                                f'<p><i>This indicates that the SDG performance is excellent, with a strong commitment to sustainability and social responsibility.</i></p>'
                                f'<p><i><strong>Investment Advice:</strong> Countries in this category are reliable and may deliver stable returns. They are suitable for investors looking for a balance between growth and sustainability.</i></p>')
    elif (prediction==100):
        return render_template('predict.html', 
                           pred=f'<strong>The SDG Index is: </strong>{prediction}<br>'
                                f'<strong>Category:</strong> Achiever<br>'
                                f'<strong>ESG Rating:</strong> Great ESG<br>'
                                f'<p><i>This indicates that the SDG performance is outstanding, with a leading role in sustainability and strong ESG commitment.</i></p>'
                                f'<p><i><strong>Investment Advice:</strong> Countires in this category are typically low-risk and exhibit long-term growth potential. Their strong ESG practices may attract investors seeking sustainable and ethical opportunities, making them ideal for long-term portfolios.</i></p>')
if __name__ =='__main__':
    app.run(host="0.0.0.0",debug=True)