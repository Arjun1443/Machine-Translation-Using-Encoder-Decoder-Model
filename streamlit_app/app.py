import streamlit as st
from ui import page

page('English → French Translation','Translate a short passage and inspect the sequence-to-sequence workflow.','NATURAL LANGUAGE PROCESSING')
st.info('The notebook’s trained LSTM weights and vocabulary are absent. This working companion uses the pretrained Helsinki-NLP/opus-mt-en-fr model; it is an explicit adaptation, not the notebook checkpoint.')
@st.cache_resource
def load_model():
    from transformers import AutoTokenizer,AutoModelForSeq2SeqLM
    name='Helsinki-NLP/opus-mt-en-fr'
    tokenizer=AutoTokenizer.from_pretrained(name,trust_remote_code=False)
    model=AutoModelForSeq2SeqLM.from_pretrained(name,trust_remote_code=False)
    model.eval()
    return tokenizer,model
with st.form('translate'):
    text=st.text_area('English passage',value='Hello! I am learning how neural machine translation works.',max_chars=1500,height=150)
    run=st.form_submit_button('Translate to French',type='primary')
st.caption('The first translation downloads model files and may take time. Subsequent requests reuse the cached model.')
if run and text.strip():
    try:
        import torch
        with st.spinner('Loading the translation model and decoding…'):
            tokenizer,model=load_model()
            inputs=tokenizer(text,return_tensors='pt',truncation=True,max_length=384)
            with torch.inference_mode():
                tokens=model.generate(**inputs,max_new_tokens=256,num_beams=4)
            result=tokenizer.decode(tokens[0],skip_special_tokens=True)
        st.subheader('French translation')
        st.write(result)
        st.download_button('Download translation',result,'translation.txt','text/plain')
    except Exception:
        st.error('Translation could not run. Check model-download access, installed dependencies, and available memory. No fallback translation has been invented.')
with st.expander('From the notebook to the application'):
    st.markdown("""The notebook studies an LSTM encoder–decoder. This app uses a pretrained Marian sequence-to-sequence model to provide a deployable translation experience without retraining on missing data. Translation quality must be assessed on representative held-out examples; no accuracy or BLEU score is claimed.

Model attribution: Helsinki-NLP/opus-mt-en-fr. Consult its model card and terms before reuse. Do not enter sensitive text into a public demonstration.
""")
