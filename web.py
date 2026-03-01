import streamlit as st
from PIL import Image

# st.set_page_config(page_title="Portfolio", layout="wide")

col1, col2 = st.columns([2, 3.8])  # Menentukan lebar kolom

# Kolom kiri untuk judul
with col1:
    st.header(''' :grey[Portofo]:red[lio]''')

# Kolom tengah untuk navigasi (Menggunakan Markdown Anchor Links)
with col2:
    st.write("")
    col1, col2, col3, col4, col5 = st.columns(5)  

    with col1:
        st.markdown("<a href='#home' style='text-decoration:none; color:inherit;'><b>🏠 Home</b></a>", unsafe_allow_html=True)
    with col2:
        st.markdown("<a href='#about' style='text-decoration:none; color:inherit;'><b>👤 About</b></a>", unsafe_allow_html=True)
    with col3:
        st.markdown("<a href='#skills' style='text-decoration:none; color:inherit;'><b>⚙️ Skills</b></a>", unsafe_allow_html=True)
    with col4:
        st.markdown("<a href='#projects' style='text-decoration:none; color:inherit;'><b>🚀 Project</b></a>", unsafe_allow_html=True)
    with col5:
        st.markdown("<a href='#contact' style='text-decoration:none; color:inherit;'><b>📞 Contact</b></a>", unsafe_allow_html=True)
            
st.markdown('___')

# ================= HOME SECTION =================
# Anchor untuk Home
st.markdown("<div id='home'></div>", unsafe_allow_html=True)

colom1, colom2  = st.columns([3,2])  

with colom1:
    st.header("")
    st.markdown('''#### _:red[Hello], my :grey[name] is_''')
    st.markdown("# Muhammad Muhsin")
    st.markdown("### :grey[I'm a Web | IoT Developer & IT Enthusiast]")
    st.header("")
    
with colom2:
    st.empty()
    # Pastikan file fotoprofil.png ada di folder yang sama
    img = Image.open("ftprofil1.webp")
    st.image(img)
    st.empty()

st.markdown('___')

# ================= ABOUT SECTION =================
# Anchor untuk About
st.markdown("<div id='about'></div><br>", unsafe_allow_html=True)

st.header("About :red[Me]")
st.markdown('''Halo! Saya adalah seorang pengembang perangkat lunak yang berfokus pada pembuatan sistem informasi dan aplikasi web yang efisien. Selain berpengalaman dalam pengembangan *front-end* dan *back-end* menggunakan berbagai *framework* modern, saya juga memiliki pengalaman praktis di bidang *Data Science*, *Machine Learning*, dan *Internet of Things* (IoT). 

Saya berkomitmen untuk menghadirkan solusi teknologi yang bermanfaat, mulai dari digitalisasi manajemen institusi pendidikan hingga sistem otomasi perangkat keras. Saya senang mengeksplorasi teknologi terkini dan selalu berusaha memberikan hasil terbaik untuk setiap proyek yang saya kerjakan.''')

st.markdown('___')

# ================= SKILLS SECTION =================
# Anchor untuk Skills
st.markdown("<div id='skills'></div><br>", unsafe_allow_html=True)

st.header(":red[My] Skills")
st.markdown("""
- **Web Development & Server**: PHP, Laravel, Node.js, Streamlit, HTML/CSS. Berpengalaman mengelola server (Armbian, aaPanel, Apache, Nginx) dan *database* (Supabase).
- **Data Science & Machine Learning**: Python, Pandas. Menguasai implementasi algoritma seperti Naïve Bayes, K-Nearest Neighbors (KNN), Random Forest, dan Support Vector Machine (SVM).
- **IoT & Electronics**: C++, Arduino, pemrograman mikrokontroler ESP32, serta perakitan dan konfigurasi modul *hardware* elektronika.
""")

st.markdown('___')

# ================= PROJECTS SECTION =================
# Anchor untuk Projects
st.markdown("<div id='projects'></div><br>", unsafe_allow_html=True)

st.header("Pro:red[jects]")

