import streamlit as stl
from PIL import Image 

stl.title('**KurrKonvat**')
stl.markdown(''' 
             A Miniature Currency Converter App
             ''')

image = Image.open('ML1.jpeg')
stl.image(image, width=490, caption='source: Bing Image Creator')

#img = Image.open('ML2.jpeg')
#stl.sidebar.image(img.resize((50, 50)))


cur = ['dollar', 'pound', 'euro', 'naira', 'rupees', 'yen',
        'cedies', 'shekel', 'dinah', 'dirham']
rate = [1557, 1919, 1621, 1, 18, 213, 102, 437, 5064, 424]

def convert_formula(num, inital, final):
    ini_id = cur.index(inital)
    fin_id = cur.index(final)

    value1 = rate[ini_id]
    value2 = rate[fin_id]

    result = (num * value1) / value2
    return round(result, 2)


stl.divider()

with stl.form(key='currency_covert_form'):
    num = stl.number_input('how much are you converting?')
    initial_currency = stl.selectbox('what is your inital currency', cur)
    final_currency = stl.selectbox('what is your final currency', cur)
    amount = convert_formula(num, initial_currency, final_currency)

    submit_botton = stl.form_submit_button("CONVERT")
    if submit_botton:
        stl.write(amount)
        stl.balloons() 


stl.divider()
expander_bar = stl.expander('About')
expander_bar.markdown('''
                      ***python libraries:** streamlit, PIL
                      ***credit:** App built by [geraldine.nneka]
                      ''')
