from streamlit_antd_components import antd_menu, MenuItem
import streamlit as st
import time
from bokeh.models.widgets import Div

st.set_page_config(layout='wide')
# Styling
# Profile
st.markdown("""
<style>
.profile {
    display: inline-block;
    width: auto;
    height: auto;
    padding: 44px 7% 44px 5%;
    background-color:#24242F;
    margin-bottom:4%;
}
            
.profile1{
    text-align: justify;
}
</style>         
            
""", unsafe_allow_html=True)
# Margin
st.markdown("""
<style>
.appview-container .main .block-container{{
        padding-top: {padding_top}rem;    }}

[data-testid="stForm"]{
    height:250px;
    background-color:#24242F;
}
[class='st-au st-av st-aw st-ax st-bj st-bk st-b8 st-bl st-bm']{
    background-color:#D7A20C;
}
            
[class='st-au st-av st-aw st-ax st-bj st-bk st-b8 st-bn st-bm']{
    background-color:#D7A20C;
}
            
[class='st-au st-av st-aw st-ax st-bj st-bk st-b8 st-bo st-bm']{
    background-color:#D7A20C;
}
            
[class='css-b3z5c9 edgvbvh5']{
    color:#747477;
}
</style>            
            
""", unsafe_allow_html=True)
# Style Circle Bar
st.markdown("""
<style>
    .padding{
        padding:1rem !important;
    }
            
    .progress{
        width: 80px;
        height: 80px;
        line-height: 80px;
        background: none;
        margin: 0 auto;
        box-shadow: none;
        position: relative;
    }
    .progress:after{
        content: "";
        width: 100%;
        height: 100%;
        border-radius: 50%;
        border: 10px solid #fff;
        position: absolute;
        top: 0;
        left: 0;
    }
    .progress > span{
        width: 50%;
        height: 100%;
        overflow: hidden;
        position: absolute;
        top: 0;
        z-index: 1;
    }
    .progress .progress-left{
        left: 0;
    }
    .progress .progress-bar{
        width: 100%;
        height: 100%;
        background: none;
        border-width: 10px;
        border-style: solid;
        position: absolute;
        top: 0;
    }
    .progress .progress-left .progress-bar{
        left: 100%;
        border-top-right-radius: 80px;
        border-bottom-right-radius: 80px;
        border-left: 0;
        -webkit-transform-origin: center left;
        transform-origin: center left;
    }
    .progress .progress-right{
        right: 0;
    }
    .progress .progress-right .progress-bar{
        left: -100%;
        border-top-left-radius: 80px;
        border-bottom-left-radius: 80px;
        border-right: 0;
        -webkit-transform-origin: center right;
        transform-origin: center right;
        animation: loading-1 1.8s linear forwards;
    }
    .progress .progress-value{
        width: 90%;
        height: 90%;
        border-radius: 50%;
        background: #44484b;
        font-size: 15px;
        color: #A3A3A8;
        line-height: 75px;
        text-align: center;
        position: absolute;
        top: 5%;
        left: 7%;
    }
    .progress.blue .progress-bar{
        border-color: #FFC107;
    }
    .progress.blue .progress-left .progress-bar{
        animation: loading-2 1.5s linear forwards 1.8s;
    }
    
    .progress-left .progress-bar{
        animation: loading-3 1s linear forwards 1.8s;
    }

    .progress-left .progress-bar{
        animation: loading-4 0.4s linear forwards 1.8s;
    }

    .progress-left .progress-bar{
        animation: loading-5 1.2s linear forwards 1.8s;
    }
    @keyframes loading-1{
        0%{
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
        }
        100%{
            -webkit-transform: rotate(180deg);
            transform: rotate(180deg);
        }
    }
    @keyframes loading-2{
        0%{
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
        }
        100%{
            -webkit-transform: rotate(180deg);
            transform: rotate(180deg);
        }
    }
    @keyframes loading-3{
        0%{
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
        }
        100%{
            -webkit-transform: rotate(90deg);
            transform: rotate(90deg);
        }
    }
    @keyframes loading-4{
        0%{
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
        }
        100%{
            -webkit-transform: rotate(180deg);
            transform: rotate(180deg);
        }
    }
    @media only screen and (max-width: 990px){
        .progress{ margin-bottom: 20px; }
    }
</style>""", unsafe_allow_html=True)

st.markdown("""
<style>
[data-testid='stSidebar']{
    background-color : rgb(36,36,47);
}
</style>""", unsafe_allow_html=True)

items = [
        MenuItem('Beranda', 'beranda', icon='house'),
        MenuItem('Cryptography', 'cryptography', icon='file-earmark-lock-fill', children=[
            MenuItem('Enkripsi', 'enkripsi', icon='lock-fill'),
            MenuItem('Dekripsi', 'dekripsi', icon='unlock-fill'),
        ]),
        MenuItem('Message Box', 'message box', icon='chat-left-text'),
        MenuItem('Setup Email', 'setup email', icon='envelope'),
        MenuItem('Logout', 'logout', icon='box-arrow-left'),

    ]
