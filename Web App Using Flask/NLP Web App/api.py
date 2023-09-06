import paralleldots
paralleldots.set_api_key('IH4OCcC3pwUFU6jRcoyzug4ShpopFEtpLFigQEZImmk')
def ner(text):
    ner = paralleldots.ner(text)
    return ner

def sentianalysis(text):
    senti = paralleldots.sentiment(text)
    return senti

def emotionanalysis(text):
    emotional = paralleldots.emotion(text)
    return emotional
