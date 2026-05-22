import streamlit as st
import os

# Sahifa sozlamalari
st.set_page_config(page_title="Fizika: Issiqlik Miqdori Testi", page_icon="🔥", layout="centered")

st.title("🔥 Fizika fanidan ovozli test")
st.subheader("Mavzu: Issiqlik Miqdori")
st.markdown("---")

# 1. FOYDALANUVCHI MA'LUMOTLARINI SO'RASH QISMI
st.markdown("### 📋 O'quvchi ma'lumotlari")
st.write("Testni boshlashdan oldin quyidagi maydonlarni to'ldiring:")

col1, col2 = st.columns(2)
with col1:
    ism = st.text_input("Ismingiz:", placeholder="Masalan: Behruz")
    familiya = st.text_input("Familiyangiz:", placeholder="Masalan: Usmonov")
with col2:
    sinf = st.text_input("Sinfingiz:", placeholder="Masalan: 9-A")

st.markdown("---")

# Savollar, variantlar va to'g'ri javoblar bazasi
savollar_bazasi = [
    {
        "id": 1,
        "savol": "1-savol: Jism yutilgan yoki ajralgan ichki energiyaning muayyan qismi nima deyiladi?",
        "variantlar": ["Solishtirma issiqlik sig‘imi.", "Issiqlik miqdori.", "Temperatura.", "Ichki energiya."],
        "togri_javob": "Issiqlik miqdori.",
        "audio": "savol_1.m4a"
    },
    {
        "id": 2,
        "savol": "2-savol: Xalqaro birliklar sistemasida issiqlik miqdori qaysi birlikda o‘lchanadi?",
        "variantlar": ["Joul.", "Kaloriya.", "Kelvin.", "Vatt."],
        "togri_javob": "Joul.",
        "audio": "savol_2.m4a"
    },
    {
        "id": 3,
        "savol": "3-savol: Massa va temperaturaning o‘zgarishi o‘zgarmas bo‘lganda, issiqlik miqdori qanday kattalikka to‘g‘ri proporsional bo‘ladi?",
        "variantlar": ["Jismning hajmiga.", "Jismning zichligiga.", "Moddaning solishtirma issiqlik sig‘imiga.", "Tashqi bosimga."],
        "togri_javob": "Moddaning solishtirma issiqlik sig‘imiga.",
        "audio": "savol_3.m4a"
    },
    {
        "id": 4,
        "savol": "4-savol: Solishtirma issiqlik sig‘imining xalqaro birliklar sistemasidagi birligi qaysi?",
        "variantlar": ["Joul taqsim kilogramm.", "Joul ko'paytirilgan kilogramm ko'paytirilgan gradus Selsiy.", "Joul taqsim qavs ichida kilogramm ko'paytirilgan Kelvin.", "Kaloriya taqsim gradus Selsiy."],
        "togri_javob": "Joul taqsim qavs ichida kilogramm ko'paytirilgan Kelvin.",
        "audio": "savol_4.m4a"
    },
    {
        "id": 5,
        "savol": "5-savol: Nima uchun kunduzi dengiz bo‘yida shamol dengizdan quruqlikka qarab esadi?",
        "variantlar": ["Suvning solishtirma issiqlik sig‘imi qumnikidan katta bo‘lib, sekinroq isiydi.", "Qumning solishtirma issiqlik sig‘imi kattaligi uchun tez isiydi.", "Suv kunduzi tezroq isiydi va havo yuqoriga ko‘tariladi.", "Quruqlik va suvning issiqlik sig‘imlari mutloq teng."],
        "togri_javob": "Suvning solishtirma issiqlik sig‘imi qumnikidan katta bo‘lib, sekinroq isiydi.",
        "audio": "savol_5.m4a"
    },
    {
        "id": 6,
        "savol": "6-savol: Massalari teng bo‘lgan alyuminiy va mis parchalari bir xil issiqlik miqdori oldi. Ularning temperaturalari qanday o‘zgaradi?",
        "variantlar": ["Alyuminiy tezroq isiydi.", "Mis tezroq isiydi.", "Ikkalasi ham bir xil temperaturagacha isiydi.", "Alyuminiy soviydi, mis isiydi."],
        "togri_javob": "Mis tezroq isiydi.",
        "audio": "savol_6.m4a"
    },
    {
        "id": 7,
        "savol": "7-savol: Jism soviganda uning ajratgan issiqlik miqdori formulasida, delta te teng te ikki minus te bir ayirmasi qanday ishoraga ega bo‘ladi?",
        "variantlar": ["Musbat", "Manfiy", "Nolga teng.", "Ishorasi vaziyatga qarab o‘zgaradi."],
        "togri_javob": "Manfiy",
        "audio": "savol_7.m4a"
    },
    {
        "id": 8,
        "savol": "8-savol: Solishtirma issiqlik sig‘imi deb qanday miqdorga aytiladi?",
        "variantlar": ["Massasi bir kilogramm bo‘lgan moddani bir Kelvin ko‘tarish uchun ketadigan issiqlik miqdoriga.", "Jismning to‘liq erishi uchun sarflanadigan umumiy issiqlik miqdoriga.", "Moddaning bir soniyada tashqi muhitga beradigan issiqlik energiyasiga.", "Jismning ichki energiyasini o‘zgartirmasdan saqlaydigan xossasiga."],
        "togri_javob": "Massasi bir kilogramm bo‘lgan moddani bir Kelvin ko‘tarish uchun ketadigan issiqlik miqdoriga.",
        "audio": "savol_8.m4a"
    },
    {
        "id": 9,
        "savol": "9-savol: Izolatsiyalangan tizimda issiqlik almashinuvi jarayonida issiqlik balansi tenglamasi qaysi qonunga asoslanadi?",
        "variantlar": ["Nyutonning ikkinchi qonuniga.", "Energiyaning saqlanish qonuniga.", "Massa saqlanish qonuniga.", "Paskal qonuniga."],
        "togri_javob": "Energiyaning saqlanish qonuniga.",
        "audio": "savol_9.m4a"
    },
    {
        "id": 10,
        "savol": "10-savol: Nima uchun turli moddalarning solishtirma issiqlik sig‘imi har xil qiymatga ega bo‘ladi?",
        "variantlar": ["Ularning ichki tuzilishi va zarrachalarining joylashishi turlicha bo‘lgani uchun.", "Jismning faqat tashqi geometrik shakli har xil bo‘lgani uchun.", "Moddalarning faqat boshlang‘ich temperaturalari farq qilgani uchun", "Ularning faqat atmosfera bosimi ostida turganligi uchun."],
        "togri_javob": "Ularning ichki tuzilishi va zarrachalarining joylashishi turlicha bo‘lgani uchun.",
        "audio": "savol_10.m4a"
    }
]

