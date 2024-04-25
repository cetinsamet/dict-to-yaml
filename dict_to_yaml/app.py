import yaml
import streamlit as st

def app():

    st.title('Convert a Python dictionary to YAML')
    st.write('This app converts a Python dictionary to YAML format.')

    # Get the dictionary from the user
    dict_str = st.text_area('Enter a dictionary in the format {"key": "value"}:', height=200)
    dict_str = dict_str.strip()

    # Convert the dictionary to YAML
    if dict_str:
        try:
            dict_obj = eval(dict_str)
            yaml_str = yaml.dump(dict_obj)
            st.write('YAML output:')
            st.code(yaml_str)
        except Exception as e:
            st.error(f'An error occurred: {e}')

    
    

if __name__ == '__main__':
    app()