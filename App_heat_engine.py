import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Heat Engine Builder", page_icon="🔥", layout="wide")

# CSS Tambahan untuk Styling ala Kartu/Dashboard
st.markdown("""
<style>
    .main-title {
        font-size: 38px;
        font-weight: bold;
        color: #FF4B4B;
        text-align: center;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #555;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigasi Utama
st.sidebar.markdown("### 🧭 Navigasi Menu")
menu = st.sidebar.radio("Pilih Menu:", [
    "1. Halaman Utama", 
    "2. Merakit Mesin",
    "3. Pilih Level & Mesin", 
    "4. Kalkulator & Diagram P-V/T-S", 
    "5. Tantangan & Skor Interaktif"
])

if menu == "1. Halaman Utama":
    st.markdown('<div class="main-title">🔥 HEAT ENGINE BUILDER</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Simulasi Interaktif Mesin Kalor & Termodinamika</div>', unsafe_allow_html=True)
    st.write("---")
    st.info("💡 **Petunjuk:** Gunakan menu navigasi di sebelah kiri untuk mulai merakit mesin, menghitung efisiensi, melihat diagram siklus, atau menguji tantangan interaktif.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("📚 Belajar")
        st.write("Pelajari siklus Carnot, Stirling, dan Diesel melalui konsep teoretis.")
    with col2:
        st.subheader("🎮 Bermain")
        st.write("Susun urutan proses termodinamika dengan benar dan kumpulkan skor tertinggi.")
    with col3:
        st.subheader("📊 Hitung")
        st.write("Analisis perhitungan kerja, kalor, dan efisiensi termal secara real-time.")
 
elif menu == "2. Merakit Mesin":
    st.markdown("## 🛠️ Stasiun Perakitan Puzzle Mesin Kalor")
    st.markdown("Seret atau pasangkan komponen modular ke dalam slot rangka mesin yang kosong. Lengkapi semua slot puzzle untuk menyalakan mesin!")

    # Inisialisasi session state untuk puzzle rakitan
    if 'puzzle_piston' not in st.session_state:
        st.session_state.puzzle_piston = "Belum Terpasang"
    if 'puzzle_valve' not in st.session_state:
        st.session_state.puzzle_valve = "Belum Terpasang"
    if 'puzzle_fluid' not in st.session_state:
        st.session_state.puzzle_fluid = "Belum Terpasang"
    if 'puzzle_selesai' not in st.session_state:
        st.session_state.puzzle_selesai = False

    # Layout Bagian Inventaris Komponen & Slot Puzzle Mesin
    col_inv, col_board = st.columns([1, 1], gap="medium")

    with col_inv:
        with st.container(border=True):
            st.markdown("### 🧰 Kotak Suku Cadang (Part Inventory)")
            st.markdown("Pilih komponen untuk dipasang ke slot mesin:")
            
            # Pilihan Piston
            piston_pick = st.selectbox(
                "🧱 Pilih Suku Cadang Piston:",
                ["Pilih...", "Piston Silinder Standar", "Piston Kompresi Tinggi"],
                key="pick_piston"
            )
            if st.button("Pasang Piston ke Slot 1", use_container_width=True):
                if piston_pick != "Pilih...":
                    st.session_state.puzzle_piston = piston_pick
                    st.success(f"Berhasil memasang: {piston_pick}")
                else:
                    st.warning("Pilih jenis piston terlebih dahulu!")

            st.write("---")

            # Pilihan Katup
            valve_pick = st.selectbox(
                "⚙️ Pilih Suku Cadang Katup:",
                ["Pilih...", "Katup Otomatis (Check Valve)", "Katup Masuk/Buang Ganda"],
                key="pick_valve"
            )
            if st.button("Pasang Katup ke Slot 2", use_container_width=True):
                if valve_pick != "Pilih...":
                    st.session_state.puzzle_valve = valve_pick
                    st.success(f"Berhasil memasang: {valve_pick}")
                else:
                    st.warning("Pilih sistem katup terlebih dahulu!")

            st.write("---")

            # Pilihan Fluida
            fluid_pick = st.selectbox(
                "🧪 Pilih Suku Cadang Fluida:",
                ["Pilih...", "Gas Ideal (Udara)", "Uap Bertekanan (Steam)"],
                key="pick_fluid"
            )
            if st.button("Pasang Fluida ke Slot 3", use_container_width=True):
                if fluid_pick != "Pilih...":
                    st.session_state.puzzle_fluid = fluid_pick
                    st.success(f"Berhasil memasang: {fluid_pick}")
                else:
                    st.warning("Pilih jenis fluida terlebih dahulu!")

    with col_board:
        with st.container(border=True):
            st.markdown("### 🧩 Papan Rangka Mesin (Assembly Slot)")
            st.markdown("Status slot komponen pada rangka utama:")
            
            # Tampilan Status Slot Puzzle
            slot1_color = "🟢" if st.session_state.puzzle_piston != "Belum Terpasang" else "🔴"
            slot2_color = "🟢" if st.session_state.puzzle_valve != "Belum Terpasang" else "🔴"
            slot3_color = "🟢" if st.session_state.puzzle_fluid != "Belum Terpasang" else "🔴"
            
            st.markdown(f"{slot1_color} **Slot 1 (Piston):** {st.session_state.puzzle_piston}")
            st.markdown(f"{slot2_color} **Slot 2 (Katup):** {st.session_state.puzzle_valve}")
            st.markdown(f"{slot3_color} **Slot 3 (Fluida):** {st.session_state.puzzle_fluid}")
            
            st.write("---")
            
            # Tombol Reset Puzzle
            if st.button("🔄 Bongkar / Reset Puzzle", use_container_width=True):
                st.session_state.puzzle_piston = "Belum Terpasang"
                st.session_state.puzzle_valve = "Belum Terpasang"
                st.session_state.puzzle_fluid = "Belum Terpasang"
                st.session_state.puzzle_selesai = False
                st.rerun()

            # Tombol Periksa & Nyalakan Mesin
            if st.button("🚀 Kunci Rakitan & Nyalakan Mesin", use_container_width=True, type="primary"):
                if (st.session_state.puzzle_piston != "Belum Terpasang" and 
                    st.session_state.puzzle_valve != "Belum Terpasang" and 
                    st.session_state.puzzle_fluid != "Belum Terpasang"):
                    st.session_state.puzzle_selesai = True
                    st.balloons()
                else:
                    st.session_state.puzzle_selesai = False
                    st.error("⚠️ Puzzle Belum Lengkap! Pastikan Slot 1, Slot 2, dan Slot 3 semuanya sudah terpasang komponen.")

    # Jika semua puzzle slot sudah lengkap dan diaktifkan, tampilkan animasi mesin bergerak
    if st.session_state.puzzle_selesai:
        st.success("🎉 Puzzle Sempurna! Komponen terkunci pada rangka. Mesin modern sedang beroperasi!")
        
        with st.container(border=True):
            st.markdown("### ⚙️ Visualisasi Mesin Kalor Bergerak (Hasil Rakitan Puzzle)")
            
            import streamlit.components.v1 as components
            
            modern_engine_html = f"""
            <div style="background: linear-gradient(135deg, #101015, #1e1e2f); padding: 20px; border-radius: 16px; color: white; font-family: 'Poppins', sans-serif; text-align: center; box-shadow: 0 8px 24px rgba(0,0,0,0.5);">
                <h3 style="margin-top: 0; color: #00f2fe; font-size: 18px; font-weight: 600;">Simulasi Mesin Kalor Modular Modern</h3>
                <p style="font-size: 13px; color: #b0b0d0; margin-bottom: 12px;">Konfigurasi Rakitan: <b>{st.session_state.puzzle_piston}</b> | <b>{st.session_state.puzzle_valve}</b> | <b>{st.session_state.puzzle_fluid}</b></p>
                
                <svg width="200" height="210" viewBox="0 0 200 210" style="margin: 0 auto; display: block; background: #08080c; border-radius: 12px; border: 2px solid #00f2fe;">
                    <rect x="25" y="10" width="150" height="160" rx="10" ry="10" stroke="#00f2fe" stroke-width="2.5" fill="none"/>
                    <g>
                        <defs>
                            <linearGradient id="pGr" x1="0%" y1="0%" x2="0%" y2="100%">
                                <stop offset="0%" style="stop-color:#bdc3c7;stop-opacity:1" />
                                <stop offset="100%" style="stop-color:#2c3e50;stop-opacity:1" />
                            </linearGradient>
                        </defs>
                        <rect x="35" y="20" width="130" height="40" rx="6" ry="6" fill="url(#pGr)" stroke="#fff" stroke-width="1">
                            <animateTransform 
                                attributeName="transform"
                                type="translate"
                                from="0,0" to="0,85"
                                dur="1.2s"
                                repeatCount="indefinite"
                                calcMode="spline"
                                keyTimes="0; 0.5; 1"
                                keySplines="0.42 0 0.58 1; 0.42 0 0.58 1"
                                additive="sum"
                            />
                        </rect>
                        <rect x="85" y="60" width="30" height="95" fill="#7f8c8d">
                            <animateTransform 
                                attributeName="transform"
                                type="translate"
                                from="0,0" to="0,85"
                                dur="1.2s"
                                repeatCount="indefinite"
                                calcMode="spline"
                                keyTimes="0; 0.5; 1"
                                keySplines="0.42 0 0.58 1; 0.42 0 0.58 1"
                                additive="sum"
                            />
                        </rect>
                    </g>
                </svg>
                
                <div style="display: flex; justify-content: space-around; margin-top: 12px; font-size: 12px; color: #ff6b6b; font-weight: 500; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 8px;">
                    <span>🔥 Suhu: Stabil</span>
                    <span>⚡ Tekanan: Dinamis</span>
                    <span>🔄 Siklus: Aktif</span>
                </div>
            </div>
            """
            components.html(modern_engine_html, height=460)
            
            st.write("---")
            
            col_res1, col_res2, col_res3 = std_cols = st.columns(3) if 'std_cols' not in locals() else st.columns(3)
            with col_res1:
                st.metric("Pilihan Piston", st.session_state.puzzle_piston)
            with col_res2:
                st.metric("Pilihan Katup", st.session_state.puzzle_valve)
            with col_res3:
                st.metric("Jenis Fluida", st.session_state.puzzle_fluid)
                    
            st.info("✨ **Status:** Mesin rakitan puzzle berjalan optimal. Silakan lanjut ke menu **Kalkulator & Diagram** untuk menghitung efisiensinya!")

elif menu == "3. Pilih Level & Mesin":
    st.markdown("## ⚙️ Pilih Jenis Mesin & Level Pembelajaran")
    st.write("Eksplorasi karakteristik termodinamika dari berbagai jenis siklus mesin kalor.")
    
    # Menggunakan layout tab atau 4 kolom rapi untuk pilihan siklus
    col_c1, col_c2 = st.columns(2)
    
    with col_c1:
        with st.container(border=True):
            st.markdown("### 🥇 Level 1: Siklus Carnot")
            st.write("Siklus teoretis ideal dengan efisiensi maksimum yang terdiri dari 2 proses isotermal dan 2 proses adiabatik.")
            if st.button("Aktifkan Level Carnot", key="b_carnot"):
                st.success("✅ Level Carnot diaktifkan! Silakan uji efisiensinya di Kalkulator.")
                
        with st.container(border=True):
            st.markdown("### 🚗 Level 2: Siklus Otto")
            st.write("Siklus pembakaran internal (mesin bensin) di mana proses pemasukan kalor terjadi pada volume konstan ($V$ konstan).")
            if st.button("Aktifkan Level Otto", key="b_otto"):
                st.success("✅ Level Otto diaktifkan!")

    with col_c2:
        with st.container(border=True):
            st.markdown("### 🚚 Level 3: Level Diesel")
            st.write("Siklus pembakaran internal dengan proses pemasukan kalor pada tekanan konstan ($P$ konstan) dan rasio kompresi tinggi.")
            if st.button("Aktifkan Level Diesel", key="b_diesel"):
                st.success("✅ Level Diesel diaktifkan!")
                
        with st.container(border=True):
            st.markdown("### 🔄 Level 4: Siklus Stirling (Eksternal)")
            st.write("Mesin pembakaran eksternal menggunakan regenerator termal dengan siklus kompresi dan ekspansi gas pada suhu konstan.")
            if st.button("Aktifkan Level Stirling", key="b_stirling"):
                st.success("✅ Level Stirling diaktifkan! (Cocok untuk animasi mesin bergerak).")

elif menu == "4. Kalkulator & Diagram P-V/T-S":
    st.markdown("## 📊 Kalkulator Kinerja & Diagram Siklus Termodinamika")
    st.write("Hitung efisiensi termal dan analisis grafik siklus secara dinamis.")
    
    col_input, col_result = st.columns([1, 1])
    
    with col_input:
        with st.container(border=True):
            st.markdown("### 📥 Parameter Input Suhu")
            Th = st.number_input("Suhu Reservoir Panas ($T_H$) dalam Kelvin", value=600.0, step=10.0, key="th_calc")
            Tc = st.number_input("Suhu Reservoir Dingin ($T_C$) dalam Kelvin", value=300.0, step=10.0, key="tc_calc")
            
    with col_result:
        with st.container(border=True):
            st.markdown("### 📤 Hasil Analisis Efisiensi")
            if Th > Tc and Tc > 0:
                efficiency = 1 - (Tc / Th)
                st.latex(r"\eta = 1 - \frac{T_c}{T_h}")
                st.markdown(rf"#### Efisiensi Termal ($\eta$) = **{efficiency * 100:.1f}%**")
                if efficiency > 0.5:
                    st.success("🌟 Performa mesin sangat tinggi dan efisien!")
                else:
                    st.info("💡 Performa standar untuk siklus termal konvensional.")
            else:
                st.error(r"⚠️ Pastikan $T_H > T_C > 0$ Kelvin!")

    st.write("---")
    st.markdown("### 📈 Visualisasi Kurva Diagram P-V & T-S Berdasarkan Siklus")
    
    # Pilihan siklus termasuk Siklus Diesel
    pilihan_siklus_grafik = st.selectbox(
        "Pilih Jenis Siklus yang Ingin Ditampilkan pada Grafik:",
        ["Siklus Carnot (Ideal)", "Siklus Otto (Mesin Bensin)", "Siklus Diesel (Mesin Berat)", "Siklus Stirling"]
    )
    
    import matplotlib.pyplot as plt
    import numpy as np
    
    # Membuat dua kolom grafik berdampingan (P-V dan T-S)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    if pilihan_siklus_grafik == "Siklus Carnot (Ideal)":
        # Kurva P-V Carnot
        v = np.linspace(1, 4, 100)
        p = 10 / v
        ax1.plot(v, p, 'r-', linewidth=2, label="Isotermal Ekspansi (1-2)")
        ax1.plot([4, 4], [2.5, 1.25], 'orange', linewidth=2, label="Adiabatik Ekspansi (2-3)")
        ax1.plot(v[::-1], p/2, 'b-', linewidth=2, label="Isotermal Kompresi (3-4)")
        ax1.plot([1, 1], [1.25, 10], 'g--', linewidth=2, label="Adiabatik Kompresi (4-1)")
        ax1.set_title("Diagram P-V Carnot")
        ax1.set_xlabel("Volume ($V$)")
        ax1.set_ylabel("Tekanan ($P$)")
        ax1.legend(loc="upper right", fontsize=7)
        ax1.grid(True, linestyle=":", alpha=0.6)
        
        # Kurva T-S Carnot
        s = [1, 2, 2, 1, 1]
        t = [Th, Th, Tc, Tc, Th]
        ax2.plot(s, t, 'purple', linewidth=2.5, marker='o')
        ax2.set_title("Diagram T-S Carnot")
        ax2.set_xlabel("Entropi ($S$)")
        ax2.set_ylabel("Suhu ($T$)")
        ax2.grid(True, linestyle=":", alpha=0.6)

    elif pilihan_siklus_grafik == "Siklus Otto (Mesin Bensin)":
        # Kurva P-V Otto
        v = np.linspace(1, 3, 100)
        p_exp = 8 / (v**1.4)
        ax1.plot(v, p_exp, 'r-', linewidth=2, label="Adiabatik Ekspansi")
        ax1.plot([3, 3], [1.5, 4.5], 'orange', linewidth=2, label="Pemasukan Kalor (V konstan)")
        ax1.plot(v[::-1], 8 / (v**1.4), 'b-', linewidth=2, label="Adiabatik Kompresi")
        ax1.plot([1, 1], [8, 2.6], 'g--', linewidth=2, label="Pembuangan Kalor (V konstan)")
        ax1.set_title("Diagram P-V Siklus Otto")
        ax1.set_xlabel("Volume ($V$)")
        ax1.set_ylabel("Tekanan ($P$)")
        ax1.legend(loc="upper right", fontsize=7)
        ax1.grid(True, linestyle=":", alpha=0.6)
        
        # Kurva T-S Otto
        s = [1, 2, 2, 1, 1]
        t = [Tc, Th * 0.8, Th, Tc * 1.2, Tc]
        ax2.plot(s, t, 'brown', linewidth=2.5, marker='s')
        ax2.set_title("Diagram T-S Siklus Otto")
        ax2.set_xlabel("Entropi ($S$)")
        ax2.set_ylabel("Suhu ($T$)")
        ax2.grid(True, linestyle=":", alpha=0.6)

    elif pilihan_siklus_grafik == "Siklus Diesel (Mesin Berat)":
        # Kurva P-V Diesel (Ada proses tekanan konstan / isobaric expansion)
        v = np.linspace(1, 3.5, 100)
        ax1.plot(v, 9 / (v**1.4), 'r-', linewidth=2, label="Adiabatik Ekspansi")
        ax1.plot([1.5, 2.5], [4, 4], 'orange', linewidth=2, label="Pemasukan Kalor (P konstan)")
        ax1.plot(v[::-1], 9 / (v**1.4), 'b-', linewidth=2, label="Adiabatik Kompresi")
        ax1.plot([1, 1], [3, 9], 'g--', linewidth=2, label="Pembuangan Kalor (V konstan)")
        ax1.set_title("Diagram P-V Siklus Diesel")
        ax1.set_xlabel("Volume ($V$)")
        ax1.set_ylabel("Tekanan ($P$)")
        ax1.legend(loc="upper right", fontsize=7)
        ax1.grid(True, linestyle=":", alpha=0.6)
        
        # Kurva T-S Diesel
        s = [1, 1.8, 2.3, 1.2, 1]
        t = [Tc, Th * 0.9, Th, Tc * 1.1, Tc]
        ax2.plot(s, t, 'darkgreen', linewidth=2.5, marker='^')
        ax2.set_title("Diagram T-S Siklus Diesel")
        ax2.set_xlabel("Entropi ($S$)")
        ax2.set_ylabel("Suhu ($T$)")
        ax2.grid(True, linestyle=":", alpha=0.6)

    else:
        # Kurva P-V Stirling
        v = np.linspace(1, 3, 100)
        ax1.plot(v, 6/v, 'r-', linewidth=2, label="Isotermal Ekspansi")
        ax1.plot([3, 3], [2, 4], 'orange', linewidth=2, label="Regenerasi (V konstan)")
        ax1.plot(v[::-1], 3/v, 'b-', linewidth=2, label="Isotermal Kompresi")
        ax1.plot([1, 1], [1, 3], 'g--', linewidth=2, label="Regenerasi (V konstan)")
        ax1.set_title("Diagram P-V Siklus Stirling")
        ax1.set_xlabel("Volume ($V$)")
        ax1.set_ylabel("Tekanan ($P$)")
        ax1.legend(loc="upper right", fontsize=7)
        ax1.grid(True, linestyle=":", alpha=0.6)
        
        # Kurva T-S Stirling
        s = np.linspace(1, 2, 100)
        ax2.plot(s, [Th]*100, 'r-', linewidth=2, label="Suhu Tinggi ($T_H$)")
        ax2.plot([2, 2], [Th, Tc], 'orange', linewidth=2)
        ax2.plot(s[::-1], [Tc]*100, 'b-', linewidth=2, label="Suhu Rendah ($T_C$)")
        ax2.plot([1, 1], [Tc, Th], 'g--', linewidth=2)
        ax2.set_title("Diagram T-S Siklus Stirling")
        ax2.set_xlabel("Entropi ($S$)")
        ax2.set_ylabel("Suhu ($T$)")
        ax2.legend(loc="upper right", fontsize=7)
        ax2.grid(True, linestyle=":", alpha=0.6)

    plt.tight_layout()
    st.pyplot(fig)

elif menu == "5. Tantangan & Skor Interaktif":
    st.markdown("## 🎮 Tantangan & Kuis Termodinamika Multi-Soal")
    st.write("Uji pemahaman Anda melalui berbagai tantangan urutan siklus dan kuis konsep termodinamika untuk mengumpulkan skor tertinggi!")
    
    # Inisialisasi session_state untuk skor dan nyawa
    if 'score' not in st.session_state:
        st.session_state.score = 250
    if 'lives' not in st.session_state:
        st.session_state.lives = 3

    with st.container(border=True):
        st.markdown(f"### ❤️ Nyawa: {'❤️' * st.session_state.lives} &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 🌟 Total Skor: {st.session_state.score}")
        st.write("---")
        
        # Pilihan jenis tantangan atau soal
        pilihan_tantangan = st.selectbox(
            "Pilih Soal / Tantangan:",
            [
                "Pilih tantangan...",
                "Tantangan 1: Susun Urutan Proses Siklus Carnot",
                "Kuis 1: Hukum Kedua Termodinamika",
                "Kuis 2: Faktor yang Mempengaruhi Efisiensi Mesin Carnot",
                "Kuis 3: Karakteristik Siklus Otto"
            ]
        )
        
        st.write("---")
        
        # 1. Tantangan Menyusun Urutan Carnot
        if pilihan_tantangan == "Tantangan 1: Susun Urutan Proses Siklus Carnot":
            st.markdown("#### 🧩 Tantangan 1: Susun 4 Tahapan Siklus Carnot")
            p1 = st.selectbox("Proses 1 (Tahap Awal):", ["Pilih proses...", "Isotermal Ekspansi", "Adiabatik Ekspansi", "Isotermal Kompresi", "Adiabatik Kompresi"], key="t1")
            p2 = st.selectbox("Proses 2:", ["Pilih proses...", "Isotermal Ekspansi", "Adiabatik Ekspansi", "Isotermal Kompresi", "Adiabatik Kompresi"], key="t2")
            p3 = st.selectbox("Proses 3:", ["Pilih proses...", "Isotermal Ekspansi", "Adiabatik Ekspansi", "Isotermal Kompresi", "Adiabatik Kompresi"], key="t3")
            p4 = st.selectbox("Proses 4 (Tahap Akhir):", ["Pilih proses...", "Isotermal Ekspansi", "Adiabatik Ekspansi", "Isotermal Kompresi", "Adiabatik Kompresi"], key="t4")
            
            if st.button("Cek Jawaban Tantangan 1"):
                kunci = ["Isotermal Ekspansi", "Adiabatik Ekspansi", "Isotermal Kompresi", "Adiabatik Kompresi"]
                if [p1, p2, p3, p4] == kunci:
                    st.success("🎉 Luar biasa! Urutan benar. Skor Anda bertambah +100.")
                    st.session_state.score += 100
                    st.balloons()
                else:
                    st.error("❌ Urutan proses belum tepat. Silakan coba lagi!")
                    st.session_state.lives = max(0, st.session_state.lives - 1)

        # 2. Kuis Soal 1
        elif pilihan_tantangan == "Kuis 1: Hukum Kedua Termodinamika":
            st.markdown("#### 📝 Kuis 1: Konsep Hukum II Termodinamika")
            ans_q1 = st.radio(
                "Pernyataan manakah yang menyatakan Hukum Kedua Termodinamika (Pernyataan Kelvin-Planck)?",
                [
                    "Pilih jawaban...",
                    "Energi total di alam semesta selalu berkurang seiring waktu.",
                    "Tidak mungkin membuat mesin kalor yang bekerja dalam suatu siklus yang mengubah semua kalor yang diserap menjadi usaha seluruhnya.",
                    "Kalor mengalir secara spontan dari suhu rendah ke suhu tinggi."
                ],
                key="q1"
            )
            if st.button("Kirim Jawaban Kuis 1"):
                if "Tidak mungkin membuat mesin kalor" in ans_q1:
                    st.success("🎉 Benar sekali! Poin Anda bertambah +50.")
                    st.session_state.score += 50
                    st.balloons()
                elif ans_q1 == "Pilih jawaban...":
                    st.warning("⚠️ Silakan pilih opsi jawaban terlebih dahulu.")
                else:
                    st.error("❌ Kurang tepat. Coba tinjau kembali konsep dasar mesin kalor.")
                    st.session_state.lives = max(0, st.session_state.lives - 1)

        # 3. Kuis Soal 2
        elif pilihan_tantangan == "Kuis 2: Faktor yang Mempengaruhi Efisiensi Mesin Carnot":
            st.markdown("#### 📝 Kuis 2: Efisiensi Mesin Carnot")
            ans_q2 = st.radio(
                "Bagaimana cara paling efektif untuk meningkatkan efisiensi teoretis dari sebuah Mesin Carnot?",
                [
                    "Pilih jawaban...",
                    "Menurunkan suhu reservoir panas ($T_H$) sekecil mungkin.",
                    "Menaikkan suhu reservoir panas ($T_H$) atau menurunkan suhu reservoir dingin ($T_C$).",
                    "Memperbesar ukuran fisik silinder mesin tanpa mengubah suhu."
                ],
                key="q2"
            )
            if st.button("Kirim Jawaban Kuis 2"):
                if "Menaikkan suhu reservoir panas" in ans_q2:
                    st.success("🎉 Tepat! Efisiensi bergantung langsung pada suhu reservoir panas dan dingin. Skor bertambah +50.")
                    st.session_state.score += 50
                    st.balloons()
                elif ans_q2 == "Pilih jawaban...":
                    st.warning("⚠️ Silakan pilih opsi jawaban terlebih dahulu.")
                else:
                    st.error("❌ Kurang tepat. Perhatikan rumus efisiensi Carnot ($\eta = 1 - T_C/T_H$).")
                    st.session_state.lives = max(0, st.session_state.lives - 1)

        # 4. Kuis Soal 3
        elif pilihan_tantangan == "Kuis 3: Karakteristik Siklus Otto":
            st.markdown("#### 📝 Kuis 3: Siklus Otto (Mesin Pembakaran Internal)")
            ans_q3 = st.radio(
                "Pada siklus Otto ideal (yang digunakan pada mesin bensin kendaraan), proses pemasukan kalor (pembakaran) terjadi pada kondisi apa?",
                [
                    "Pilih jawaban...",
                    "Tekanan konstan (Isobarik)",
                    "Volume konstan (Isokhorik / Isovolumetrik)",
                    "Suhu konstan (Isotermal)"
                ],
                key="q3"
            )
            if st.button("Kirim Jawaban Kuis 3"):
                if "Volume konstan" in ans_q3:
                    st.success("🎉 Betul! Proses pembakaran pada siklus Otto diasumsikan terjadi pada volume konstan. Skor bertambah +50.")
                    st.session_state.score += 50
                    st.balloons()
                elif ans_q3 == "Pilih jawaban...":
                    st.warning("⚠️ Silakan pilih opsi jawaban terlebih dahulu.")
                else:
                    st.error("❌ Belum tepat. Ingat kembali karakteristik siklus pembakaran internal bensin.")
                    st.session_state.lives = max(0, st.session_state.lives - 1)
        
        else:
            st.info("👆 Silakan pilih salah satu tantangan atau kuis pada menu dropdown di atas untuk mulai bermain.")

        st.write("---")
        st.markdown("### 🏅 Papan Peringkat (Leaderboard Pemain)")
        nama_pemain = st.text_input("Masukkan Nama Anda untuk Masuk Papan Peringkat:", placeholder="Ketik nama Anda di sini...")

        if nama_pemain.strip() != "":
            st.markdown(f"""
            | Peringkat | Nama Pengguna | Total Skor | Keterangan |
            | :---: | :--- | :---: | :--- |
            | 1 | **{nama_pemain}** | **{st.session_state.score}** | **Master Termodinamika** |
            """)
        else:
            st.info("💡 Ketik nama Anda di atas untuk mencatatkan total skor ke papan peringkat.")