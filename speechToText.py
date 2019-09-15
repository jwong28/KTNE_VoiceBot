import speech_recognition as sr

def speechToText(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "text": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    print("Listening")
    recognizer.energy_threshold = 1000
    # print("Waiting for start energy: " + str(energy))
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration = .5)
        recognizer.dynamic_energy_threshold = True
        recognizer.pause_threshold = 1
        print("Start talking")
        audio = recognizer.listen(source)
        # print("Waiting for end energy: " + str(energy))

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "text": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        print("Recieved and translating")
        response["text"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response