with st.sidebar.container():
    buffer, col1 = st.columns([2.2, 5])
    with col1:
        st.image("circle_me.png", width=100)
    st.markdown("<p style=text-align:center;'> Jefri Maulana </p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color: #747477'> Associate Data Scientist</p>", unsafe_allow_html=True)
    st.markdown("<hr style='height:1px; width:100%; border-width:0; color:#747477; background-color:#747477'>", unsafe_allow_html=True)

    buffer, col1 = st.columns([.2, 5])
    with col1:
        st.markdown("<p style='color: white; font-size : 15px'> Residence : Sleman</p>", unsafe_allow_html=True)
        st.markdown("<p style='color: white; font-size : 15px'> City : Sleman</p>", unsafe_allow_html=True)
        st.markdown("<p style='color: white; font-size : 15px'> Age : 23</p>", unsafe_allow_html=True)

    st.markdown("<hr style='height:1px; width:100%; border-width:0; color:#747477; background-color:#747477'>", unsafe_allow_html=True)

    # col1, col2 = st.columns([3, 3], gap='small')
    # with col1:
    #     st.markdown("""
    #     <div class="container d-flex justify-content-center padding">
    #         <div class="row">
    #             <div class="col-md-9 col-sm-6">
    #                 <div class="progress blue">
    #                     <span class="progress-left">
    #                         <span class="progress-bar"></span>
    #                     </span>
    #                     <span class="progress-right">
    #                         <span class="progress-bar"></span>
    #                     </span>
    #                     <div class="progress-value">100%</div>
    #                 </div>
    #             </div>    
    #         </div>
    #     </div>""", unsafe_allow_html=True)
    #     st.markdown("<p align='center'>Indonesia</p>", unsafe_allow_html=True)

    # with col2:
    #     st.markdown("""
    #     <div class="container d-flex justify-content-center padding">
    #         <div class="row">
    #             <div class="col-md-9 col-sm-6">
    #                 <div class="progress blue">
    #                     <span class="progress-left">
    #                         <span class="progress-bar"></span>
    #                     </span>
    #                     <span class="progress-right">
    #                         <span class="progress-bar"></span>
    #                     </span>
    #                     <div class="progress-value">70%</div>
    #                 </div>
    #             </div>    
    #         </div>
    #     </div>""", unsafe_allow_html=True)
    #     st.markdown("<p align='center'>English</p>", unsafe_allow_html=True)
       
    list_skill = ["Python", "Machine Learning", "Natural Language Processing", "Computer Vision", "Spark", "SQL", "Data Analytics"]
    level_skill = ["80 %", "80 %", "85 %", "75 %", "80 %", "85 %", "85 %", "80 %"]
    for skill, level in zip(list_skill, level_skill):
        buffer, col1, col2 = st.columns([.2, 5, 1])
        with col1:
            bar = st.progress(0)
            bar.progress(int(level.split()[0]), text=skill)
        with col2:
            st.write("")
            st.write(level)
    
    st.markdown("<hr style='height:1px; width:100%; border-width:0; color:#747477; background-color:#747477'>", unsafe_allow_html=True)
    buffer, col1 = st.columns([.2, 5])
    with col1:
        st.markdown("<a href='https://youtube.com' style='color: #747477; font-size:17px'> Download CV</a>", unsafe_allow_html=True)


    # for percent_complete in range(100):
    #     time.sleep(0.1)
    #     my_bar.progress(percent_complete + 1, text=progress_text)


# st.write("## Hello World")
st.markdown("""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<div class="profile1">
    <div class="profile">
            <h2 style='color: #747477'> Associate Data Scientist </h2>Sebagai seorang Associate Data Scientist, saya memiliki Latar belakang kuat dalam ilmu data, machine learning, dan statistik. Mengembangkan sistem dan model untuk klasifikasi penyakit jantung menggunakan SVM & Algoritma Genetika, Analisis sentimen terhadap topik seperti Covid-19 dan Ferdy Sambo menggunakan Naive Bayes dan Algoritma Genetika, Keahlian dalam pemrosesan teks, keamanan informasi termasuk enkripsi dengan Caesar Cipher & Vigenere Cipher dan yang terakhir yaitu pengalaman dalam deteksi objek otomatis menggunakan teknik seperti YOLO. Selain itu saya memiliki kemampuan untuk berkomunikasi dengan baik dan bekerja dalam tim. Komitmen untuk inovasi, terus belajar di bidang ilmu data dan siap untuk tantangan baru dan menciptakan dampak positif melalui analisis data dan kecerdasan buatan.
            <p style='font-size:25px;margin-top:25px;'>
                <a style='padding-right:10px;color:#747477;' href="https://www.linkedin.com/in/jeff20" target="_blank"><i class="fa fa-linkedin icon"></i></a>
                <a style='padding-right:10px;color:#747477;' href="https://www.instagram.com/jefri.mln/" target="_blank"><i class="fa fa-instagram icon"></i></a>
                <a style='padding-right:10px;color:#747477;' href="https://www.youtube.com/@jefrimaulana9043/featured" target="_blank"><i class="fa fa-youtube icon"></i></a>  
            </p>
    </div>
</div>  
""", unsafe_allow_html=True)

