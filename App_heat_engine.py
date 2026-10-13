import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

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
    "3. Pilih Level, Teori & Rumus Siklus", 
    "4. Kalkulator & Diagram P-V/T-S", 
    "5. Tantangan & Skor Interaktif"
])

if menu == "1. Halaman Utama":
    st.markdown('<div class="main-title">🔥 HEAT ENGINE BUILDER</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Simulasi Interaktif Mesin Kalor & Termodinamika</div>', unsafe_allow_html=True)
    st.write("---")
    st.info("💡 **Petunjuk:** Gunakan menu navigasi di sebelah kiri untuk mulai merakit mesin per siklus, mempelajari materi teoretis lengkap beserta rumus, menghitung efisiensi, melihat diagram, atau menguji tantangan interaktif.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("📚 Belajar")
        st.write("Pelajari siklus Carnot, Otto, Diesel, dan Stirling melalui konsep teoretis dan rumus matematis.")
    with col2:
        st.subheader("🎮 Bermain")
        st.write("Susun puzzle komponen mesin per siklus dan kumpulkan skor tertinggi.")
    with col3:
        st.subheader("📊 Hitung")
        st.write("Analisis perhitungan kerja, kalor, dan efisiensi termal secara real-time.")
 
elif menu == "2. Merakit Mesin":
    st.markdown("## 🛠️ Stasiun Perakitan Puzzle Mesin Kalor Berdasarkan Siklus")
    st.markdown("Pilih jenis siklus mesin, lalu pilih dan pasang komponen modular yang tepat untuk menyusun puzzle perakitan!")

    pilihan_siklus_puzzle = st.selectbox(
        "🔧 Pilih Jenis Siklus untuk Dirakit:",
        ["Siklus Carnot (Ideal)", "Siklus Otto (Mesin Bensin)", "Siklus Diesel (Mesin Solar)", "Siklus Stirling (Eksternal)"]
    )

    if 'puzzle_piston' not in st.session_state:
        st.session_state.puzzle_piston = "Belum Terpasang"
    if 'puzzle_valve' not in st.session_state:
        st.session_state.puzzle_valve = "Belum Terpasang"
    if 'puzzle_fluid' not in st.session_state:
        st.session_state.puzzle_fluid = "Belum Terpasang"
    if 'puzzle_selesai' not in st.session_state:
        st.session_state.puzzle_selesai = False

    col_inv, col_board = st.columns([1, 1], gap="medium")

    with col_inv:
        with st.container(border=True):
            st.markdown("### 🧰 Kotak Suku Cadang (Part Inventory)")
            st.markdown(f"Pilih komponen khusus untuk **{pilihan_siklus_puzzle}**:")
            
            if "Carnot" in pilihan_siklus_puzzle:
                piston_options = ["Pilih...", "Piston Reversibel Isotermal (Valid)", "Piston Standar"]
                valve_options = ["Pilih...", "Reservoir Suhu Tinggi & Rendah (Valid)", "Busi"]
                fluid_options = ["Pilih...", "Gas Ideal Murni (Valid)", "Solar Cair"]
            elif "Otto" in pilihan_siklus_puzzle:
                piston_options = ["Pilih...", "Piston Silinder Standar Kompresi Sedang (Valid)", "Piston Displacer"]
                valve_options = ["Pilih...", "Busi / Spark Plug & Katup Isap-Buang (Valid)", "Injektor"]
                fluid_options = ["Pilih...", "Campuran Bahan Bakar Bensin & Udara (Valid)", "Gas Helium"]
            elif "Diesel" in pilihan_siklus_puzzle:
                piston_options = ["Pilih...", "Piston Kompresi Tinggi Heavy Duty (Valid)", "Piston Ringan"]
                valve_options = ["Pilih...", "Injektor Solar Bertekanan Tinggi (Valid)", "Busi Standar"]
                fluid_options = ["Pilih...", "Solar & Udara Murni Terkompresi (Valid)", "Gas Ideal Murni"]
            else:
                piston_options = ["Pilih...", "Piston Daya & Piston Displacer Terpisah (Valid)", "Piston Tunggal"]
                valve_options = ["Pilih...", "Matriks Regenerator Eksternal (Valid)", "Injektor Solar"]
                fluid_options = ["Pilih...", "Gas Helium / Hidrogen Tertutup (Valid)", "Bensin"]

            piston_pick = st.selectbox("🧱 Pilih Suku Cadang Piston:", piston_options, key="pick_piston")
            if st.button("Pasang Piston ke Slot 1", use_container_width=True):
                if piston_pick != "Pilih...":
                    st.session_state.puzzle_piston = piston_pick
                    st.success(f"Berhasil memasang: {piston_pick}")
                else:
                    st.warning("Pilih jenis piston terlebih dahulu!")

            st.write("---")

            valve_pick = st.selectbox("⚙️ Pilih Suku Cadang Katup / Penukar:", valve_options, key="pick_valve")
            if st.button("Pasang Katup ke Slot 2", use_container_width=True):
                if valve_pick != "Pilih...":
                    st.session_state.puzzle_valve = valve_pick
                    st.success(f"Berhasil memasang: {valve_pick}")
                else:
                    st.warning("Pilih sistem katup/penukar terlebih dahulu!")

            st.write("---")

            fluid_pick = st.selectbox("🧪 Pilih Suku Cadang Fluida:", fluid_options, key="pick_fluid")
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
            
            slot1_color = "🟢" if st.session_state.puzzle_piston != "Belum Terpasang" else "🔴"
            slot2_color = "🟢" if st.session_state.puzzle_valve != "Belum Terpasang" else "🔴"
            slot3_color = "🟢" if st.session_state.puzzle_fluid != "Belum Terpasang" else "🔴"
            
            st.markdown(f"{slot1_color} **Slot 1 (Piston):** {st.session_state.puzzle_piston}")
            st.markdown(f"{slot2_color} **Slot 2 (Katup):** {st.session_state.puzzle_valve}")
            st.markdown(f"{slot3_color} **Slot 3 (Fluida):** {st.session_state.puzzle_fluid}")
            
            st.write("---")
            
            if st.button("🔄 Bongkar / Reset Puzzle", use_container_width=True):
                st.session_state.puzzle_piston = "Belum Terpasang"
                st.session_state.puzzle_valve = "Belum Terpasang"
                st.session_state.puzzle_fluid = "Belum Terpasang"
                st.session_state.puzzle_selesai = False
                st.rerun()

            if st.button("🚀 Kunci Rakitan & Nyalakan Mesin", use_container_width=True, type="primary"):
                p_val = st.session_state.puzzle_piston
                v_val = st.session_state.puzzle_valve
                f_val = st.session_state.puzzle_fluid
                
                is_correct_match = False
                if "Carnot" in pilihan_siklus_puzzle and "Valid" in p_val and "Valid" in v_val and "Valid" in f_val:
                    is_correct_match = True
                elif "Otto" in pilihan_siklus_puzzle and "Valid" in p_val and "Valid" in v_val and "Valid" in f_val:
                    is_correct_match = True
                elif "Diesel" in pilihan_siklus_puzzle and "Valid" in p_val and "Valid" in v_val and "Valid" in f_val:
                    is_correct_match = True
                elif "Stirling" in pilihan_siklus_puzzle and "Valid" in p_val and "Valid" in v_val and "Valid" in f_val:
                    is_correct_match = True

                if is_correct_match:
                    st.session_state.puzzle_selesai = True
                    st.balloons()
                else:
                    st.session_state.puzzle_selesai = False
                    st.error(f"⚠️ Komponen puzzle belum lengkap atau keliru/tidak sesuai dengan karakteristik **{pilihan_siklus_puzzle}**!")

    if st.session_state.puzzle_selesai:
        st.success(f"🎉 Puzzle Sempurna untuk {pilihan_siklus_puzzle}! Mesin modern sedang beroperasi!")
        with st.container(border=True):
            st.markdown("### ⚙️ Visualisasi Mesin Kalor Bergerak (Animasi SVG Modern)")
            import streamlit.components.v1 as components
            modern_engine_html = f"""
            <div style="background: linear-gradient(135deg, #101015, #1e1e2f); padding: 20px; border-radius: 16px; color: white; font-family: 'Poppins', sans-serif; text-align: center; box-shadow: 0 8px 24px rgba(0,0,0,0.5);">
                <h3 style="margin-top: 0; color: #00f2fe; font-size: 18px; font-weight: 600;">Simulasi {pilihan_siklus_puzzle}</h3>
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
                            <animateTransform attributeName="transform" type="translate" from="0,0" to="0,85" dur="1.2s" repeatCount="indefinite" calcMode="spline" keyTimes="0; 0.5; 1" keySplines="0.42 0 0.58 1; 0.42 0 0.58 1" additive="sum"/>
                        </rect>
                        <rect x="85" y="60" width="30" height="95" fill="#7f8c8d">
                            <animateTransform attributeName="transform" type="translate" from="0,0" to="0,85" dur="1.2s" repeatCount="indefinite" calcMode="spline" keyTimes="0; 0.5; 1" keySplines="0.42 0 0.58 1; 0.42 0 0.58 1" additive="sum"/>
                        </rect>
                    </g>
                </svg>
            </div>
            """
            components.html(modern_engine_html, height=460)

elif menu == "3. Pilih Level, Teori & Rumus Siklus":
    st.markdown("## 📚 Level, Penjelasan Teori Komprehensif & Rumus Masing-Masing Siklus")
    st.write("Pelajari materi teoretis, karakteristik tahapan proses, serta persamaan matematis eksak untuk ke-4 siklus termodinamika.")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Siklus Carnot", "Siklus Otto", "Siklus Diesel", "Siklus Stirling"])
    
    with tab1:
        st.subheader("🥇 1. Siklus Carnot (Mesin Ideal Reversibel)")
        st.write("Siklus Carnot adalah siklus teoretis ideal yang terdiri dari dua proses isotermal dan dua proses adiabatik (isentropik). Siklus ini menetapkan batas atas maksimum efisiensi yang dapat dicapai oleh mesin kalor manapun di alam semesta.")
        st.markdown("**Karakteristik & Tahapan Proses:**")
        st.markdown("- **Proses 1-2:** Ekspansi Isotermal (Menyerap kalor dari reservoir tinggi).")
        st.markdown("- **Proses 2-3:** Ekspansi Adiabatik (Suhu turun dari tinggi ke rendah tanpa pertukaran kalor).")
        st.markdown("- **Proses 3-4:** Kompresi Isotermal (Melepaskan kalor ke reservoir rendah).")
        st.markdown("- **Proses 4-1:** Kompresi Adiabatik (Suhu naik kembali dari rendah ke tinggi).")
        st.markdown("### 📐 Rumus Efisiensi Teoretis:")
        st.latex(r"\eta_{\text{Carnot}} = 1 - \frac{T_C}{T_H}")
        
        st.markdown("""
        **Keterangan Rinci Variabel Rumus:**
        * $\\eta_{\\text{Carnot}}$ = Efisiensi termal maksimum Siklus Carnot (nilai antara 0 sampai 1, atau persentase jika dikalikan 100%)
        * $T_C$ = Suhu mutlak reservoir dingin / suhu pembuangan (dalam satuan Kelvin, K)
        * $T_H$ = Suhu mutlak reservoir panas / suhu sumber energi (dalam satuan Kelvin, K)
        """)
        
    with tab2:
        st.subheader("🚗 2. Siklus Otto (Mesin Pembakaran Dalam / Bensin)")
        st.write("Siklus Otto adalah siklus termodinamika yang merepresentasikan cara kerja mesin pembakaran dalam modern menggunakan bahan bakar bensin, di mana proses pembakaran atau pemasukan kalor terjadi secara sangat cepat pada volume konstan.")
        st.markdown("**Karakteristik & Tahapan Proses:**")
        st.markdown("- **Proses 1-2:** Kompresi Isentropik (Langkah kompresi fluida kerja di dalam silinder).")
        st.markdown("- **Proses 2-3:** Pemasukan Kalor pada Volume Konstan (Pembakaran oleh percikan api busi).")
        st.markdown("- **Proses 3-4:** Ekspansi Isentropik (Langkah usaha/daya yang menggerakkan piston).")
        st.markdown("- **Proses 4-1:** Pembuangan Kalor pada Volume Konstan (Pembukaan katup buang).")
        st.markdown("### 📐 Rumus Efisiensi Siklus Otto:")
        st.latex(r"\eta_{\text{Otto}} = 1 - \frac{1}{r^{\gamma - 1}}")
        
        st.markdown(r"""
        **Keterangan Rinci Variabel Rumus:**
        * $\eta_{\text{Otto}}$ = Efisiensi termal ideal dari Siklus Otto
        * $r$ = Rasio kompresi volume silinder, didefinisikan sebagai $V_1 / V_2$ (perbandingan volume awal terhadap volume minimum/titik mati atas)
        * $\gamma$ (gamma) = Indeks adiabatik atau konstanta Laplace (perbandingan kapasitas panas $C_p / C_v$, untuk udara bernilai sekitar $1.4$)
        """)
        
    with tab3:
        st.subheader("🚚 3. Siklus Diesel (Mesin Pembakaran Dalam / Solar)")
        st.write("Siklus Diesel adalah variasi siklus pembakaran dalam untuk mesin berat berbahan bakar solar. Penyaluran bahan bakar dilakukan secara perlahan pada tekanan konstan, memanfaatkan suhu tinggi akibat kompresi udara murni untuk penyulutan otomatis (*auto-ignition*).")
        st.markdown("**Karakteristik & Tahapan Proses:**")
        st.markdown("- **Proses 1-2:** Kompresi Isentropik (Udara murni ditekan hingga suhu sangat tinggi).")
        st.markdown("- **Proses 2-3:** Pemasukan Kalor pada Tekanan Konstan (Penyemprotan solar oleh injektor).")
        st.markdown("- **Proses 3-4:** Ekspansi Isentropik (Langkah daya dorong piston).")
        st.markdown("- **Proses 4-1:** Pembuangan Kalor pada Volume Konstan (Pembuangan sisa gas hasil pembakaran).")
        st.markdown("### 📐 Rumus Efisiensi Siklus Diesel:")
        st.latex(r"\eta_{\text{Diesel}} = 1 - \frac{1}{r^{\gamma-1}} \left[\frac{r_c^\gamma - 1}{\gamma (r_c - 1)}\right]")
        
        st.markdown(r"""
        **Keterangan Rinci Variabel Rumus:**
        * $\eta_{\text{Diesel}}$ = Efisiensi termal ideal dari Siklus Diesel
        * $r$ = Rasio kompresi total silinder ($V_1 / V_2$)
        * $r_c$ = Rasio pemotongan / *cut-off ratio* ($V_3 / V_2$, yaitu perbandingan volume saat selesai pemasukan kalor terhadap volume minimum)
        * $\gamma$ (gamma) = Indeks adiabatik atau konstanta Laplace ($\approx 1.4$ untuk udara)
        """)
        
    with tab4:
        st.subheader("🔄 4. Siklus Stirling (Mesin Pembakaran Eksternal)")
        st.write("Siklus Stirling adalah mesin pembakaran eksternal yang menggunakan matriks penukar panas internal atau *regenerator* untuk menyimpan dan mendaur ulang energi termal. Siklus ini dikenal memiliki efisiensi tinggi serta operasional yang sangat hening.")
        st.markdown("**Karakteristik & Tahapan Proses:**")
        st.markdown("- **Proses 1-2:** Ekspansi Isotermal (Gas berekspansi pada suhu tinggi konstan).")
        st.markdown("- **Proses 2-3:** Regenerasi Isokhorik (Pendinginan gas melalui penyerapan panas oleh regenerator).")
        st.markdown("- **Proses 3-4:** Kompresi Isotermal (Gas dikompresi pada suhu rendah konstan).")
        st.markdown("- **Proses 4-1:** Regenerasi Isokhorik (Pemanasan kembali gas oleh regenerator).")
        st.markdown("### 📐 Rumus Efisiensi Siklus Stirling Ideal:")
        st.latex(r"\eta_{\text{Stirling}} = 1 - \frac{T_C}{T_H}")
        
        st.markdown("""
        **Keterangan Rinci Variabel Rumus:**
        * $\\eta_{\\text{Stirling}}$ = Efisiensi termal ideal dari Siklus Stirling
        * $T_C$ = Suhu mutlak reservoir dingin / sisi pendingin eksternal (dalam satuan Kelvin, K)
        * $T_H$ = Suhu mutlak reservoir panas / sisi pemanas eksternal (dalam satuan Kelvin, K)
        * *Catatan Penting:* Dengan asumsi efisiensi regenerator internal mencapai 100%, batasan teoretis efisiensi siklus ini setara dengan Siklus Carnot.
        """)


elif menu == "4. Kalkulator & Diagram P-V/T-S":
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import streamlit as st

    st.markdown("## 📊 Kalkulator Kinerja & Diagram Siklus Termodinamika")
    st.write(
        "Visualisasi diagram P–V dan T–S berdasarkan persamaan "
        "proses termodinamika gas ideal."
    )

    # =========================================================
    # 1. PARAMETER INPUT
    # =========================================================
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("### 📥 Parameter Termodinamika")

            Th = st.number_input(
                "Suhu reservoir panas, T_H (K)",
                min_value=100.0,
                max_value=3000.0,
                value=600.0,
                step=10.0,
                key="th_calc"
            )

            Tc = st.number_input(
                "Suhu reservoir dingin, T_C (K)",
                min_value=50.0,
                max_value=2000.0,
                value=300.0,
                step=10.0,
                key="tc_calc"
            )

            gamma = st.number_input(
                "Indeks adiabatik, γ",
                min_value=1.1,
                max_value=1.67,
                value=1.4,
                step=0.05,
                key="gamma_calc"
            )

            rasio_volume = st.slider(
                "Rasio volume Carnot dan Stirling",
                min_value=1.2,
                max_value=4.0,
                value=2.0,
                step=0.1,
                key="rv_calc"
            )

    with col2:
        with st.container(border=True):
            st.markdown("### 📘 Asumsi Model")

            st.write("• Gas ideal dengan jumlah mol tetap.")
            st.write("• Kalor jenis konstan.")
            st.write("• Proses isentropik bersifat reversibel.")
            st.write("• R = 8,314462618 J/(mol·K).")
            st.write("• Volume adalah volume molar (m³/mol).")
            st.write("• Tekanan dihitung menggunakan PV = RT.")
            st.write("• Siklus Stirling menggunakan regenerasi ideal.")

    if Th <= Tc:
        st.error("T_H harus lebih besar daripada T_C.")
        st.stop()

    # =========================================================
    # 2. KONSTANTA DAN FUNGSI KEADAAN
    # =========================================================
    R = 8.314462618
    cv = R / (gamma - 1.0)
    cp = gamma * cv

    Vref = 1.0e-3
    Tref = Tc
    npoints = 300

    def state(T, V):
        """Menghitung keadaan gas ideal."""

        P = R * T / V

        S = (
            cv * np.log(T / Tref)
            + R * np.log(V / Vref)
        )

        return {
            "T": float(T),
            "V": float(V),
            "P": float(P),
            "S": float(S)
        }

    def process(a, b, kind, count=npoints):
        """
        Membentuk kurva berdasarkan persamaan proses.
        Titik awal dan akhir harus memenuhi persamaan proses.
        """

        Ta, Va = a["T"], a["V"]
        Tb, Vb = b["T"], b["V"]

        if kind == "Isentropik":
            # T V^(gamma-1) = konstan
            V = np.geomspace(Va, Vb, count)
            T = Ta * (Va / V) ** (gamma - 1.0)

        elif kind == "Isotermal":
            # T = konstan
            V = np.linspace(Va, Vb, count)
            T = np.full(count, Ta)

        elif kind == "Isokhorik":
            # V = konstan
            T = np.linspace(Ta, Tb, count)
            V = np.full(count, Va)

        elif kind == "Isobarik":
            # P = konstan, sehingga V/T = konstan
            T = np.linspace(Ta, Tb, count)
            V = Va * T / Ta

        else:
            raise ValueError(
                f"Jenis proses tidak dikenal: {kind}"
            )

        P = R * T / V

        S = (
            cv * np.log(T / Tref)
            + R * np.log(V / Vref)
        )

        return {
            "T": T,
            "V": V,
            "P": P,
            "S": S
        }

    # =========================================================
    # 3. PILIHAN SIKLUS
    # =========================================================
    pilihan = st.selectbox(
        "Pilih siklus termodinamika:",
        [
            "Siklus Carnot (Ideal)",
            "Siklus Otto (Mesin Bensin)",
            "Siklus Diesel (Mesin Berat)",
            "Siklus Stirling"
        ],
        key="pilihan_siklus_termodinamika"
    )

    rasio_suhu = Th / Tc
    Vdasar = Vref

    titik = []
    proses = []
    layak = True
    pesan = ""

    # =========================================================
    # 4. SIKLUS CARNOT
    # =========================================================
    if pilihan == "Siklus Carnot (Ideal)":

        # 1 -> 2: ekspansi isotermal pada Th
        # 2 -> 3: ekspansi isentropik
        # 3 -> 4: kompresi isotermal pada Tc
        # 4 -> 1: kompresi isentropik

        V1 = Vdasar
        V2 = V1 * rasio_volume

        faktor = rasio_suhu ** (1.0 / (gamma - 1.0))

        V3 = V2 * faktor
        V4 = V1 * faktor

        titik = [
            state(Th, V1),
            state(Th, V2),
            state(Tc, V3),
            state(Tc, V4)
        ]

        proses = [
            ("1 → 2: Ekspansi isotermal", "Isotermal", 0, 1),
            ("2 → 3: Ekspansi isentropik", "Isentropik", 1, 2),
            ("3 → 4: Kompresi isotermal", "Isotermal", 2, 3),
            ("4 → 1: Kompresi isentropik", "Isentropik", 3, 0)
        ]

    # =========================================================
    # 5. SIKLUS OTTO
    # =========================================================
    elif pilihan == "Siklus Otto (Mesin Bensin)":

        # 1 -> 2: kompresi isentropik
        # 2 -> 3: pemasukan kalor isokhorik
        # 3 -> 4: ekspansi isentropik
        # 4 -> 1: pembuangan kalor isokhorik

        # Model contoh: T2 = T4 = sqrt(Th * Tc).
        # Rasio kompresi ditentukan dari kondisi tersebut.

        r = rasio_suhu ** (1.0 / (2.0 * (gamma - 1.0)))

        V2 = Vdasar
        V1 = r * V2

        T1 = Tc
        T2 = T1 * r ** (gamma - 1.0)
        T3 = Th
        T4 = T3 / r ** (gamma - 1.0)

        if not (T1 < T2 < T3 and T1 < T4 < T3):
            layak = False
            pesan = "Parameter tidak memenuhi syarat siklus Otto."

        else:
            titik = [
                state(T1, V1),
                state(T2, V2),
                state(T3, V2),
                state(T4, V1)
            ]

            proses = [
                ("1 → 2: Kompresi isentropik", "Isentropik", 0, 1),
                ("2 → 3: Pemasukan kalor (V konstan)", "Isokhorik", 1, 2),
                ("3 → 4: Ekspansi isentropik", "Isentropik", 2, 3),
                ("4 → 1: Pembuangan kalor (V konstan)", "Isokhorik", 3, 0)
            ]

    # =========================================================
    # 6. SIKLUS DIESEL
    # =========================================================
    elif pilihan == "Siklus Diesel (Mesin Berat)":

        # 1 -> 2: kompresi isentropik
        # 2 -> 3: pemasukan kalor isobarik
        # 3 -> 4: ekspansi isentropik
        # 4 -> 1: pembuangan kalor isokhorik

        # Rasio kompresi dipilih agar siklus layak
        # untuk rentang suhu yang dimasukkan.

        r_bawah = rasio_suhu ** (1.0 / gamma)
        r_atas = rasio_suhu ** (1.0 / (gamma - 1.0))
        r = np.sqrt(r_bawah * r_atas)

        V2 = Vdasar
        V1 = r * V2

        T1 = Tc
        T2 = T1 * r ** (gamma - 1.0)
        T3 = Th

        # 2 -> 3: tekanan konstan
        V3 = V2 * T3 / T2

        # 3 -> 4: ekspansi isentropik sampai V4 = V1
        V4 = V1
        T4 = T3 * (V3 / V4) ** (gamma - 1.0)

        if not (
            T1 < T2 < T3
            and V2 < V3 < V1
            and T4 > T1
        ):
            layak = False
            pesan = "Parameter tidak memenuhi syarat siklus Diesel."

        else:
            titik = [
                state(T1, V1),
                state(T2, V2),
                state(T3, V3),
                state(T4, V4)
            ]

            proses = [
                ("1 → 2: Kompresi isentropik", "Isentropik", 0, 1),
                ("2 → 3: Pemasukan kalor (P konstan)", "Isobarik", 1, 2),
                ("3 → 4: Ekspansi isentropik", "Isentropik", 2, 3),
                ("4 → 1: Pembuangan kalor (V konstan)", "Isokhorik", 3, 0)
            ]

    # =========================================================
    # 7. SIKLUS STIRLING
    # =========================================================
    else:

        # 1 -> 2: ekspansi isotermal pada Th
        # 2 -> 3: pendinginan isokhorik
        # 3 -> 4: kompresi isotermal pada Tc
        # 4 -> 1: pemanasan isokhorik

        V1 = Vdasar
        V2 = rasio_volume * V1

        titik = [
            state(Th, V1),
            state(Th, V2),
            state(Tc, V2),
            state(Tc, V1)
        ]

        proses = [
            ("1 → 2: Ekspansi isotermal", "Isotermal", 0, 1),
            ("2 → 3: Pendinginan (V konstan)", "Isokhorik", 1, 2),
            ("3 → 4: Kompresi isotermal", "Isotermal", 2, 3),
            ("4 → 1: Pemanasan (V konstan)", "Isokhorik", 3, 0)
        ]

    if not layak:
        st.error(pesan)
        st.stop()

    # =========================================================
    # 8. PEMERIKSAAN TITIK KEADAAN DAN KONTINUITAS
    # =========================================================
    st.markdown("### 🔎 Verifikasi Titik Keadaan")

    tabel = []

    for i, p in enumerate(titik):
        tabel.append({
            "Titik": i + 1,
            "T (K)": p["T"],
            "V (m³/mol)": p["V"],
            "P (Pa)": p["P"],
            "PV/(RT)": p["P"] * p["V"] / (R * p["T"]),
            "S (J/(mol·K))": p["S"]
        })

    st.dataframe(
        pd.DataFrame(tabel).round(6),
        use_container_width=True,
        hide_index=True
    )

    sambungan_ok = all(
        proses[i][3] == proses[(i + 1) % len(proses)][2]
        for i in range(len(proses))
    )

    pv_ok = all(
        np.isclose(
            p["P"] * p["V"],
            R * p["T"],
            rtol=1e-10
        )
        for p in titik
    )

    # =========================================================
    # 9. PEMBENTUKAN KURVA DAN GRAFIK
    # =========================================================
    kurva_proses = []

    for nama, jenis, awal, akhir in proses:
        a = titik[awal]
        b = titik[akhir]
        kurva_proses.append(process(a, b, jenis))

    warna = [
        "tab:blue",
        "tab:orange",
        "tab:green",
        "tab:red"
    ]

    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(16, 7)
    )

    for i, (nama, jenis, awal, akhir) in enumerate(proses):

        kurva = kurva_proses[i]

        V = kurva["V"]
        P = kurva["P"]
        T = kurva["T"]
        S = kurva["S"]

        # -------------------------
        # DIAGRAM P-V
        # -------------------------
        ax1.plot(
            V, P,
            color=warna[i],
            linewidth=2.5,
            label=nama
        )

        # Panah mengikuti arah lintasan.
        idx = len(V) // 2

        ax1.annotate(
            "",
            xy=(V[idx + 3], P[idx + 3]),
            xytext=(V[idx - 3], P[idx - 3]),
            arrowprops=dict(
                arrowstyle="->",
                color=warna[i],
                lw=1.8
            )
        )

        # -------------------------
        # DIAGRAM T-S
        # -------------------------
        ax2.plot(
            S, T,
            color=warna[i],
            linewidth=2.5,
            label=nama
        )

        ax2.annotate(
            "",
            xy=(S[idx + 3], T[idx + 3]),
            xytext=(S[idx - 3], T[idx - 3]),
            arrowprops=dict(
                arrowstyle="->",
                color=warna[i],
                lw=1.8
            )
        )

    # -------------------------
    # LABEL TITIK KEADAAN
    # -------------------------
    for i, p in enumerate(titik):

        nomor = str(i + 1)

        ax1.scatter(
            p["V"], p["P"],
            color="black",
            s=40,
            zorder=5
        )

        ax1.annotate(
            nomor,
            (p["V"], p["P"]),
            xytext=(5, 6),
            textcoords="offset points",
            fontsize=10
        )

        ax2.scatter(
            p["S"], p["T"],
            color="black",
            s=40,
            zorder=5
        )

        ax2.annotate(
            nomor,
            (p["S"], p["T"]),
            xytext=(5, 6),
            textcoords="offset points",
            fontsize=10
        )

    # -------------------------
    # FORMAT DIAGRAM P-V
    # -------------------------
    ax1.set_title(
        f"Diagram P–V\n{pilihan}",
        fontsize=12
    )

    ax1.set_xlabel("Volume molar (m³/mol)")
    ax1.set_ylabel("Tekanan (Pa)")
    ax1.grid(True, linestyle=":", alpha=0.6)
    ax1.legend(fontsize=8, loc="best")
    ax1.margins(x=0.08, y=0.12)

    # -------------------------
    # FORMAT DIAGRAM T-S
    # -------------------------
    ax2.set_title(
        f"Diagram T–S\n{pilihan}",
        fontsize=12
    )

    ax2.set_xlabel("Entropi molar relatif (J/(mol·K))")
    ax2.set_ylabel("Suhu (K)")
    ax2.grid(True, linestyle=":", alpha=0.6)
    ax2.legend(fontsize=8, loc="best")
    ax2.margins(x=0.12, y=0.12)

    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    # =========================================================
    # 10. UJI PERSAMAAN SETIAP PROSES
    # =========================================================
    st.markdown("### 🧪 Uji Persamaan Proses")

    hasil_uji = []

    for i, (nama, jenis, awal, akhir) in enumerate(proses):

        a = titik[awal]
        b = titik[akhir]
        kurva = kurva_proses[i]

        if jenis == "Isentropik":

            nilai = (
                kurva["T"] * kurva["V"] ** (gamma - 1.0)
            )

            galat = np.max(
                np.abs(nilai / nilai[0] - 1.0)
            )

            persamaan = "T V^(γ−1) = konstan"

        elif jenis == "Isotermal":

            nilai = kurva["P"] * kurva["V"]

            galat = np.max(
                np.abs(nilai / nilai[0] - 1.0)
            )

            persamaan = "P V = konstan"

        elif jenis == "Isokhorik":

            galat = abs(b["V"] / a["V"] - 1.0)

            persamaan = "V = konstan"

        else:

            galat = abs(b["P"] / a["P"] - 1.0)

            persamaan = "P = konstan"

        hasil_uji.append({
            "Proses": nama,
            "Persamaan": persamaan,
            "Galat relatif maksimum": galat,
            "Status": "LULUS" if galat < 1e-8 else "PERIKSA"
        })

    df_uji = pd.DataFrame(hasil_uji)

    st.dataframe(
        df_uji.round(10),
        use_container_width=True,
        hide_index=True
    )

    proses_ok = all(
        item["Galat relatif maksimum"] < 1e-8
        for item in hasil_uji
    )

    if sambungan_ok and pv_ok and proses_ok:
        st.success(
            "LULUS: siklus tertutup, persamaan gas ideal terpenuhi, "
            "dan semua kurva sesuai dengan persamaan proses."
        )
    else:
        st.error(
            "PERIKSA: terdapat persamaan atau sambungan proses "
            "yang belum memenuhi toleransi pemeriksaan."
        )

    # =========================================================
    # 11. ANALISIS ENERGI DAN EFISIENSI TERMAL
    # =========================================================
    st.markdown("### ⚙️ Analisis Energi")

    def kalor_proses(a, b, jenis):

        if jenis == "Isentropik":
            return 0.0

        elif jenis == "Isokhorik":
            return cv * (b["T"] - a["T"])

        elif jenis == "Isobarik":
            return cp * (b["T"] - a["T"])

        elif jenis == "Isotermal":
            return R * a["T"] * np.log(b["V"] / a["V"])

        raise ValueError("Jenis proses tidak dikenal.")

    tabel_kalor = []

    Qin = 0.0
    Qout = 0.0

    for nama, jenis, awal, akhir in proses:

        a = titik[awal]
        b = titik[akhir]

        q_total = kalor_proses(a, b, jenis)
        q_regenerasi = 0.0

        # Pada Stirling ideal, kalor proses isokhorik
        # disimpan atau dilepas ke regenerator internal.
        # Kalor tersebut bukan kalor eksternal siklus.
        if pilihan == "Siklus Stirling" and jenis == "Isokhorik":

            q_eksternal = 0.0
            q_regenerasi = q_total

        else:
            q_eksternal = q_total

        if q_eksternal > 0:
            Qin += q_eksternal

        elif q_eksternal < 0:
            Qout += -q_eksternal

        tabel_kalor.append({
            "Proses": nama,
            "Kalor proses (J/mol)": q_total,
            "Kalor eksternal (J/mol)": q_eksternal,
            "Kalor regenerasi (J/mol)": q_regenerasi
        })

    if Qin > 0:

        efisiensi = (1.0 - Qout / Qin) * 100.0

        st.metric(
            "Efisiensi termal model",
            f"{efisiensi:.2f}%"
        )

        st.write(f"Kalor eksternal masuk: {Qin:.5f} J/mol")
        st.write(f"Kalor eksternal keluar: {Qout:.5f} J/mol")

    else:
        st.warning(
            "Kalor masuk tidak positif. Efisiensi tidak dapat dihitung."
        )

    st.dataframe(
        pd.DataFrame(tabel_kalor).round(5),
        use_container_width=True,
        hide_index=True
    )

    if pilihan == "Siklus Stirling":
        st.caption(
            "Efisiensi Stirling dihitung dengan asumsi regenerasi ideal. "
            "Kalor pada proses isokhorik merupakan pertukaran kalor "
            "internal dengan regenerator, bukan kalor eksternal."
        )

    if pilihan == "Siklus Otto (Mesin Bensin)":
        st.caption(
            "Siklus Otto menggunakan model ideal dengan pemasukan "
            "dan pembuangan kalor pada volume konstan."
        )

    if pilihan == "Siklus Diesel (Mesin Berat)":
        st.caption(
            "Siklus Diesel menggunakan model ideal dengan pemasukan "
            "kalor pada tekanan konstan."
        )

    # =========================================================
    # 12. DASAR TEORI
    # =========================================================
    with st.expander("📘 Persamaan Dasar yang Digunakan"):

        st.markdown("**Persamaan gas ideal**")
        st.latex(r"PV=RT")

        st.markdown("**Proses isentropik**")
        st.latex(r"TV^{\gamma-1}=\text{konstan}")

        st.markdown("**Proses isotermal**")
        st.latex(r"PV=\text{konstan}")

        st.markdown("**Proses isokhorik**")
        st.latex(r"V=\text{konstan}")

        st.markdown("**Proses isobarik**")
        st.latex(r"P=\text{konstan}")

        st.markdown("**Perubahan entropi molar gas ideal**")
        st.latex(
            r"\Delta S=c_v\ln\left(\frac{T_2}{T_1}\right)"
            r"+R\ln\left(\frac{V_2}{V_1}\right)"
        )

        st.markdown("**Efisiensi termal**")
        st.latex(
            r"\eta=\left(1-\frac{Q_{\text{keluar}}}"
            r"{Q_{\text{masuk}}}\right)\times100\%"
        )

