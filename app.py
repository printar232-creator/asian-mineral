import streamlit as st
import pandas as pd

# ตั้งค่าหน้าเว็บ (Page Configuration)
st.set_page_config(
    page_title="Asia Mineral Supply (AMS)",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ส่วนของแถบเมนูด้านซ้าย (Sidebar Navigation) ---
st.sidebar.title("📌 เมนูหลัก")
page = st.sidebar.radio(
    "ไปยังหน้า:",
    ["หน้าแรก & รู้จักเรา", "ผลิตภัณฑ์ Barytes", "ผลิตภัณฑ์ Talc", "ติดต่อเรา"]
)

# --- หน้าที่ 1: หน้าแรก & รู้จักเรา ---
if page == "หน้าแรก & รู้จักเรา":
    st.title("🏢 Asia Mineral Supply (AMS)")
    st.subheader("Reliable supply of Barium Sulphate (BaSO4) & Talc powder")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.header("📋 ข้อมูลบริษัท (Who is AMS)")
        st.write(
            "AMS เป็นผู้เชี่ยวชาญในการจัดหาผงแร่ธรรมชาติ **Barium Sulphate (BaSO4)** "
            "ที่มีขนาดตั้งแต่ 5 ไมครอน ไปจนถึงขนาดทั่วไป 325 mesh ซึ่งตอบโจทย์การใช้งานในอุตสาหกรรม "
            "สี (Paint), พลาสติก (Plastic), ยาง (Rubber) และการเจาะน้ำมัน (Oil Drilling)"
        )
        st.write(
            "เรามีบริษัทในเครือคือ **'Asian Mineral Resources (AMR)'** ซึ่งเป็นหน่วยผลิตที่มีประสบการณ์ "
            "การผลิตยาวนานกว่า 30 ปี ตั้งอยู่ที่อำเภอพระพุทธบาท จังหวัดสระบุรี (เมืองแห่งการบดแร่) "
            "ซึ่งอยู่ห่างจากกรุงเทพฯ ไปทางตะวันออกประมาณ 120 กิโลเมตร โดย AMS ทำหน้าที่เป็นกลไกหลักด้านการขายและการตลาดให้กับ AMR"
        )
    
    with col2:
        st.header("🌟 ปัจจัยสู่ความสำเร็จ (Key Success Factors)")
        st.markdown(
            """
            * **ความสามารถในการจัดหาแร่ (Supply Ability):** เรามีแหล่งแร่ BaSO4 ที่เชื่อถือได้ 3 แหล่งหลัก ได้แก่
                * **จีน:** คุณภาพสูงและยังมีปริมาณสำรองจำนวนมาก
                * **ปากีสถาน:** คุณภาพเป็นที่ยอมรับได้
                * **ลาว:** มีการคัดเลือกและล้างแร่ล่วงหน้า สามารถจัดส่งได้อย่างรวดเร็วที่ชายแดน
            * **คุณภาพที่เหนือกว่า (Quality):** * ควบคุมค่าความขาว (Whiteness) มากกว่า 95% 
                * ควบคุมการกระจายตัวของขนาดอนุภาค (Particle size distribution) อย่างเข้มงวด
            * **ความปลอดภัยสูง:** ผ่านการทดสอบจากห้องปฏิบัติการอิสระในออสเตรเลีย พบว่ามีแร่ซิลิกาที่สูดดมได้ (Respirable Crystalline Silica) ต่ำกว่า 0.001%
            * **เป็นธรรมชาติ 100%:** ไม่ผ่านกระบวนการปรับแต่งด้วยเคมีใดๆ ก่อนบดก้อนแร่
            """
        )

# --- หน้าที่ 2: ผลิตภัณฑ์ Barytes ---
elif page == "ผลิตภัณฑ์ Barytes":
    st.title("🧪 ผลิตภัณฑ์กลุ่ม Barytes (Barium Sulphate)")
    st.write("ตารางแสดงรายละเอียดข้อมูลจำเพาะและอุตสาหกรรมที่เหมาะสมของแต่ละเกรด")
    
    # ข้อมูลผลิตภัณฑ์ Barytes
    barytes_data = {
        "Product": ["Microbytes 2", "Microbytes 5", "Microbytes 7", "Microbytes 10", "Milbar 5", "Milbar 7", "Milbar 10", "Milbar A45", "Milbar D45"],
        "BaSO4 (%)": [">98.0%", "96.7%", "96.7%", "96.7%", "96.7%", "96.7%", "96.7%", "96.7%", "93.0%"],
        "Top Cut (d98)": ["14 µ (800 mesh)", "20 µ (625 mesh)", "25 µ (550 mesh)", "30 µ (450 mesh)", "20 µ (625 mesh)", "25 µ (550 mesh)", "30 µ (450 mesh)", "45 µ (325 mesh)", "45 µ (325 mesh)"],
        "Average / Median": ["2 µ (3,500 mesh)", "5 µ (2,500 mesh)", "7 µ (1,500 mesh)", "10 µ (1,250 mesh)", "5 µ (2,500 mesh)", "7 µ (1,500 mesh)", "10 µ (1,250 mesh)", "14 µ (900 mesh)", "14 µ (900 mesh)"],
        "Whiteness (%)": [">93%", "91%", "91%", "91%", "89% ±3", "89% ±3", "89% ±3", "90%", "60%"],
        "Specific Gravity": [">4.20", ">4.20", ">4.20", ">4.20", ">4.20", ">4.20", ">4.20", ">4.20", "3.90-4.00"],
        "Applications": [
            "สีพาวเดอร์โค้ตติ้ง & สีเกรดสูง", 
            "สีพาวเดอร์โค้ตติ้ง & สีเกรดสูง", 
            "สีพาวเดอร์โค้ตติ้ง & สีเกรดสูง", 
            "สีพาวเดอร์โค้ตติ้ง & สีเกรดสูง",
            "ใช้ 15% ในสีพาวเดอร์โค้ตติ้ง / สารเพิ่มเนื้อเพิ่มความทนทานต่อการขัดถูในสีทาอาคาร",
            "ใช้ 15% ในสีพาวเดอร์โค้ตติ้ง / สารเพิ่มเนื้อเพิ่มความทนทานต่อการขัดถูในสีทาอาคาร",
            "ใช้ 15% ในสีพาวเดอร์โค้ตติ้ง / สารเพิ่มเนื้อเพิ่มความทนทานต่อการขัดถูในสีทาอาคาร",
            "สารเพิ่มเนื้อมาตรฐาน 325mesh สำหรับสีอุตสาหกรรม (ช่วยเพิ่มน้ำหนักแต่ราคาประหยัด)",
            "ผ้าเบรค, สารเติมแต่งน้ำหนักใน PP compound, สีรองพื้น/สีอุดเสี้ยนไม้"
        ]
    }
    
    df_barytes = pd.DataFrame(barytes_data)
    st.dataframe(df_barytes, use_container_width=True)
    
    st.markdown("---")
    st.subheader("📋 เกรดอื่นๆ เพิ่มเติม")
    st.markdown(
        """
        * **Milbar B45:** Whiteness 80% | BaSO4 91-93% | SG 4.00-4.10 (คุณสมบัติคล้าย A45 แต่ความขาวลดลง)
        * **Milbar C45:** Whiteness 75% | BaSO4 91-93% | SG 4.00-4.10 (คุณสมบัติคล้าย A45 แต่ความขาวลดลง)
        * **T-Bar 200:** Top Cut 75 µ (200 mesh) | เกรดสำหรับงานเจาะน้ำมันตามมาตรฐาน API (API compliance oil drilling grade)
        """
    )
    
    st.info("ℹ️ **Methodology:** วิเคราะห์ขนาดอนุภาคด้วยเครื่อง SediGraph, micromeritics และควบคุมค่าความขาวด้วย KETT Reflectometer อย่างเข้มงวด ความชื้นเฉลี่ยต่ำเพียง 0.1% - 0.2%")

# --- หน้าที่ 3: ผลิตภัณฑ์ Talc ---
elif page == "ผลิตภัณฑ์ Talc":
    st.title("🍃 ผลิตภัณฑ์กลุ่ม Talc (ทัลคัม / แป้งหิน)")
    st.write("นอกจากแร่ Barytes แล้ว โรงงานของเรายังมีผลิตภัณฑ์แป้งทัลคัมคุณภาพสูงรองรับกลุ่มอุตสาหกรรมต่างๆ ดังนี้")
    
    talc_data = {
        "Product": ["Talcon BC20", "Talcon BC45"],
        "Top Size": ["20 µ (630 mesh)", "45 µ (325 mesh)"],
        "Median Size": ["6.0 - 7.0 µ", "12.0 - 15.0 µ"],
        "Whiteness": [91, 90],
        "Application": ["อุตสาหกรรมผลิตเส้นด้ายยาง (Rubber Thread)", "อุตสาหกรรมเครื่องสำอาง และ สี (Cosmetic & Paint)"]
    }
    
    df_talc = pd.DataFrame(talc_data)
    st.table(df_talc)
    
    st.success("✨ **Option เสริม:** ทั้งสองเกรดสามารถเข้าสู่กระบวนการฆ่าเชื้อ (Sterilization) เพิ่มเติมได้ตามความต้องการของลูกค้า")

# --- หน้าที่ 4: ติดต่อเรา ---
elif page == "ติดต่อเรา":
    st.title("📞 ติดต่อเรา (Contact Us)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🏢 สำนักงานและการตลาด")
        st.write("**Asia Mineral Supply (AMS)**")
        st.write("ทำหน้าที่ดูแลการตลาดและซัพพลายเชนระหว่างประเทศ")
        
        st.subheader("🏭 ที่ตั้งโรงงานผลิต")
        st.write("**Asian Mineral Resources (AMR)**")
        st.write("📍 ศูนย์กลางเมืองแห่งการบดแร่ อำเภอพระพุทธบาท จังหวัดสระบุรี ประเทศไทย")
        st.write("🚛 **ทำเลเชิงกลยุทธ์:** ห่างจากด่านชายแดน (สปป.ลาว) 500 กม. และห่างจากท่าเรือกรุงเทพฯ เพียง 120 กม. สะดวกต่อการขนส่งทั้งทางบกและทางเรือเพื่อการส่งออก")
        
    with col2:
        st.subheader("⚙️ ศักยภาพการผลิต (Production Capacity)")
        st.write("โรงงานเปิดทำงาน 16 ชั่วโมงต่อวัน (16hrs/day x 26 days x 12 months) โดยมีสายการผลิตทั้งหมด 5 ไลน์:")
        st.markdown(
            """
            * **Line 1:** 2,500 MT/ปี สำหรับ Super Fine Barytes/Talc (ละเอียดถึง 5 ไมครอน)
            * **Line 2 & 3:** เกรดละ 7,500 MT/ปี สำหรับ Fine Barytes/Talc (ขนาด 5, 7, 10 ไมครอน)
            * **Line 4 & 5:** เกรดละ 15,000 MT/ปี สำหรับ API Barytes (งานเจาะน้ำมัน)
            """
        )
        
    st.markdown("---")
    st.center = st.write("🙏 Thank you - Asia Mineral Supply")
