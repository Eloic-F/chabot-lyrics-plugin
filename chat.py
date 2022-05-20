from matplotlib.style import context
import numpy
import tools
from app import analyse, searchAnswer

subjects, types, stopwords, dictionnary = tools.defaultValues()
context= None


def get_response(msg):
    rSubject, rType, rValue= analyse(msg)
    global context
    if context is None:
        context=  subjects[numpy.argmax(rSubject)].split(".")[0]
    result = searchAnswer(msg, subjects[numpy.argmax(rSubject)], types[numpy.argmax(rType)], context)
    if context is not "lyrics":
        context= None
    return result