# web tinh toan

# import streamlit
# def sum(a,b):
#     return a+b

# def minus(a,b):
#     return a-b

# def div(a,b):
#     return a/b

# def mul(a,b):
#     return a*b

# webName=streamlit.set_page_config(page_title="calculator")
# numA = streamlit.number_input("The first num: ")
# numB = streamlit.number_input("The second num: ")
# operation=streamlit.selectbox("select", ["+","-","*", "/"])
# if operation == "+":
#     result = streamlit.write(sum(numA,numB))
# elif operation == "-":
#     result = streamlit.write(minus(numA,numB))
# elif operation == "*":
#     result = streamlit.write(mul(numA,numB))
# elif operation == "/":
#     result = streamlit.write(div(numA,numB))
pip install gtts
#web chuyen doi van ban thanh giong noi
import streamlit
from gtts import *
import playsound

webName = streamlit.set_page_config(page_title="my web")
webInput = streamlit.text_area(label="Input your text")
a = webInput
print(a)
def convertor():
    language = "en"
    output=gTTS(text=webInput,lang=language)
    filename="voice.mp3"
    output.save(filename)
    playsound.playsound(filename)

d=convertor()
webButton=streamlit.button(label="save", data=d)