# Agar ism, familiya va sinf to'liq kiritilgan bo'lsa, testni ko'rsatamiz
if ism.strip() and familiya.strip() and sinf.strip():
    
    st.success(f"Omad tilaymiz, {ism} {familiya}! Savollarni eshiting va javob qoldiring.")
    user_answers = {}

    # Savollarni chiqarish loopi
    for item in savollar_bazasi:
        st.markdown(f"### {item['savol']}")
        
        # Audio fayl yo'li
        audio_path = os.path.join("audio_files", item["audio"])
        
        if os.path.exists(audio_path):
            st.audio(audio_path, format="audio/m4a")
        else:
            st.warning(f"Audio fayl topilmadi: {item['audio']}")
            
        izoh = f"Savol-{item['id']} uchun javob"
        user_answers[item["id"]] = st.radio(izoh, item["variantlar"], index=None, key=f"q_{item['id']}", label_visibility="collapsed")
        st.markdown("---")

    # Tekshirish tugmasi
    if st.button("Testni yakunlash va Natijani ko'rish", type="primary"):
        belgilanmaganlar = any(user_answers[item["id"]] is None for item in savollar_bazasi)
        
        if belgilanmaganlar:
            st.error("Iltimos, barcha savollarga javob belgilang, keyin testni yakunlang!")
        else:
            togri_javoblar_soni = 0
            
            # Natijalar paneli
            st.markdown("## 📊 IMTIHON NATIJALARI")
            st.info(f"👤 **O'quvchi:** {familiya} {ism} | 🏫 **Sinf:** {sinf}")
            st.markdown("---")
            
            for item in savollar_bazasi:
                u_ans = user_answers[item["id"]]
                t_ans = item["togri_javob"]
                
                if u_ans == t_ans:
                    togri_javoblar_soni += 1
                    st.success(f"✅ **Savol {item['id']}: TO'G'RI.** \n\n Sizning javobingiz: {u_ans}")
                else:
                    st.error(f"❌ **Savol {item['id']}: NOTO'G'RI.** \n\n *Siz belgilagan javob:* {u_ans} \n\n *To'g'ri javob:* {t_ans}")
                st.markdown(" ")
            
            # Yakuniy natija hisobi
            foiz = (togri_javoblar_soni / len(savollar_bazasi)) * 100
            st.balloons()
            
            st.markdown("### 🏆 Yakuniy Ko'rsatkich:")
            st.metric(label="To'g'ri javoblar", value=f"{togri_javoblar_soni} / {len(savollar_bazasi)}", delta=f"{foiz}% natija")

else:
    # Agar ma'lumotlar to'liq kiritilmagan bo'lsa ogohlantirish chiqarib turadi
    st.warning("⚠️ Test savollarini ko'rish uchun yuqoridagi maydonlarga Ismingiz, Familiyangiz va Sinfingizni yozing!")