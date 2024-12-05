from flask import Flask,jsonify
from flask_cors import CORS
from pytube import YouTube 


link = input(" Enter The Link Here >> ")

y_tube = YouTube(link)

print(f'Video Title >> {y_tube.title}')
print(f'Video Description >> {y_tube.description}')

stream = y_tube.streams.filter(progressive=True)
video = list(enumerate(stream))

for i in video:
    print(i)

index =int( input("Select Prefered Quality >> "))
stream[index].download()
print("Success")
if __name__ == "__main__":
    
    
    
    # https://youtu.be/bQ-QKim9Tjc