elif menu == "5. Tantangan & Skor Interaktif":
    st.markdown("## 🎮 Tantangan & Bank Kuis Termodinamika per Siklus (5 Soal)")
    st.write("Uji pemahaman mendalam Anda melalui tantangan urutan proses dan bank kuis komprehensif (masing-masing 5 soal berkualitas tinggi) untuk mengumpulkan skor tertinggi!")
    
    if 'score' not in st.session_state:
        st.session_state.score = 250
    if 'lives' not in st.session_state:
        st.session_state.lives = 3

    with st.container(border=True):
        st.markdown(f"### ❤️ Nyawa: {'❤️' * st.session_state.lives} &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 🌟 Total Skor: {st.session_state.score}")
        st.write("---")
        
        pilihan_tantangan = st.selectbox(
            "Pilih Kategori Soal / Tantangan:",
            [
                "Pilih tantangan...",
                "Tantangan 1: Susun Urutan Proses Siklus Carnot",
                "Kuis 1: Siklus Carnot (5 Soal)",
                "Kuis 2: Siklus Otto / Mesin Bensin (5 Soal)",
                "Kuis 3: Siklus Diesel / Mesin Solar (5 Soal)",
                "Kuis 4: Siklus Stirling (5 Soal)"
            ]
        )
        
        st.write("---")
        
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

        bank_kuis_all = {
            "Kuis 1: Siklus Carnot (5 Soal)": [
                {"q": "1. Siklus Carnot terdiri dari kombinasi 4 proses reversibel, yaitu...", "options": ["2 Isotermal dan 2 Isentropik (Adiatik Reversibel)", "2 Isobarik dan 2 Isokhorik", "2 Isokhorik dan 2 Isotermal", "2 Isobarik dan 2 Isentropik"], "ans": "2 Isotermal dan 2 Isentropik (Adiatik Reversibel)"},
                {"q": "2. Persamaan efisiensi termal maksimum untuk mesin Carnot dinyatakan oleh rumus...", "options": ["η = 1 - (T_C / T_H)", "η = 1 - (P_C / P_H)", "η = (T_H + T_C) / T_H", "η = T_C / T_H"], "ans": "η = 1 - (T_C / T_H)"},
                {"q": "3. Mengapa mesin Carnot tidak dapat dibuat secara nyata dalam kehidupan sehari-hari?", "options": ["Prosesnya harus berjalan sangat lambat agar tetap reversibel", "Membutuhkan bahan bakar yang terlalu mahal", "Tidak membutuhkan fluida kerja", "Menggunakan tekanan yang mendekati nol"], "ans": "Prosesnya harus berjalan sangat lambat agar tetap reversibel"},
                {"q": "4. Jika suhu reservoir panas T_H diperbesar sedangkan T_C tetap, bagaimana efisiensi mesin Carnot?", "options": ["Efisiensi akan meningkat", "Efisiensi akan menurun", "Efisiensi tetap sama", "Efisiensi menjadi 0%"], "ans": "Efisiensi akan meningkat"},
                {"q": "5. Pada Hukum II Termodinamika, tidak mungkin ada mesin kalor yang memiliki efisiensi sebesar...", "options": ["100%", "50%", "75%", "33%"], "ans": "100%"}
            ],
            "Kuis 2: Siklus Otto / Mesin Bensin (5 Soal)": [
                {"q": "1. Pada Siklus Otto (mesin bensin), proses pemasukan kalor dari pembakaran terjadi secara...", "options": ["Volume Konstan (Isokhorik)", "Tekanan Konstan (Isobarik)", "Suhu Konstan (Isotermal)", "Entropi Konstan (Isentropik)"], "ans": "Volume Konstan (Isokhorik)"},
                {"q": "2. Alat pemantik yang digunakan untuk menyulut campuran bahan bakar dan udara pada Siklus Otto adalah...", "options": ["Busi (Spark Plug)", "Injektor Bahan Bakar", "Turbin Kalor", "Kondensor"], "ans": "Busi (Spark Plug)"},
                {"q": "3. Parameter r pada rumus efisiensi Siklus Otto merepresentasikan...", "options": ["Rasio Kompresi Volume (V_max / V_min)", "Rasio Suhu Maksimum", "Rasio Tekanan Udara", "Rasio Kecepatan Piston"], "ans": "Rasio Kompresi Volume (V_max / V_min)"},
                {"q": "4. Apa yang terjadi jika rasio kompresi pada mesin bensin dibuat terlalu tinggi?", "options": ["Terjadi ngelitik / pembakaran dini (Knocking)", "Mesin menjadi lebih dingin", "Bahan bakar menjadi tidak bisa terbakar", "Daya mesin langsung turun ke nol"], "ans": "Terjadi ngelitik / pembakaran dini (Knocking)"},
                {"q": "5. Siklus Otto ideal terdiri dari kombinasi 4 proses, yaitu...", "options": ["2 Isentropik dan 2 Isokhorik", "2 Isentropik dan 2 Isobarik", "2 Isotermal dan 2 Isokhorik", "2 Isobarik dan 2 Isotermal"], "ans": "2 Isentropik dan 2 Isokhorik"}
            ],
            "Kuis 3: Siklus Diesel / Mesin Solar (5 Soal)": [
                {"q": "1. Perbedaan utama Siklus Diesel dibanding Siklus Otto berada pada proses pemasukan kalor yang terjadi secara...", "options": ["Tekanan Konstan (Isobarik)", "Volume Konstan (Isokhorik)", "Suhu Konstan (Isotermal)", "Tanpa Kalor (Adiabatik)"], "ans": "Tekanan Konstan (Isobarik)"},
                {"q": "2. Mengapa mesin Diesel tidak memerlukan busi untuk proses pembakarannya?", "options": ["Suhu akibat kompresi udara yang sangat tinggi mampu membakar solar secara mandiri (Auto-ignition)", "Karena mesin Diesel menggunakan bahan bakar bensin", "Karena tidak ada fluida kerja di dalam silinder", "Karena pemanasan dilakukan oleh regenerator luar"], "ans": "Suhu akibat kompresi udara yang sangat tinggi mampu membakar solar secara mandiri (Auto-ignition)"},
                {"q": "3. Komponen yang bertugas menyemprotkan kabut bahan bakar solar ke dalam silinder mesin Diesel adalah...", "options": ["Injektor (Injector)", "Busi (Spark Plug)", "Karburator", "Katup Isap"], "ans": "Injektor (Injector)"},
                {"q": "4. Parameter rc pada Siklus Diesel dikenal dengan sebutan...", "options": ["Rasio Pemotongan (Cut-off Ratio)", "Rasio Kompresi Busi", "Rasio Suhu Dingin", "Rasio Kerja Otomatis"], "ans": "Rasio Pemotongan (Cut-off Ratio)"},
                {"q": "5. Mana yang memiliki rasio kompresi lebih tinggi pada umumnya dalam praktik teknik?", "options": ["Mesin Diesel", "Mesin Bensin (Otto)", "Keduanya selalu sama", "Mesin Carnot"], "ans": "Mesin Diesel"}
            ],
            "Kuis 4: Siklus Stirling (5 Soal)": [
                {"q": "1. Siklus Stirling tergolong ke dalam jenis mesin pembakaran...", "options": ["Pembakaran Eksternal (External Combustion Engine)", "Pembakaran Dalam (Internal Combustion Engine)", "Mesin Tanpa Pembakaran", "Mesin Listrik Murni"], "ans": "Pembakaran Eksternal (External Combustion Engine)"},
                {"q": "2. Komponen kunci khas pada mesin Stirling yang berfungsi menyimpan dan mengembalikan energi termal adalah...", "options": ["Regenerator", "Injektor Solar", "Busi Listrik", "Karburator"], "ans": "Regenerator"},
                {"q": "3. Dua proses isotermal pada Siklus Stirling dihubungkan oleh dua proses...", "options": ["Isokhorik (Volume Konstan)", "Isobarik (Tekanan Konstan)", "Isentropik (Entropi Konstan)", "Adiabatik Bebas"], "ans": "Isokhorik (Volume Konstan)"},
                {"q": "4. Mengapa mesin Stirling dikenal sangat ramah lingkungan dan hening?", "options": ["Pembakaran berlangsung kontinu di luar silinder tanpa ledakan letupan katup buang", "Karena tidak menggunakan fluida kerja", "Karena bergerak tanpa adanya piston", "Karena bekerja tanpa memerlukan energi panas"], "ans": "Pembakaran berlangsung kontinu di luar silinder tanpa ledakan letupan katup buang"},
                {"q": "5. Jika regenerator pada Siklus Stirling bekerja 100% sempurna, efisiensi Siklus Stirling akan sama dengan...", "options": ["Efisiensi Siklus Carnot", "Efisiensi Siklus Otto", "Efisiensi Siklus Diesel", "0%"], "ans": "Efisiensi Siklus Carnot"}
            ]
        }

        if pilihan_tantangan in bank_kuis_all:
            st.markdown(f"#### 📝 {pilihan_tantangan}")
            soal_list = bank_kuis_all[pilihan_tantangan]
            user_answers = {}
            
            for idx, item in enumerate(soal_list):
                user_answers[idx] = st.radio(item["q"], ["Pilih jawaban..."] + item["options"], key=f"q_key_{pilihan_tantangan}_{idx}")
                st.write("")
                
            if st.button(f"Kirim Jawaban {pilihan_tantangan}"):
                benar = 0
                for idx, item in enumerate(soal_list):
                    if user_answers[idx] == item["ans"]:
                        benar += 1
                
                skor_tambah = benar * 20
                st.session_state.score += skor_tambah
                st.success(f"🎉 Anda menjawab benar {benar} dari 5 soal! Poin bertambah +{skor_tambah}.")
                if benar == 5:
                    st.balloons()

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