st.write("### My Projects")
col1, col2, col3= st.columns(3, gap='large')

with col1:
    form = st.empty()
    with form.form('test1'):
        st.markdown("<h5 align='center'> Stroke Classification (SVM & Genetic Algorithm)</h5>", unsafe_allow_html=True)
        st.write("")
        st.markdown("<p style='text-align:justify; color:#747477;'>Klasifikasi penyakit stroke menggunakan Support Vector Machine dan Algoritma Genetika.</p>", unsafe_allow_html=True)
        st.write("")
        submit = st.form_submit_button("Explore")
        if submit:
            js = "window.open('https://colab.research.google.com/drive/1Fg3gIyk_UyGKhj-RtGVJgTCVd2XLgMCf?usp=sharing')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

with col2:
    form = st.empty()
    with form.form('test2'):
        st.markdown("<h5 align='center'> Comparison Shopping Engine using Cosine Similarity </h5>", unsafe_allow_html=True)
        st.write("")
        st.markdown("<p style='text-align:justify; color:#747477;'>Sistem yang membandingkan beberapa produk di E-Commerce Indonesia menggunakan cosine similarity.</p>", unsafe_allow_html=True)
        st.write("")
        submit = st.form_submit_button("Explore")
        if submit:
            js = "window.open('')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

with col3:
    form = st.empty()
    with form.form('test3'):
        st.markdown("<h5 align='center'> Sentiment Analysis Covid - 19 using Naive Bayes & GA</h5>", unsafe_allow_html=True)
        st.write("")
        st.markdown("<p style='text-align:justify; color:#747477;'>Melakukan analisis sentimen twitter terhadap kasus covid-19 menggunakan naive bayes dan algoritma genetika</p>", unsafe_allow_html=True)
        st.write("")
        submit = st.form_submit_button("Explore")
        if submit:
            js = "window.open('https://colab.research.google.com/drive/19WPr8DfI9xaMYTyCBKcBN4Peghjz9PWg?usp=sharing')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

st.write("")
col1, col2, col3= st.columns(3, gap='large')

with col1:
    form = st.empty()
    with form.form('test4'):
        st.markdown("<h5 align='center'>Scholarship Selection System using SVM & SMART</h5>", unsafe_allow_html=True)
        st.write("")
        st.markdown("<p style='text-align:justify; color:#747477;'>sistem seleksi beasiswa menggunakan support vector machine dan sistem pendukung keputusan SMART</p>", unsafe_allow_html=True)
        st.write("")
        submit = st.form_submit_button("Explore")
        if submit:
            js = "window.open('https://github.com/Jeff-04/Seminar_tematik_beasiswa')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

with col2:
    form = st.empty()
    with form.form('test5'):
        st.markdown("<h5 align='center'>Cryptography Systems for Text Security (Caesar & Viginere)</h5>", unsafe_allow_html=True)
        st.write("")
        st.markdown("<p style='text-align:justify; color:#747477;'>Sistem enkripsi dan dekripsi text menggunakan caesar cipher dan viginere cipher.</p>", unsafe_allow_html=True)
        st.write("")
        submit = st.form_submit_button("Explore")
        if submit:
            js = "window.open('https://github.com/Jeff-04/Crypto_Cippher_V2')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

with col3:
    form = st.empty()
    with form.form('test6'):
        st.markdown("<h5 align='center'>Automated Object Detection (ODA)</h5>", unsafe_allow_html=True)
        st.write("")
        st.markdown("<p style='text-align:justify; color:#747477;'>Sistem training otomatis untuk object detection, dimulai dari pengambilan data, anotasi hingga training.</p>", unsafe_allow_html=True)
        st.write("")
        submit = st.form_submit_button("Explore")
        if submit:
            js = "window.open('https://medium.com/@mystearica989/object-detection-automation-yolov3-b77c3438dfd6')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

st.write("")
col1, col2, col3= st.columns(3, gap='large')

with col1:
    form = st.empty()
    with form.form('test7'):
        st.markdown("<h5 align='center'>Parking Detection System using YOLO</h5>", unsafe_allow_html=True)
        st.write("")
        st.markdown("<p style='text-align:justify; color:#747477;'>Sistem deteksi slot parkir studi kasus pemkot Yogyakarta menggunakan YOLO V3</p>", unsafe_allow_html=True)
        st.write("")
        submit = st.form_submit_button("Explore")
        if submit:
            js = "window.open('')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

with col2:
    form = st.empty()
    with form.form('test8'):
        st.markdown("<h5 align='center'> Sentiment Analysis Ferdy Sambo using Naive Bayes</h5>", unsafe_allow_html=True)
        st.write("")
        st.markdown("<p style='text-align:justify; color:#747477;'>Melakukan analisis sentimen twitter terhadap kasus ferdy sambo dari tahun 2022 - 2023</p>", unsafe_allow_html=True)
        st.write("")
        submit = st.form_submit_button("Explore")
        if submit:
            js = "window.open('https://colab.research.google.com/drive/1pmFBfxH1AfgsU_PmfBV_QheYygBkjYft?usp=sharing')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
