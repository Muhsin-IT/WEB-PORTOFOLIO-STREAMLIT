import streamlit as st
from PIL import Image

# st.set_page_config(page_title="Portfolio", layout="wide")

col1, col2 = st.columns([2, 3.8])  # Menentukan lebar kolom

# Kolom kiri untuk judul
with col1:
    st.header(''' :grey[Portofo]:red[lio]''')

# Kolom tengah untuk tombol navigasi
with col2:
    st.write("")
    col1, col2, col3, col4, col5 = st.columns(5)  # 5 kolom untuk tombol

    # Menambahkan tombol navigasi di setiap kolom
    with col1:
        if st.button("Home"):
            st.write("Home page clicked!")
    with col2:
        if st.button("About"):
            st.write("About Me page clicked!")
    with col3:
        if st.button("Skills"):
            st.write("Skills page clicked!")
    with col4:
        if st.button("Project"):
            st.write("Projects page clicked!")
    with col5:
        if st.button("Contact"):
            st.write("Contact Us page clicked!")
            
st.markdown('___')

# Konten Profil di bawah header
colom1, colom2  = st.columns([3,2])  

with colom1:
    st.header("")
    st.markdown('''#### _:red[Hello], my :grey[name] is_''')
    st.markdown("# Muhammad Muhsin")
    st.markdown("### :grey[I'm a Software & Web Developer]")
    st.header("")
    
with colom2:
    st.empty()
    img = Image.open("ftprofil1.webp")
    st.image(img)
    st.empty()

st.markdown('___')

# Konten About Me
st.header("About :red[Me]")
st.markdown('''Halo! Saya adalah seorang pengembang perangkat lunak yang berfokus pada pembuatan sistem informasi dan aplikasi web yang efisien. Selain berpengalaman dalam pengembangan *front-end* dan *back-end* menggunakan berbagai *framework* modern, saya juga memiliki pengalaman praktis di bidang *Data Science*, *Machine Learning*, dan *Internet of Things* (IoT). 

Saya berkomitmen untuk menghadirkan solusi teknologi yang bermanfaat, mulai dari digitalisasi manajemen institusi pendidikan hingga sistem otomasi perangkat keras. Saya senang mengeksplorasi teknologi terkini dan selalu berusaha memberikan hasil terbaik untuk setiap proyek yang saya kerjakan.''')

st.markdown('___')

# Konten Skills
st.header(":red[My] Skills")
st.markdown("""
- **Web Development & Server**: PHP, Laravel, Node.js, Streamlit, HTML/CSS. Berpengalaman mengelola server (Armbian, aaPanel, Apache, Nginx) dan *database* (Supabase).
- **Data Science & Machine Learning**: Python, Pandas. Menguasai implementasi algoritma seperti Naïve Bayes, K-Nearest Neighbors (KNN), Random Forest, dan Support Vector Machine (SVM).
- **IoT & Electronics**: C++, Arduino, pemrograman mikrokontroler ESP32, serta perakitan dan konfigurasi modul *hardware* elektronika.
""")

st.markdown('___')

# Konten Projects
st.header("Pro:red[jects]")

# Membuat layout dengan 3 kolom untuk menampilkan proyek secara sejajar
col1, col2, col3 = st.columns(3)

# Kartu Proyek 1
with col1:
    st.button(":red[Sistem Manajemen Pesantren]")
    st.write("**Siponpes & Web Al-Miftah**: Pengembangan *student management system* terintegrasi dan situs web profil untuk pondok pesantren menggunakan arsitektur Laravel dan basis data Supabase.")
    
# Kartu Proyek 2
with col2:
    st.button(":red[Machine Learning & AI]")
    st.write("**Sistem Prediksi & Rekomendasi**: Implementasi *Machine Learning* menggunakan Python untuk sistem prediksi kelulusan mahasiswa dengan Naïve Bayes dan sistem rekomendasi jurusan menggunakan Random Forest.")
    
# Kartu Proyek 3
with col3:
    st.button(":red[Otomasi Tarhim IoT]")
    st.write("**Sistem Tarhim Otomatis**: Rancang bangun pemutar tarhim prabuh terjadwal otomatis menggunakan mikrokontroler ESP32, DFPlayer Mini, dan modul *relay* untuk mengontrol amplifier.")
    
st.markdown('___')

# Konten Contact
st.header("Contact")

# URL yang ingin dibuka
kolom1, kolom2, kolom3 = st.columns([1,1,1])

with kolom1:
    img = Image.open("instagram.png")
    st.image(img, width=60)
    st.write("[:red[Instagram]](https://www.instagram.com/mad_muhsin/)")

with kolom2:
    img = Image.open("facebook.png")
    st.image(img, width=60)
    # Jangan lupa ganti URL di bawah dengan link Facebook Anda yang sebenarnya
    st.write("[:red[Facebook]](https://www.facebook.com/)")

with kolom3:
    img = Image.open("dribbble.png") 
    st.image(img, width=60)
    # Jangan lupa ganti URL di bawah dengan link Github Anda yang sebenarnya
    st.write("[:red[Github]](https://github.com/)")