# 1. Memasukkan CSS khusus untuk membuat wadah bisa di-scroll horizontal
st.markdown("""
<style>
/* Desain area scroll */
.scroll-wrapper {
    display: flex;
    overflow-x: auto;
    gap: 20px;
    padding-bottom: 15px;
}
/* Mempercantik tampilan scrollbar */
.scroll-wrapper::-webkit-scrollbar {
    height: 10px;
}
.scroll-wrapper::-webkit-scrollbar-track {
    background: #333; 
    border-radius: 10px;
}
.scroll-wrapper::-webkit-scrollbar-thumb {
    background: #ff4b4b; 
    border-radius: 10px;
}

/* Desain untuk setiap Kartu Proyek */
.card {
    flex: 0 0 320px; /* Lebar setiap kartu otomatis 320px */
    border: 1px solid #555;
    border-radius: 10px;
    padding: 15px;
    background-color: #1e1e1e; /* Warna latar belakang kartu */
    color: #fff;
}
.card h4 {
    margin-top: 0;
    color: #ff4b4b; /* Judul berwarna merah khas Streamlit */
    font-size: 18px;
}
/* Menyesuaikan ukuran gambar dan iframe agar pas di dalam kartu */
.card img, .card iframe {
    width: 100%;
    height: 180px;
    border-radius: 8px;
    object-fit: cover;
    border: none;
    margin-bottom: 15px;
}
.card p {
    font-size: 14px;
    line-height: 1.5;
    color: #ddd;
}
</style>
""", unsafe_allow_html=True)

# 2. Membuat Kartu Proyek dengan HTML
html_projects = """
<div class="scroll-wrapper">
    <div class="card">
        <h4>Sistem Manajemen Pesantren</h4>
        <img src="https://github.com/Muhsin-IT/Sistem-Rekomendasi-Kost/blob/main/Tampilan-Web-RadenStay.jpeg" alt="Siponpes">
        <p>Rekomendasi <i>Kost Mahasiswa</i> isi</p>
    </div>

    <div class="card">
        <h4>Sistem Tarhim dan Bel | IoT</h4>
        <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60" alt="IoT Tarhim">
        <p>Pemutar tarhim dan Bel terjadwal otomatis menggunakan mikrokontroler NodeMCU ESP8266, DFPlayer Mini, dan modul <i>relay</i> untuk mengontrol amplifier.</p>
        Link Github ""
    </div>

    <div class="card">
        <h4> Teka Teki Silang</h4>
        <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60" alt="IoT Tarhim">
        <p>Pemutar tarhim dan Bel terjadwal otomatis menggunakan mikrokontroler NodeMCU ESP8266, DFPlayer Mini, dan modul <i>relay</i> untuk mengontrol amplifier.</p>
        link github "https://github.com/Muhsin-IT/teka-teki-silang"
    </div>

    <div class="card">
        <h4>Platform Streaming "Nonime"</h4>
        <iframe src="https://anisora.web.id/" alt="Nonime">
        <p>Pengembangan antarmuka dan platform <i>website</i> untuk melakukan <i>streaming</i> dan menonton berbagai tayangan anime secara <i>online</i>.</p>
    </div>

</div>
"""

# Menampilkan HTML yang sudah dibuat ke layar
st.markdown(html_projects, unsafe_allow_html=True)

st.markdown('___')

# ================= CONTACT SECTION =================
# Anchor untuk Contact
st.markdown("<div id='contact'></div><br>", unsafe_allow_html=True)

st.header("Contact")

kolom1, kolom2, kolom3 = st.columns([1,1,1])

with kolom1:
    img = Image.open("instagram.png")
    st.image(img, width=60)
    st.write("[:red[Instagram]](https://www.instagram.com/mad_muhsin/)")

with kolom2:
    img = Image.open("facebook.png")
    st.image(img, width=60)
    st.write("[:red[Facebook]](https://www.facebook.com/)")

with kolom3:
    img = Image.open("dribbble.png") 
    st.image(img, width=60)
    st.write("[:red[Github]](https://github.com/Muhsin-IT)")