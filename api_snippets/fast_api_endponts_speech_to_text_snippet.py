import speech_recognition as sr
import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException

from logger_creator import LoggerCreator

app = FastAPI()

logger = LoggerCreator(log_file_name='speech-recognition-api.log').create()


@app.get('/ping')
async def ping():
    logger.info('Ping received')
    return 'Pong'


@app.post("/speech-to-text")
async def speech_to_text(file: UploadFile = File(...)):
    logger.info('Speech to text request received...')

    recognizer = sr.Recognizer()

    with sr.AudioFile(file.file) as source:
        # listen for the data (load audio to memory)
        audio_data = recognizer.record(source)
    try:
        # recognize (convert from speech to text)
        text = recognizer.recognize_google(audio_data)
        return {"text": text}
    except sr.UnknownValueError as e:
        logger.info(e)
        error_message = "Speech Recognition could not understand audio"
        logger.info(error_message)
        raise HTTPException(status_code=400, detail=error_message)
    except sr.RequestError as e:
        error_message = "Could not request results from Speech Recognition service; {0}".format(e)
        logger.error(error_message)
        raise HTTPException(status_code=500, detail=error_message)
    except Exception as e:
        error_message = "Unknown error occurred when converting speech to text"
        logger.error(f"{error_message}: {str(e)}")
        raise HTTPException(status_code=500, detail=error_message)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, port=8000)
