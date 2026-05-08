import whisper
import json
import os

model = whisper.load_model("large-v2") #This loads the "large-v2" version of the model. This is the most accurate (but slowest) version, which is a great "Management Trainee" point because it shows you prioritized data quality over raw speed.

audios = os.listdir("audios")

for audio in audios: 
    if("_" in audio):  # This line makes sure that we are only processing the audio files that have the correct format.
        number = audio.split("_")[0]  # Here we split the audio files title using "_" character and take the first object as number
        title = audio.split("_")[1][:-4] # Similarly we take the second object as title and remove the last four chartacters as they are just file format details (.mp3) and they are not needed in the title.
        print(number, title)
        result = model.transcribe(audio = f"audios/{audio}", 
        # result = model.transcribe(audio = f"audios/sample.mp3", 
                              language="hi",
                              task="translate",
                              word_timestamps=False )
        
        chunks = []
        for segment in result["segments"]:
            chunks.append({"number": number, "title":title, "start": segment["start"], "end": segment["end"], "text": segment["text"]})
        
        chunks_with_metadata = {"chunks": chunks, "text": result["text"]}

        with open(f"jsons/{audio}.json", "w") as f:
            json.dump(chunks_with_metadata,f)