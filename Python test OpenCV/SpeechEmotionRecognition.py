import librosa
import soundfile
import os, glob, pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Extract features (mfcc, chroma, mel) from a sound file
def extract_feature(file_name, mfcc, chroma, mel):
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate = sound_file.samplerate
        if chroma:
            stft = np.abs(librosa.stft(X))
            result=np.array([])
        if mfcc:
            mfccs=np.mean(librosa.feature.mfcc(y = X,sr= sample_rate, n_mfcc=40).T,axis=0)
            result=np.hstack((result,mfccs))
        if chroma:
            chroma=np.mean(librosa.feature.chroma_stft(S = stft,sr= sample_rate).T,axis=0)
            result=np.hstack((result,chroma))
        if mel:
            mel=np.mean(librosa.feature.melspectrogram(X,sr= sample_rate).T,axis=0)
            result=np.hstack((result,mel))
    return result

# Cảm xúc trong bộ dữ liệu RAVDESS
emotions={
    '01':'Bình Thường',
    '02':'Yên Lặng',
    '03':'Vui Vẻ',
    '04':'Buồn',
    '05':'Tức Giận',
    '06':'Sợ Hãi',
    '07':'Căm Thù',
    '08':'Ngạc Nhiên',
    }

# Cảm xúc nhìn thấy
observed_emotions=['Yên Lặng', 'Vui Vẻ', 'Sợ Hãi', 'Căm Thù']

# Tải dữ liệu và trích xuất các chức năng cho từng loại âm thanh
def load_data(test_size=0.2):
    x,y = [], []
    for file in glob.glob(r"C:\Users\DK0626\Desktop\Python\Data\Audio_Speech_Actors_01-24\Actor_*\*.wav"):
        file_name= os.path.basename(file)
        emotion = emotions[file_name.split("-")[2]]
        if emotion not in observed_emotions:
            continue
        feature= extract_feature(file,mfcc=True,chroma=True,mel = True)
        x.append(feature)
        y.append(emotion)
    return train_test_split(np.array(x),y,test_size=test_size,random_state=9)
# Tách dữ liệu
x_train,x_test,y_train,y_test = load_data(test_size=0.25)

# Lấy hình dạng của tập dữ liệu training và testing 
print((x_train.shape[0],x_test.shape[0]))

# In số tính năng đã trích xuất
print(f'Features extracted: {x_train.shape[1]}')

# Initialize the Multi Layer Perceptron Classifier
model=MLPClassifier(alpha=0.01, batch_size=256, epsilon=1e-08, hidden_layer_sizes=(300,), learning_rate='adaptive', max_iter=500)

# Train the model
model.fit(x_train,y_train)

# Predict for the test set
y_pred=model.predict(x_test)

# Calculate the accuracy of our model
accuracy=accuracy_score(y_true=y_test, y_pred=y_pred)
# Print the accuracy
print("Accuracy: {:.2f}%".format(accuracy*100))