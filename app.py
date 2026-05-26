import streamlit as st

# กำหนดค่าหน้าเพจ Streamlit ให้แสดงผลแบบกว้าง (Wide Mode) และเปลี่ยนชื่อแท็บบนบราวเซอร์
st.set_page_config(
    page_title="Asia Mineral Supply (AMS) - High-Purity BaSO4 & Talc",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# สไตล์การซ่อนองค์ประกอบพื้นฐานบางส่วนของ Streamlit เพื่อให้เว็บไซต์ดูเนียนตาเป็นธรรมชาติ
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
    div[data-testid="stToolbar"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# โค้ด HTML, Tailwind CSS และ Vanilla JavaScript สำหรับแสดงผลเว็บไซต์องค์กรแบบเต็มรูปแบบ
html_code = """
<!DOCTYPE html>
<html lang="th" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Asia Mineral Supply (AMS)</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #F8FAFC;
        }
        .bg-navy { background-color: #0F172A; }
        .text-teal { color: #0D9488; }
        .bg-teal { background-color: #0D9488; }
        .border-teal { border-color: #0D9488; }
        .hover-bg-teal:hover { background-color: #0F766E; }
    </style>
</head>
<body class="text-slate-800 antialiased">

    <header id="main-header" class="fixed top-0 left-0 w-full z-50 transition-all duration-300 bg-slate-900/90 backdrop-blur-md shadow-lg border-b border-slate-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="bg-teal p-2.5 rounded-lg text-white font-bold text-xl tracking-wider shadow-inner shadow-teal-400">AMS</div>
                <div>
                    <span class="text-white font-extrabold text-lg block tracking-wide">Asia Mineral Supply</span>
                    <span class="text-slate-400 text-xs block -mt-1">Reliable Powder Solutions</span>
                </div>
            </div>
            <nav class="hidden lg:flex space-x-8 text-sm font-medium">
                <a href="#home" class="text-teal transition-colors">หน้าแรก</a>
                <a href="#about" class="text-slate-300 hover:text-teal transition-colors">เกี่ยวกับเรา</a>
                <a href="#key-success" class="text-slate-300 hover:text-teal transition-colors">จุดแข็งของเรา</a>
                <a href="#products" class="text-slate-300 hover:text-teal transition-colors">ผลิตภัณฑ์</a>
                <a href="#technical" class="text-slate-300 hover:text-teal transition-colors">เทคโนโลยี & QC</a>
                <a href="#contact" class="text-slate-300 hover:text-teal transition-colors">ติดต่อเรา</a>
            </nav>
            <div class="hidden lg:block">
                <a href="#contact" class="bg-teal hover:bg-teal-700 text-white px-5 py-2.5 rounded-lg text-sm font-semibold transition-all duration-300 shadow-md shadow-teal-900/30">ติดต่อขอใบเสนอราคา</a>
            </div>
            <button onclick="toggleMobileMenu()" class="lg:hidden text-white focus:outline-none text-2xl">
                <i id="menu-icon" class="fa-solid fa-bars"></i>
            </button>
        </div>
        <div id="mobile-menu" class="hidden lg:hidden bg-slate-900 border-b border-slate-800 px-6 py-4 space-y-3 shadow-xl">
            <a href="#home" onclick="toggleMobileMenu()" class="block text-teal py-2 font-medium">หน้าแรก</a>
            <a href="#about" onclick="toggleMobileMenu()" class="block text-slate-300 hover:text-teal py-2 font-medium">เกี่ยวกับเรา</a>
            <a href="#key-success" onclick="toggleMobileMenu()" class="block text-slate-300 hover:text-teal py-2 font-medium">จุดแข็งของเรา</a>
            <a href="#products" onclick="toggleMobileMenu()" class="block text-slate-300 hover:text-teal py-2 font-medium">ผลิตภัณฑ์</a>
            <a href="#technical" onclick="toggleMobileMenu()" class="block text-slate-300 hover:text-teal py-2 font-medium">เทคโนโลยี & QC</a>
            <a href="#contact" onclick="toggleMobileMenu()" class="block text-slate-300 hover:text-teal py-2 font-medium">ติดต่อเรา</a>
            <a href="#contact" onclick="toggleMobileMenu()" class="block w-full text-center bg-teal text-white py-2.5 rounded-lg font-semibold mt-4">ติดต่อขอใบเสนอราคา</a>
        </div>
    </header>

    <section id="home" class="relative min-h-screen pt-20 flex items-center bg-gradient-to-br from-slate-950 via-slate-900 to-slate-800 overflow-hidden">
        <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#0D9488_1px,transparent_1px)] [background-size:16px_16px]"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 relative z-10 grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
            <div class="lg:col-span-7 space-y-6 text-left animate-fade-in">
                <div class="inline-flex items-center space-x-2 bg-slate-800/80 border border-slate-700 px-4 py-1.5 rounded-full text-xs font-semibold text-teal tracking-wide shadow-sm">
                    <span class="flex h-2 w-2 rounded-full bg-teal animate-pulse"></span>
                    <span>LEADING MINERAL SUPPLIER IN ASIA</span>
                </div>
                <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-white leading-tight">
                    Asia Mineral Supply (AMS)<br>
                    <span class="text-transparent bg-clip-text bg-gradient-to-r from-teal-400 to-cyan-400">
                        Reliable Supply of High-Purity BaSO4 & Talc
                    </span>
                </h1>
                <p class="text-base sm:text-lg text-slate-300 max-w-xl leading-relaxed">
                    ผู้จัดจำหน่ายผงแร่ธรรมชาติ Barium Sulphate ($BaSO_4$) และ Talc คุณภาพสูงมาตรฐานอุตสาหกรรม ตั้งแต่ขนาดละเอียดพิเศษ 5 ไมครอน ไปจนถึงขนาดทั่วไป 325 mesh สำหรับอุตสาหกรรมสี, พลาสติก, ยาง และการเจาะน้ำมัน
                </p>
                <div class="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4 pt-4">
                    <a href="#products" class="bg-teal hover:bg-teal-700 text-white text-center px-8 py-3.5 rounded-xl font-bold transition-all shadow-lg shadow-teal-900/40 tracking-wide">
                        ดูผลิตภัณฑ์ของเรา <i class="fa-solid fa-arrow-right ml-2 text-xs"></i>
                    </a>
                    <a href="#contact" class="border border-slate-600 hover:border-teal text-slate-200 hover:text-teal text-center px-8 py-3.5 rounded-xl font-bold transition-all bg-slate-900/40 backdrop-blur-sm">
                        ติดต่อฝ่ายขาย
                    </a>
                </div>
            </div>
            <div class="lg:col-span-5 relative flex justify-center lg:justify-end">
                <div class="relative w-full max-w-md bg-slate-800/40 p-4 rounded-3xl border border-slate-700/60 shadow-2xl backdrop-blur-sm">
                    <div class="absolute -top-4 -left-4 w-24 h-24 bg-teal/20 rounded-full blur-xl"></div>
                    <div class="absolute -bottom-4 -right-4 w-32 h-32 bg-cyan-500/10 rounded-full blur-xl"></div>
                    <img src="https://images.unsplash.com/photo-1605117882932-f9e32b17fea2?auto=format&fit=crop&q=80&w=600" alt="Mineral rocks" class="rounded-2xl shadow-inner w-full object-cover h-[400px]">
                    <div class="absolute bottom-8 left-8 right-8 bg-slate-900/95 backdrop-blur-md border border-slate-700 p-4 rounded-xl shadow-lg">
                        <p class="text-xs font-bold text-teal tracking-wide uppercase">แร่แบไรต์บริสุทธิ์สูง</p>
                        <p class="text-sm text-slate-300 mt-1">คัดสรรวัตถุดิบความขาวดัชนีสูงพิเศษเพื่อควบคุมคุณภาพชั้นเลิศ</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="about" class="py-24 bg-white border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
                <div class="space-y-6">
                    <h2 class="text-xs font-bold uppercase tracking-widest text-teal">เกี่ยวกับเรา / ABOUT US</h2>
                    <h3 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">พันธมิตรเชิงกลยุทธ์ร่วมกับ Asian Mineral Resources (AMR)</h3>
                    <p class="text-slate-600 leading-relaxed text-base">
                        <strong>Asia Mineral Supply (AMS)</strong> ทำหน้าที่เป็นกลไกและตัวแทนด้านการขายและการตลาดอย่างเป็นทางการให้แก่ <strong>Asian Mineral Resources (AMR)</strong> ซึ่งเป็นโรงงานผู้ผลิตแร่รายใหญ่ที่มีประสบการณ์และความเชี่ยวชาญการบดละเอียดแร่มาอย่างยาวนานกว่า 30 ปี
                    </p>
                    <div class="p-5 bg-slate-50 border-l-4 border-teal rounded-r-xl space-y-2">
                        <p class="text-sm font-semibold text-slate-900"><i class="fa-solid fa-map-location-dot text-teal mr-2"></i> ทำเลที่ตั้งยุทธศาสตร์แห่งศูนย์กลางแร่</p>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            ฐานการผลิตตั้งอยู่ที่ อ.พระพุทธบาท จ.สระบุรี ซึ่งได้รับการยอมรับว่าเป็นศูนย์กลางการบดและแปรรูปแร่ที่สำคัญที่สุดของประเทศไทย ตัวโรงงานตั้งอยู่ห่างจากท่าเรือกรุงเทพฯ เพียง 120 กิโลเมตร และห่างจากแนวชายแดนเชื่อมต่อประเทศเพื่อนบ้าน 500 กิโลเมตร เอื้อประโยชน์สูงสุดต่อการจัดการโลจิสติกส์ทั้งในประเทศและการส่งออกไปต่างประเทศ
                        </p>
                    </div>
                    <div>
                        <button onclick="openModal('factoryModal')" class="bg-slate-900 hover:bg-slate-800 text-white px-6 py-3 rounded-xl text-sm font-bold transition-all shadow-md inline-flex items-center">
                            <i class="fa-solid fa-industry mr-2 text-teal"></i> ดูข้อมูลกำลังการผลิตโรงงานผลิต (AMR Factory)
                        </button>
                    </div>
                </div>
                <div class="grid grid-cols-2 gap-4">
                    <div class="space-y-4">
                        <div class="bg-slate-100 rounded-2xl overflow-hidden shadow-sm h-48 border border-slate-200">
                            <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&q=80&w=400" alt="Factory inside" class="w-full h-full object-cover">
                        </div>
                        <div class="bg-slate-900 p-6 rounded-2xl text-center text-white shadow-xl border border-slate-800">
                            <p class="text-4xl font-extrabold text-teal">30+</p>
                            <p class="text-xs text-slate-400 font-medium mt-1 uppercase tracking-wide">ปีแห่งประสบการณ์การผลิตแร่</p>
                        </div>
                    </div>
                    <div class="space-y-4 pt-8">
                        <div class="bg-teal p-6 rounded-2xl text-center text-white shadow-xl shadow-teal-900/10">
                            <p class="text-4xl font-extrabold">5</p>
                            <p class="text-xs text-teal-100 font-medium mt-1 uppercase tracking-wide">สายการผลิตหลักแบบครบวงจร</p>
                        </div>
                        <div class="bg-slate-100 rounded-2xl overflow-hidden shadow-sm h-48 border border-slate-200">
                            <img src="https://images.unsplash.com/photo-1535551951406-a199435e2c88?auto=format&fit=crop&q=80&w=400" alt="QC lab" class="w-full h-full object-cover">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="key-success" class="py-24 bg-slate-50 border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <div class="max-w-3xl mx-auto space-y-4 mb-16">
                <h2 class="text-xs font-bold uppercase tracking-widest text-teal">ทำไมต้องเลือกเรา / KEY SUCCESS FACTORS</h2>
                <h3 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">หัวใจสำคัญในการขับเคลื่อนความเสถียรของซัพพลายเชน</h3>
                <p class="text-sm text-slate-500">เราผสานจุดเด่นด้านแหล่งวัตถุดิบ มาตรฐานการผลิต และชัยภูมิการจัดส่งเพื่อมอบคุณค่าสูงสุดให้ธุรกิจคุณ</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-left">
                <div class="bg-white p-8 rounded-2xl border border-slate-200 shadow-sm space-y-4 hover:shadow-md transition-shadow">
                    <div class="w-12 h-12 bg-teal/10 rounded-xl flex items-center justify-center text-teal text-xl font-bold">
                        <i class="fa-solid fa-cubes-stacked"></i>
                    </div>
                    <h4 class="text-lg font-bold text-slate-900">Supply Ability (ความมั่นคงด้านวัตถุดิบ)</h4>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        AMS ครอบคลุมแหล่งสัมปทานและซัพพลายเออร์ที่น่าเชื่อถือ 3 แหล่งหลักเพื่อกระจายความเสี่ยงและประกันความต่อเนื่องในการส่งมอบวัตถุดิบ:
                    </p>
                    <ul class="text-xs text-slate-600 space-y-2 pt-2 border-t border-slate-100">
                        <li><i class="fa-solid fa-check text-teal mr-1.5"></i> <strong>ประเทศจีน:</strong> แหล่งแร่เกรดพรีเมียม ปริมาณสำรองในชั้นดินสูงมาก มั่นใจได้ระยะยาว</li>
                        <li><i class="fa-solid fa-check text-teal mr-1.5"></i> <strong>ประเทศปากีสถาน:</strong> แร่คุณภาพดีเป็นที่ยอมรับ อยู่ระหว่างการทดสอบและขยายผลอย่างมีระบบ</li>
                        <li><i class="fa-solid fa-check text-teal mr-1.5"></i> <strong>สปป.ลาว:</strong> เน้นการคัดสรรชั้นแร่ประณีตและมีกระบวนการ Pre-wash จัดส่งรวดเร็วผ่านแนวชายแดน</li>
                    </ul>
                </div>
                <div class="bg-white p-8 rounded-2xl border border-slate-200 shadow-sm space-y-4 hover:shadow-md transition-shadow">
                    <div class="w-12 h-12 bg-teal/10 rounded-xl flex items-center justify-center text-teal text-xl font-bold">
                        <i class="fa-solid fa-microscope"></i>
                    </div>
                    <h4 class="text-lg font-bold text-slate-900">Strict Quality Control (ควบคุมคุณภาพเข้มงวด)</h4>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        เราควบคุมคุณลักษณะทางฟิสิกส์และเคมีอย่างเข้มงวดในทุก ๆ ล็อตการผลิต โดยเน้นหนักใน 2 มิติสำคัญเพื่อความเสถียรในการนำไปประยุกต์ใช้งานจริง:
                    </p>
                    <ul class="text-xs text-slate-600 space-y-2 pt-2 border-t border-slate-100">
                        <li><i class="fa-solid fa-circle text-[6px] text-teal mr-2 align-middle"></i><strong>Whiteness Index:</strong> รักษาระดับค่าความสว่างความขาวอย่างสม่ำเสมอ</li>
                        <li><i class="fa-solid fa-circle text-[6px] text-teal mr-2 align-middle"></i><strong>Particle Size Distribution (PSD):</strong> ควบคุมการกระจายตัวของขนาดอนุภาคแร่ให้ตรงตามสเปกไม่เกิดการเบี่ยงเบน</li>
                    </ul>
                </div>
                <div class="bg-white p-8 rounded-2xl border border-slate-200 shadow-sm space-y-4 hover:shadow-md transition-shadow">
                    <div class="w-12 h-12 bg-teal/10 rounded-xl flex items-center justify-center text-teal text-xl font-bold">
                        <i class="fa-solid fa-truck-fast"></i>
                    </div>
                    <h4 class="text-lg font-bold text-slate-900">Logistics Advantage (ข้อได้เปรียบด้านโลจิสติกส์)</h4>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        ด้วยชัยภูมิโรงงานในจังหวัดสระบุรีที่เชื่อมต่อโครงข่ายคมนาคมหลักได้อย่างสมบูรณ์แบบ ทำให้ระบบขนส่งและการกระจายสินค้ามีประสิทธิภาพสูงสุด:
                    </p>
                    <ul class="text-xs text-slate-600 space-y-2 pt-2 border-t border-slate-100">
                        <li><i class="fa-solid fa-circle text-[6px] text-teal mr-2 align-middle"></i>กระจายสินค้าสู่โรงงานในส่วนกลางและนิคมอุตสาหกรรมหลักได้อย่างรวดเร็ว</li>
                        <li><i class="fa-solid fa-circle text-[6px] text-teal mr-2 align-middle"></i>ย่นระยะเวลาการลากตู้คอนเทนเนอร์สู่ท่าเรือกรุงเทพฯ (BKK Port) เพื่อการส่งออก</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <section id="products" class="py-24 bg-white border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <div class="max-w-3xl mx-auto space-y-4 mb-12">
                <h2 class="text-xs font-bold uppercase tracking-widest text-teal">กลุ่มผลิตภัณฑ์ / PRODUCT RANGES</h2>
                <h3 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">แร่ผงอุตสาหกรรมบดละเอียดคุณภาพสูง</h3>
                <p class="text-sm text-slate-500">คลิกเลือกแท็บกลุ่มแร่เพื่อดูผลิตภัณฑ์ย่อย และกดปุ่มดู Specification เพื่อเปิดตารางคุณสมบัติทางเทคนิคแบบละเอียด</p>
            </div>

            <div class="flex justify-center space-x-4 mb-12">
                <button onclick="switchTab('baso4-tab', 'talc-tab', this)" class="tab-btn px-6 py-3 rounded-xl font-bold text-sm transition-all bg-slate-900 text-white shadow-md">
                    <i class="fa-solid fa-flask mr-2"></i> 1. กลุ่มสินค้า Barium Sulphate (Barytes)
                </button>
                <button onclick="switchTab('talc-tab', 'baso4-tab', this)" class="tab-btn px-6 py-3 rounded-xl font-bold text-sm transition-all bg-slate-100 text-slate-600 hover:bg-slate-200">
                    <i class="fa-solid fa-gem mr-2"></i> 2. กลุ่มสินค้า Talc (แร่ทัลก์)
                </button>
            </div>

            <div id="baso4-tab" class="tab-content grid grid-cols-1 md:grid-cols-3 gap-8 text-left">
                <div class="bg-slate-50 border border-slate-200 p-6 rounded-2xl flex flex-col justify-between shadow-sm hover:shadow-md transition-shadow">
                    <div class="space-y-4">
                        <div class="bg-gradient-to-r from-teal-600 to-teal-800 text-white text-xs px-3 py-1 rounded-md font-bold uppercase inline-block tracking-wide">Premium Grade</div>
                        <h4 class="text-xl font-extrabold text-slate-900">Microbytes Series</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            แร่แบไรต์บดละเอียดพิเศษความบริสุทธิ์สูง คัดเกรดเน้นค่าความขาวและความสว่างสูงสุด ออกแบบมาโดยเฉพาะสำหรับอุตสาหกรรมสีผงคุณภาพสูง (Powder Coating) และสีทาอาคารระดับพรีเมียม
                        </p>
                        <div class="space-y-2 pt-2">
                            <div class="flex justify-between text-xs border-b border-slate-250 pb-1"><span class="text-slate-500">ความบริสุทธิ์ $BaSO_4$</span><span class="font-semibold text-slate-900">สูงสุดถึง >98.0%</span></div>
                            <div class="flex justify-between text-xs border-b border-slate-250 pb-1"><span class="text-slate-500">ขนาดอนุภาคเฉลี่ย</span><span class="font-semibold text-slate-900">2 µ - 10 µ</span></div>
                        </div>
                    </div>
                    <button onclick="openModal('microbytesModal')" class="mt-6 w-full text-center bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold py-2.5 rounded-xl transition-colors shadow-sm">
                        ดู Specification <i class="fa-solid fa-table ml-1.5 text-[10px]"></i>
                    </button>
                </div>
                <div class="bg-slate-50 border border-slate-200 p-6 rounded-2xl flex flex-col justify-between shadow-sm hover:shadow-md transition-shadow">
                    <div class="space-y-4">
                        <div class="bg-gradient-to-r from-slate-600 to-slate-800 text-white text-xs px-3 py-1 rounded-md font-bold uppercase inline-block tracking-wide">Standard & Industrial</div>
                        <h4 class="text-xl font-extrabold text-slate-900">Milbar Series</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            สารเพิ่มเนื้อแร่แบไรต์เกรดอุตสาหกรรมและสีทั่วไป ทำหน้าที่เป็น Extender ชั้นดี ช่วยเพิ่มน้ำหนักถ่วง ควบคุมการตกตะกอน และเพิ่มความทนทานต่อการขัดถูในฟิล์มสี งานผ้าเบรค พลาสติก PP และ Wood Filler
                        </p>
                        <div class="space-y-2 pt-2">
                            <div class="flex justify-between text-xs border-b border-slate-250 pb-1"><span class="text-slate-500">ความหลากหลายเกรด</span><span class="font-semibold text-slate-900">Milbar 5 ถึง D45</span></div>
                            <div class="flex justify-between text-xs border-b border-slate-250 pb-1"><span class="text-slate-500">ขนาดทั่วไป</span><span class="font-semibold text-slate-900">325 mesh (45 µ) เป็นต้น</span></div>
                        </div>
                    </div>
                    <button onclick="openModal('milbarModal')" class="mt-6 w-full text-center bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold py-2.5 rounded-xl transition-colors shadow-sm">
                        ดู Specification <i class="fa-solid fa-table ml-1.5 text-[10px]"></i>
                    </button>
                </div>
                <div class="bg-slate-50 border border-slate-200 p-6 rounded-2xl flex flex-col justify-between shadow-sm hover:shadow-md transition-shadow">
                    <div class="space-y-4">
                        <div class="bg-gradient-to-r from-amber-600 to-amber-800 text-white text-xs px-3 py-1 rounded-md font-bold uppercase inline-block tracking-wide">Drilling Grade</div>
                        <h4 class="text-xl font-extrabold text-slate-900">T-Bar Series (API Grade)</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            ผลิตภัณฑ์แร่แบไรต์บดหยาบเกรดอุตสาหกรรมขุดเจาะน้ำมันและก๊าซธรรมชาติ ได้รับการผลิตและควบคุมสเปกให้สอดคล้องตามมาตรฐานสากล American Petroleum Institute (API Standard) อย่างเข้มงวด
                        </p>
                        <div class="space-y-2 pt-2">
                            <div class="flex justify-between text-xs border-b border-slate-250 pb-1"><span class="text-slate-500">การนำไปใช้งาน</span><span class="font-semibold text-slate-900">Weighting agent ในน้ำยาเจาะ</span></div>
                            <div class="flex justify-between text-xs border-b border-slate-250 pb-1"><span class="text-slate-500">ความถ่วงจำเพาะ (SG)</span><span class="font-semibold text-slate-900">3.90 - 4.00</span></div>
                        </div>
                    </div>
                    <button onclick="openModal('tbarModal')" class="mt-6 w-full text-center bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold py-2.5 rounded-xl transition-colors shadow-sm">
                        ดู Specification <i class="fa-solid fa-table ml-1.5 text-[10px]"></i>
                    </button>
                </div>
            </div>

            <div id="talc-tab" class="tab-content hidden grid grid-cols-1 md:grid-cols-2 gap-8 text-left max-w-4xl mx-auto">
                <div class="bg-slate-50 border border-slate-200 p-6 rounded-2xl flex flex-col justify-between shadow-sm hover:shadow-md transition-shadow">
                    <div class="space-y-4">
                        <div class="bg-gradient-to-r from-teal-600 to-teal-800 text-white text-xs px-3 py-1 rounded-md font-bold uppercase inline-block tracking-wide">Industrial & Cosmetic</div>
                        <h4 class="text-xl font-extrabold text-slate-900">Talcon Series</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            แร่ทัลก์ (Talcum Powder) คุณภาพสูง ผงละเอียดลื่น มีคุณสมบัติเด่นทนความร้อน ทนเคมี และช่วยในการหล่อลื่นผิวสัมผัส เหมาะสำหรับกลุ่มโรงงานผลิตสายยาง ด้ายยาง อุตสาหกรรมพลาสติก สีทาอาคาร และอุตสาหกรรมเครื่องสำอาง
                        </p>
                        <div class="p-3 bg-teal/5 border border-teal/20 text-teal rounded-lg text-xs font-semibold">
                            <i class="fa-solid fa-circle-check mr-1.5"></i> Special Highlight: สามารถผ่านกระบวนการฆ่าเชื้อ (Sterilization Available) ได้ตามความต้องการของลูกค้า
                        </div>
                    </div>
                    <button onclick="openModal('talconModal')" class="mt-6 w-full text-center bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold py-2.5 rounded-xl transition-colors shadow-sm">
                        ดู Specification <i class="fa-solid fa-table ml-1.5 text-[10px]"></i>
                    </button>
                </div>
                <div class="hidden md:block rounded-2xl overflow-hidden border border-slate-200 shadow-sm">
                    <img src="https://images.unsplash.com/photo-1614850523459-c2f4c699c52e?auto=format&fit=crop&q=80&w=500" alt="Talc processing" class="w-full h-full object-cover">
                </div>
            </div>
        </div>
    </section>

    <section id="technical" class="py-24 bg-slate-900 text-white relative overflow-hidden">
        <div class="absolute inset-0 opacity-5 bg-[radial-gradient(#FFFFFF_1px,transparent_1px)] [background-size:24px_24px]"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center max-w-3xl mx-auto space-y-4 mb-16">
                <h2 class="text-xs font-bold uppercase tracking-widest text-teal">ความเป็นเลิศทางเทคนิค / TECHNICAL EXCELLENCE</h2>
                <h3 class="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">การันตีความปลอดภัยและคุณภาพด้วยผลทดสอบระดับสากล</h3>
                <p class="text-sm text-slate-400">ควบคุมแล็บทดสอบด้วยเครื่องมือที่ทันสมัยและทีมวิศวกรควบคุมคุณภาพที่มีประสบการณ์สูง</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 text-left mb-16">
                <div class="bg-slate-800/60 p-6 rounded-xl border border-slate-700 space-y-3">
                    <div class="text-teal text-xl"><i class="fa-solid fa-shield-halved"></i></div>
                    <h4 class="text-sm font-bold text-white">Respirable Silica < 0.001%</h4>
                    <p class="text-xs text-slate-400 leading-relaxed">
                        ผลการทดสอบจากห้องปฏิบัติการอิสระ ณ ประเทศออสเตรเลีย ยืนยันว่ากลุ่มสินค้าพรีเมียม (Microbytes 2, 5, 7, 10) มีปริมาณฝุ่นซิลิกาที่เข้าสู่ทางเดินหายใจต่ำกว่า 0.001% ปลอดภัยอย่างยิ่งต่อผู้ใช้งานในระยะยาว
                    </p>
                </div>
                <div class="bg-slate-800/60 p-6 rounded-xl border border-slate-700 space-y-3">
                    <div class="text-teal text-xl"><i class="fa-solid fa-leaf"></i></div>
                    <h4 class="text-sm font-bold text-white">Purely Natural 100%</h4>
                    <p class="text-xs text-slate-400 leading-relaxed">
                        ผลิตภัณฑ์ทุกชิ้นสกัดและแปรรูปจากก้อนแร่ธรรมชาติแท้บริสุทธิ์ โดยปราศจากการใช้สารเคมีในกระบวนการปรับแต่งฟอกสีใด ๆ (No Chemical Pre-treatment) มั่นใจในความเป็นแร่ธรรมชาติที่แท้จริง
                    </p>
                </div>
                <div class="bg-slate-800/60 p-6 rounded-xl border border-slate-700 space-y-3">
                    <div class="text-teal text-xl"><i class="fa-solid fa-chart-area"></i></div>
                    <h4 class="text-sm font-bold text-white">SediGraph Particle Control</h4>
                    <p class="text-xs text-slate-400 leading-relaxed">
                        เราควบคุมและวิเคราะห์ช่วงการกระจายตัวของขนาดอนุภาคแร่ (PSD) และตรวจสอบขนาด Top Cut ขอบเขตบนอย่างละเอียดแม่นยำด้วยเครื่องวิเคราะห์ระดับโลกอย่าง SediGraph (Micromeritics)
                    </p>
                </div>
                <div class="bg-slate-800/60 p-6 rounded-xl border border-slate-700 space-y-3">
                    <div class="text-teal text-xl"><i class="fa-solid fa-eye"></i></div>
                    <h4 class="text-sm font-bold text-white">KETT Reflectometer Control</h4>
                    <p class="text-xs text-slate-400 leading-relaxed">
                        หมดห่วงเรื่องปัญหาความเพี้ยนของเฉดสีในเนื้อวัสดุ เพราะเราควบคุมค่าความเบี่ยงเบนของสีแร่อย่างเข้มงวดด้วยเทคโนโลยีเครื่องวัดความสะท้อนแสง KETT Reflectometer ทำให้ได้ค่าเผื่อความคลาดเคลื่อน (Tolerance) ต่ำมาก
                    </p>
                </div>
            </div>

            <div class="max-w-4xl mx-auto bg-slate-800/40 border border-slate-700 rounded-2xl p-6 shadow-xl backdrop-blur-sm">
                <h4 class="text-base font-bold text-white mb-4 text-center md:text-left"><i class="fa-solid fa-circle-info text-teal mr-2"></i> สรุปค่าความถ่วงจำเพาะ และเปอร์เซ็นต์ความชื้นคงเหลือ</h4>
                <div class="overflow-x-auto">
                    <table class="w-full text-xs text-left text-slate-300">
                        <thead class="text-[11px] uppercase tracking-wider text-teal border-b border-slate-700">
                            <tr>
                                <th class="pb-3 pt-2 px-4 font-bold">กลุ่มผลิตภัณฑ์ (Product Group)</th>
                                <th class="pb-3 pt-2 px-4 font-bold">ความถ่วงจำเพาะ (Specific Gravity)</th>
                                <th class="pb-3 pt-2 px-4 font-bold">ความชื้นคงเหลือสูงสุด (Moisture Content)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-700/60">
                            <tr class="hover:bg-slate-800/30">
                                <td class="py-3.5 px-4 font-semibold text-white">Microbytes & Milbar (5, 7, 10, A45)</td>
                                <td class="py-3.5 px-4 text-teal font-medium">&gt; 4.20</td>
                                <td class="py-3.5 px-4">&lt; 0.1%</td>
                            </tr>
                            <tr class="hover:bg-slate-800/30">
                                <td class="py-3.5 px-4 font-semibold text-white">Milbar B, C</td>
                                <td class="py-3.5 px-4 text-teal font-medium">4.00 - 4.10</td>
                                <td class="py-3.5 px-4">&lt; 0.1%</td>
                            </tr>
                            <tr class="hover:bg-slate-800/30">
                                <td class="py-3.5 px-4 font-semibold text-white">Milbar D, T-Bar 200</td>
                                <td class="py-3.5 px-4 text-teal font-medium">3.90 - 4.00</td>
                                <td class="py-3.5 px-4">0.1% - 0.2%</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </section>

    <section id="contact" class="py-24 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-16">
                <div class="lg:col-span-5 space-y-6">
                    <h2 class="text-xs font-bold uppercase tracking-widest text-teal">ติดต่อเรา / CONTACT US</h2>
                    <h3 class="text-3xl font-extrabold text-slate-900 tracking-tight">สนใจสั่งซื้อหรือขอรับตัวอย่างทดลอง</h3>
                    <p class="text-sm text-slate-600 leading-relaxed">
                        ท่านสามารถติดต่อทีมงานฝ่ายขายเพื่อสอบถามรายละเอียดข้อมูลผลิตภัณฑ์แร่ผง บรรจุภัณฑ์ เงื่อนไขราคาส่งมอบ หรือส่งคำขอรับตัวอย่างสำหรับการทำ Lab Trial ได้ตลอดเวลาทำการ
                    </p>
                    
                    <div class="space-y-4 pt-4 border-t border-slate-100 text-xs">
                        <div class="flex items-start space-x-3">
                            <div class="text-teal text-lg mt-0.5"><i class="fa-solid fa-building"></i></div>
                            <div>
                                <p class="font-bold text-slate-900">สำนักงานและโรงงานบดแร่สระบุรี (AMR Production Base)</p>
                                <p class="text-slate-500 mt-1">อ.พระพุทธบาท จ.สระบุรี, ประเทศไทย (ศูนย์กลางอุตสาหกรรมบดแร่)</p>
                            </div>
                        </div>
                        <div class="flex items-start space-x-3">
                            <div class="text-teal text-lg mt-0.5"><i class="fa-solid fa-map-pin"></i></div>
                            <div>
                                <p class="font-bold text-slate-900">สำนักงานฝ่ายขายและต่างประเทศกรุงเทพฯ (AMS Headquarters)</p>
                                <p class="text-slate-500 mt-1">กรุงเทพมหานคร, ประเทศไทย (สะดวกใกล้ท่าเรือกรุงเทพฯ 120 กม.)</p>
                            </div>
                        </div>
                        <div class="flex items-center space-x-3">
                            <div class="text-teal text-base"><i class="fa-solid fa-envelope"></i></div>
                            <div>
                                <a href="mailto:info@asiamineralsupply.com" class="font-semibold text-slate-900 hover:text-teal transition-colors">info@asiamineralsupply.com</a>
                            </div>
                        </div>
                    </div>
                    <div class="w-full h-40 bg-slate-100 rounded-xl border border-slate-200 flex items-center justify-center text-slate-400 text-xs text-center p-4">
                        <p><i class="fa-solid fa-map-location-dot text-slate-300 text-3xl block mb-2"></i> แผนที่แสดงที่ตั้งโรงงานบดแร่ จังหวัดสระบุรี และท่าเรือส่งออก</p>
                    </div>
                </div>

                <div class="lg:col-span-7 bg-slate-50 p-8 rounded-2xl border border-slate-200 shadow-sm">
                    <h4 class="text-lg font-bold text-slate-900 mb-6">แบบฟอร์มส่งข้อมูลติดต่อและขอใบเสนอราคา</h4>
                    <form onsubmit="event.preventDefault(); alert('ระบบจำลอง: ได้รับข้อมูลการติดต่อเรียบร้อยแล้ว ทีมฝ่ายขายจะติดต่อกลับโดยด่วนที่สุด');" class="space-y-4 text-xs">
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <div class="space-y-1">
                                <label class="font-semibold text-slate-700">ชื่อผู้ติดต่อ <span class="text-red-500">*</span></label>
                                <input type="text" required placeholder="คุณสมชาย ใจดี" class="w-full px-4 py-2.5 rounded-lg border border-slate-300 bg-white focus:outline-none focus:border-teal text-slate-800">
                            </div>
                            <div class="space-y-1">
                                <label class="font-semibold text-slate-700">ชื่อบริษัท / องค์กร <span class="text-red-500">*</span></label>
                                <input type="text" required placeholder="บริษัท อุตสาหกรรมผลิตสี จำกัด" class="w-full px-4 py-2.5 rounded-lg border border-slate-300 bg-white focus:outline-none focus:border-teal text-slate-800">
                            </div>
                        </div>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <div class="space-y-1">
                                <label class="font-semibold text-slate-700">อีเมลติดต่อ <span class="text-red-500">*</span></label>
                                <input type="email" required placeholder="name@company.com" class="w-full px-4 py-2.5 rounded-lg border border-slate-300 bg-white focus:outline-none focus:border-teal text-slate-800">
                            </div>
                            <div class="space-y-1">
                                <label class="font-semibold text-slate-700">เบอร์โทรศัพท์ <span class="text-red-500">*</span></label>
                                <input type="tel" required placeholder="081-XXXXXXX" class="w-full px-4 py-2.5 rounded-lg border border-slate-300 bg-white focus:outline-none focus:border-teal text-slate-800">
                            </div>
                        </div>
                        <div class="space-y-1">
                            <label class="font-semibold text-slate-700">ผลิตภัณฑ์ที่ท่านสนใจ <span class="text-red-500">*</span></label>
                            <select class="w-full px-4 py-2.5 rounded-lg border border-slate-300 bg-white focus:outline-none focus:border-teal text-slate-800">
                                <option>Microbytes Series (Premium Barium Sulphate)</option>
                                <option>Milbar Series (Standard Barium Sulphate)</option>
                                <option>T-Bar Series (API Oil Drilling Barytes)</option>
                                <option>Talcon Series (High-Quality Talc Powder)</option>
                                <option>อื่น ๆ / ต้องการขอตัวอย่างทดลองรวม</option>
                            </select>
                        </div>
                        <div class="space-y-1">
                            <label class="font-semibold text-slate-700">ข้อความเพิ่มเติม / ข้อกำหนดทางเทคนิคที่ต้องการ</label>
                            <textarea rows="4" placeholder="ระบุขนาดไมครอน, ปริมาณความต้องการใช้งานโดยประมาณ หรือรายละเอียดเกรดที่ต้องการใช้ร่วมกับชิ้นงานเพื่อขอรับคำแนะนำเพิ่ม..." class="w-full px-4 py-2.5 rounded-lg border border-slate-300 bg-white focus:outline-none focus:border-teal text-slate-800"></textarea>
                        </div>
                        <div class="pt-2">
                            <button type="submit" class="w-full bg-teal hover:bg-teal-700 text-white font-bold py-3 rounded-xl transition-all shadow-md text-sm tracking-wide">
                                <i class="fa-solid fa-paper-plane mr-2 text-xs"></i> ส่งข้อมูลคำขอไปยังฝ่ายขาย
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <footer class="bg-slate-950 text-slate-500 text-xs py-8 border-t border-slate-900 text-center">
        <p class="text-slate-400 font-semibold">&copy; 2026 Asia Mineral Supply (AMS). All Rights Reserved.</p>
        <p class="mt-1">Coordinating with Asian Mineral Resources (AMR) Production Base.</p>
    </footer>


    <div id="factoryModal" class="fixed inset-0 z-50 flex items-center justify-center opacity-0 pointer-events-none transition-all duration-300 bg-slate-950/70 backdrop-blur-sm p-4">
        <div class="bg-white rounded-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto shadow-2xl border border-slate-200 transform scale-95 transition-all duration-300">
            <div class="p-6 border-b border-slate-200 flex justify-between items-center bg-slate-900 text-white">
                <h3 class="font-extrabold text-base flex items-center"><i class="fa-solid fa-industry text-teal mr-2"></i> ข้อมูลกำลังการผลิตโรงงานผลิต AMR (สระบุรี)</h3>
                <button onclick="closeModal('factoryModal')" class="text-slate-400 hover:text-white transition-colors text-lg focus:outline-none"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <div class="p-6 space-y-4 text-xs text-slate-600">
                <p class="leading-relaxed">
                    โรงงานผลิต <strong>Asian Mineral Resources (AMR)</strong> ณ จังหวัดสระบุรี มีความพร้อมด้านเทคโนโลยีเครื่องจักรบดคัดแยกขนาดและระบบตรวจสอบคุณภาพ ประกอบไปด้วย <strong>5 สายการผลิตหลัก (5 Production Lines)</strong> ซึ่งแบ่งกำลังการผลิตอย่างชัดเจนตามกลุ่มผลิตภัณฑ์ดังนี้:
                </p>
                <div class="overflow-x-auto">
                    <table class="w-full text-left border-collapse">
                        <thead>
                            <tr class="bg-slate-50 border-b border-slate-200 text-slate-900 font-bold">
                                <th class="p-2.5">สายการผลิตหลัก</th>
                                <th class="p-2.5">ประเภทและพิกัดความละเอียด</th>
                                <th class="p-2.5 text-right">กำลังการผลิตรวม</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-700">
                            <tr>
                                <td class="p-2.5 font-semibold">Line 1: Super Fine</td>
                                <td class="p-2.5">Super Fine Barytes / Talc (ละเอียดสูงเฉลี่ย $\le$ 5 ไมครอน)</td>
                                <td class="p-2.5 text-right font-medium text-teal">2,500 MT / ปี</td>
                            </tr>
                            <tr>
                                <td class="p-2.5 font-semibold">Line 2: Fine Line A</td>
                                <td class="p-2.5">Fine Barytes / Talc (ขนาดละเอียด 5, 7, 10 ไมครอน)</td>
                                <td class="p-2.5 text-right font-medium text-teal">7,500 MT / ปี</td>
                            </tr>
                            <tr>
                                <td class="p-2.5 font-semibold">Line 3: Fine Line B</td>
                                <td class="p-2.5">Fine Barytes / Talc (ขนาดละเอียด 5, 7, 10 ไมครอน)</td>
                                <td class="p-2.5 text-right font-medium text-teal">7,500 MT / ปี</td>
                            </tr>
                            <tr>
                                <td class="p-2.5 font-semibold">Line 4: API Barytes 1</td>
                                <td class="p-2.5">API compliance Barytes (เกรดงานขุดเจาะน้ำมันมาตรฐาน API)</td>
                                <td class="p-2.5 text-right font-medium text-teal">15,000 MT / ปี</td>
                            </tr>
                            <tr>
                                <td class="p-2.5 font-semibold">Line 5: API Barytes 2</td>
                                <td class="p-2.5">API compliance Barytes (เกรดงานขุดเจาะน้ำมันมาตรฐาน API)</td>
                                <td class="p-2.5 text-right font-medium text-teal">15,000 MT / ปี</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="p-4 bg-slate-50 rounded-xl border border-slate-200">
                    <p class="font-bold text-slate-900"><i class="fa-regular fa-clock text-teal mr-1"></i> ตารางเวลาการดำเนินงานของโรงงาน:</p>
                    <p class="mt-1 font-medium text-slate-700">16 ชั่วโมงต่อวัน &times; 26 วันต่อเดือน &times; 12 เดือนเต็มต่อปี</p>
                    <p class="text-[11px] text-slate-500 mt-1">ทำให้มีปริมาณสต็อกบัฟเฟอร์หมุนเวียนคงที่ รองรับความต้องการใช้งานปริมาณมากแบบเร่งด่วนของลูกค้าได้สมบูรณ์แบบ</p>
                </div>
            </div>
        </div>
    </div>

    <div id="microbytesModal" class="fixed inset-0 z-50 flex items-center justify-center opacity-0 pointer-events-none transition-all duration-300 bg-slate-950/70 backdrop-blur-sm p-4">
        <div class="bg-white rounded-2xl max-w-4xl w-full max-h-[90vh] overflow-y-auto shadow-2xl border border-slate-200 transform scale-95 transition-all duration-300">
            <div class="p-6 border-b border-slate-200 flex justify-between items-center bg-slate-900 text-white">
                <h3 class="font-extrabold text-base flex items-center"><i class="fa-solid fa-table text-teal mr-2"></i> Technical Specifications: Microbytes Series</h3>
                <button onclick="closeModal('microbytesModal')" class="text-slate-400 hover:text-white transition-colors text-lg focus:outline-none"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <div class="p-6 space-y-4 text-xs text-slate-600">
                <p>ตารางคุณสมบัติทางเคมีและมิติอนุภาคของแร่แบไรต์บริสุทธิ์สูงเกรดพรีเมียม (Microbytes Series):</p>
                <div class="overflow-x-auto">
                    <table class="w-full text-left border-collapse border border-slate-200">
                        <thead>
                            <tr class="bg-slate-100 border-b border-slate-200 text-slate-900 font-bold">
                                <th class="p-2 border-r border-slate-200">Product Name</th>
                                <th class="p-2 border-r border-slate-200">$BaSO_4$ (%)</th>
                                <th class="p-2 border-r border-slate-200">Top Cut ($d_{98}$)</th>
                                <th class="p-2 border-r border-slate-200">Average Size ($d_{50}$)</th>
                                <th class="p-2 border-r border-slate-200">Whiteness Index</th>
                                <th class="p-2">Key Industrial Applications</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-200 text-slate-700">
                            <tr class="hover:bg-slate-50">
                                <td class="p-2 font-bold text-slate-900 border-r border-slate-200">Microbytes 2</td>
                                <td class="p-2 border-r border-slate-200">&gt;98.0%</td>
                                <td class="p-2 border-r border-slate-200">5 µ (800 mesh)</td>
                                <td class="p-2 border-r border-slate-200">2 µ (3,500 mesh)</td>
                                <td class="p-2 border-r border-slate-200 font-semibold text-teal">&gt;93%</td>
                                <td class="p-2">สีทาอาคารระดับท็อป, สีอุตสาหกรรมขั้นสูง และฟิล์มโพลิเมอร์ใส</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2 font-bold text-slate-900 border-r border-slate-200">Microbytes 5</td>
                                <td class="p-2 border-r border-slate-200">96.7%</td>
                                <td class="p-2 border-r border-slate-200">20 µ (625 mesh)</td>
                                <td class="p-2 border-r border-slate-200">5 µ (2,500 mesh)</td>
                                <td class="p-2 border-r border-slate-200 font-semibold text-teal">91%</td>
                                <td class="p-2" rowspan="3">สีผงอุตสาหกรรม (Powder Coating), สีพ่นรถยนต์ และสีอุตสาหกรรมคุณภาพสูงเกรดเงาพิเศษ (High-grade Gloss Paint)</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2 font-bold text-slate-900 border-r border-slate-200">Microbytes 7</td>
                                <td class="p-2 border-r border-slate-200">96.7%</td>
                                <td class="p-2 border-r border-slate-200">25 µ (550 mesh)</td>
                                <td class="p-2 border-r border-slate-200">7 µ (1,500 mesh)</td>
                                <td class="p-2 border-r border-slate-200 font-semibold text-teal">91%</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2 font-bold text-slate-900 border-r border-slate-200">Microbytes 10</td>
                                <td class="p-2 border-r border-slate-200">96.7%</td>
                                <td class="p-2 border-r border-slate-200">30 µ (450 mesh)</td>
                                <td class="p-2 border-r border-slate-200">10 µ (1,250 mesh)</td>
                                <td class="p-2 border-r border-slate-200 font-semibold text-teal">91%</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <p class="text-[11px] text-slate-500 italic">*ตัวเลขในวงเล็บอ้างอิงขนาดเทียบเท่าเป็นหน่วยระบบ US Mesh | ระเบียบวิธีวิเคราะห์วัดขนาดอนุภาคด้วยระบบแล็บ: SediGraph, Micromeritics</p>
            </div>
        </div>
    </div>

    <div id="milbarModal" class="fixed inset-0 z-50 flex items-center justify-center opacity-0 pointer-events-none transition-all duration-300 bg-slate-950/70 backdrop-blur-sm p-4">
        <div class="bg-white rounded-2xl max-w-4xl w-full max-h-[90vh] overflow-y-auto shadow-2xl border border-slate-200 transform scale-95 transition-all duration-300">
            <div class="p-6 border-b border-slate-200 flex justify-between items-center bg-slate-900 text-white">
                <h3 class="font-extrabold text-base flex items-center"><i class="fa-solid fa-table text-teal mr-2"></i> Technical Specifications: Milbar Series</h3>
                <button onclick="closeModal('milbarModal')" class="text-slate-400 hover:text-white transition-colors text-lg focus:outline-none"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <div class="p-6 space-y-4 text-xs text-slate-600">
                <p>ตารางคุณสมบัติทางเคมีและมิติอนุภาคของสารเติมแต่งแร่แบไรต์เกรดอุตสาหกรรม (Milbar Series):</p>
                <div class="overflow-x-auto">
                    <table class="w-full text-left border-collapse border border-slate-200">
                        <thead>
                            <tr class="bg-slate-100 border-b border-slate-200 text-slate-900 font-bold">
                                <th class="p-2 border-r border-slate-200">Product Name</th>
                                <th class="p-2 border-r border-slate-200">$BaSO_4$ (%)</th>
                                <th class="p-2 border-r border-slate-200">Top Cut ($d_{98}$)</th>
                                <th class="p-2 border-r border-slate-200">Average Size ($d_{50}$)</th>
                                <th class="p-2 border-r border-slate-200">Whiteness Index</th>
                                <th class="p-2">Key Applications</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-200 text-slate-700">
                            <tr class="hover:bg-slate-50">
                                <td class="p-2 font-bold text-slate-900 border-r border-slate-200">Milbar 5</td>
                                <td class="p-2 border-r border-slate-200">96.7%</td>
                                <td class="p-2 border-r border-slate-200">20 µ (625)</td>
                                <td class="p-2 border-r border-slate-200">5 µ (2,500)</td>
                                <td class="p-2 border-r border-slate-200">89% &plusmn; 3</td>
                                <td class="p-2" rowspan="3">สีอุตสาหกรรมทั่วไป, สารขยายเนื้อสี (Extender) ป้องกันการตกขัดถู และลดระยะเวลาการบดกระจายในถังผสมของเหลว</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2 font-bold text-slate-900 border-r border-slate-200">Milbar 7</td>
                                <td class="p-2 border-r border-slate-200">96.7%</td>
                                <td class="p-2 border-r border-slate-200">25 µ (550)</td>
                                <td class="p-2 border-r border-slate-200">7 µ (1,500)</td>
                                <td class="p-2 border-r border-slate-200">89% &plusmn; 3</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2 font-bold text-slate-900 border-r border-slate-200">Milbar 10</td>
                                <td class="p-2 border-r border-slate-200">96.7%</td>
                                <td class="p-2 border-r border-slate-200">30 µ (450)</td>
                                <td class="p-2 border-r border-slate-200">10 µ (1,250)</td>
                                <td class="p-2 border-r border-slate-200">89% &plusmn; 3</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2 font-bold text-slate-900 border-r border-slate-200">Milbar A45</td>
                                <td class="p-2 border-r border-slate-200">96.7%</td>
                                <td class="p-2 border-r border-slate-200">45 µ (325 Mesh)</td>
                                <td class="p-2 border-r border-slate-200">14 µ (900)</td>
                                <td class="p-2 border-r border-slate-200 font-semibold text-teal">90%</td>
                                <td class="p-2">สารขยายเนื้อเกรดมาตรฐาน 325 mesh สำหรับสีอุตสาหกรรม ให้สารตัวเติมสีต้นทุนต่ำแต่คงคุณสมบัติต้านทานการตกตะกอนได้ยอดเยี่ยม</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2 font-bold text-slate-900 border-r border-slate-200">Milbar B45</td>
                                <td class="p-2 border-r border-slate-200">91 - 93%</td>
                                <td class="p-2 border-r border-slate-200">45 µ (325 Mesh)</td>
                                <td class="p-2 border-r border-slate-200">14 µ (900)</td>
                                <td class="p-2 border-r border-slate-200 font-semibold">80%</td>
                                <td class="p-2" rowspan="2">กลุ่มผลิตภัณฑ์เพิ่มน้ำหนักเนื้อสีเกรดราคาประหยัด (Economy Industrial Paint Fillers) คงประสิทธิภาพเชิงกลเท่าเกรด A45 แต่ความขาวลดหลั่นลงตามดัชนี</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2 font-bold text-slate-900 border-r border-slate-200">Milbar C45</td>
                                <td class="p-2 border-r border-slate-200">91 - 93%</td>
                                <td class="p-2 border-r border-slate-200">45 µ (325 Mesh)</td>
                                <td class="p-2 border-r border-slate-200">14 µ (900)</td>
                                <td class="p-2 border-r border-slate-200 font-semibold">75%</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2 font-bold text-slate-900 border-r border-slate-200">Milbar D45</td>
                                <td class="p-2 border-r border-slate-200">93.0%</td>
                                <td class="p-2 border-r border-slate-200">45 µ (325 Mesh)</td>
                                <td class="p-2 border-r border-slate-200">14 µ (900)</td>
                                <td class="p-2 border-r border-slate-200 font-semibold">60%</td>
                                <td class="p-2">ใช้ในงานอุตสาหกรรมผ้าเบรค/ผ้าคลัตช์รถยนต์ (Brake pads / Shoe), สารเติมสีอุดรอยไม้ (Wood filler), และเป็นตัวช่วยถ่วงน้ำหนักในคอมพาวนด์พลาสติกพอลิโพรพิลีน (PP compound)</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>

    <div id="tbarModal" class="fixed inset-0 z-50 flex items-center justify-center opacity-0 pointer-events-none transition-all duration-300 bg-slate-950/70 backdrop-blur-sm p-4">
        <div class="bg-white rounded-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto shadow-2xl border border-slate-200 transform scale-95 transition-all duration-300">
            <div class="p-6 border-b border-slate-200 flex justify-between items-center bg-slate-900 text-white">
                <h3 class="font-extrabold text-base flex items-center"><i class="fa-solid fa-table text-teal mr-2"></i> Technical Specifications: T-Bar 200 (API Drilling Grade)</h3>
                <button onclick="closeModal('tbarModal')" class="text-slate-400 hover:text-white transition-colors text-lg focus:outline-none"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <div class="p-6 space-y-4 text-xs text-slate-600">
                <p>คุณสมบัติสำหรับใช้งานถ่วงน้ำหนักในโคลนขุดเจาะน้ำมันและก๊าซธรรมชาติ (API standard compliance):</p>
                <div class="overflow-x-auto">
                    <table class="w-full text-left border-collapse border border-slate-200">
                        <thead>
                            <tr class="bg-slate-100 border-b border-slate-200 text-slate-900 font-bold">
                                <th class="p-3 border-r border-slate-200">Product</th>
                                <th class="p-3 border-r border-slate-200">Specific Gravity</th>
                                <th class="p-3 border-r border-slate-200">Top Cut ($d_{98}$)</th>
                                <th class="p-3 border-r border-slate-200">Average Size ($d_{50}$)</th>
                                <th class="p-3">Whiteness Index</th>
                            </tr>
                        </thead>
                        <tbody class="text-slate-700">
                            <tr>
                                <td class="p-3 font-bold text-slate-900 border-r border-slate-200 bg-slate-50">T-Bar 200</td>
                                <td class="p-3 border-r border-slate-200 font-bold text-teal">3.90 - 4.00</td>
                                <td class="p-3 border-r border-slate-200">75 µ (200 Mesh)</td>
                                <td class="p-3 border-r border-slate-200">16 µ (700)</td>
                                <td class="p-3 text-slate-400 italic">ไม่ระบุสีเฉพาะเจาะจง (No specific color)</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="p-4 bg-amber-50 border border-amber-200 text-amber-900 rounded-xl">
                    <p class="font-semibold"><i class="fa-solid fa-triangle-exclamation mr-1"></i> หมายเหตุการใช้งาน:</p>
                    <p class="mt-1 leading-relaxed text-[11px]">
                        ผลิตภัณฑ์รุ่น T-Bar 200 นี้มุ่งเน้นการควบคุมค่าความถ่วงจำเพาะ (Specific Gravity) ให้คงที่และขนาดการกระจายตัวของขนาดอนุภาคให้ตรงตามข้อกำหนด API เพื่อทำหน้าที่เพิ่มแรงดันไฮโดรสแตติกในบ่อน้ำมันอย่างปลอดภัยสูงสุด โดยไม่มีเกณฑ์การควบคุมด้านความขาวสะอาดเหมือนเกณฑ์ของสีทาอาคาร
                    </p>
                </div>
            </div>
        </div>
    </div>

    <div id="talconModal" class="fixed inset-0 z-50 flex items-center justify-center opacity-0 pointer-events-none transition-all duration-300 bg-slate-950/70 backdrop-blur-sm p-4">
        <div class="bg-white rounded-2xl max-w-3xl w-full max-h-[90vh] overflow-y-auto shadow-2xl border border-slate-200 transform scale-95 transition-all duration-300">
            <div class="p-6 border-b border-slate-200 flex justify-between items-center bg-slate-900 text-white">
                <h3 class="font-extrabold text-base flex items-center"><i class="fa-solid fa-table text-teal mr-2"></i> Technical Specifications: Talcon Series (แร่ทัลก์)</h3>
                <button onclick="closeModal('talconModal')" class="text-slate-400 hover:text-white transition-colors text-lg focus:outline-none"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <div class="p-6 space-y-4 text-xs text-slate-600">
                <p>สเปกทางเทคนิคของกลุ่มแร่ทัลก์แปรรูปบดละเอียด (Talcon Series):</p>
                <div class="overflow-x-auto">
                    <table class="w-full text-left border-collapse border border-slate-200">
                        <thead>
                            <tr class="bg-slate-100 border-b border-slate-200 text-slate-900 font-bold">
                                <th class="p-3 border-r border-slate-200">Product Name</th>
                                <th class="p-3 border-r border-slate-200">Top Size Limit</th>
                                <th class="p-3 border-r border-slate-200">Median Size ($d_{50}$)</th>
                                <th class="p-3 border-r border-slate-200">Whiteness Index</th>
                                <th class="p-3">Key Applications & Markets</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-200 text-slate-700">
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-slate-900 border-r border-slate-200">Talcon BC20</td>
                                <td class="p-3 border-r border-slate-200">20 µ (630 mesh)</td>
                                <td class="p-3 border-r border-slate-200">6.0 - 7.0 µ</td>
                                <td class="p-3 border-r border-slate-200 font-semibold text-teal">91%</td>
                                <td class="p-3">อุตสาหกรรมสายยาง, ด้ายยางยืด (Rubber Thread) และส่วนผสมพลาสติกวิศวกรรมเพื่อรับแรงกระแทก</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-slate-900 border-r border-slate-200">Talcon BC45</td>
                                <td class="p-3 border-r border-slate-200">45 µ (325 mesh)</td>
                                <td class="p-3 border-r border-slate-200">12.0 - 15.0 µ</td>
                                <td class="p-3 border-r border-slate-200 font-semibold text-teal">90%</td>
                                <td class="p-3">อุตสาหกรรมแป้งผสมเครื่องสำอาง (Cosmetics), สารเติมเนื้อสีอุตสาหกรรม และงานเซรามิกทั่วไป</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="p-4 bg-teal/5 border border-teal/20 rounded-xl text-slate-800">
                    <p class="font-bold text-teal"><i class="fa-solid fa-circle-check mr-1"></i> บริการเสริมพิเศษสำหรับการใช้งานจำเพาะ:</p>
                    <p class="mt-1 leading-relaxed">
                        ทั้งผลิตภัณฑ์ <strong>Talcon BC20</strong> และ <strong>Talcon BC45</strong> สามารถส่งเข้ากระบวนการฆ่าเชื้อเพิ่มเติม (Sterilization Process Available) ตามข้อบังคับมาตรฐานความปลอดภัยสาธารณสุขและเกณฑ์ของลูกค้าแต่ละอุตสาหกรรมได้
                    </p>
                </div>
            </div>
        </div>
    </div>


    <script>
        // 1. ควบคุม Mobile Menu สลับการเปิด-ปิดหน้าเมนูย่อย
        function toggleMobileMenu() {
            const menu = document.getElementById('mobile-menu');
            const icon = document.getElementById('menu-icon');
            if (menu.classList.contains('hidden')) {
                menu.classList.remove('hidden');
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-xmark');
            } else {
                menu.classList.add('hidden');
                icon.classList.remove('fa-xmark');
                icon.classList.add('fa-bars');
            }
        }

        // 2. ควบคุมการสลับแท็บสินค้าระหว่าง BaSO4 และ Talc
        function switchTab(showId, hideId, activeBtn) {
            // ซ่อนและแสดงเนื้อหาแท็บ
            document.getElementById(showId).classList.remove('hidden');
            document.getElementById(hideId).classList.add('hidden');
            
            // ปรับสไตล์สีของปุ่มกดแท็บทั้งหมด
            const buttons = document.querySelectorAll('.tab-btn');
            buttons.forEach(btn => {
                btn.classList.remove('bg-slate-900', 'text-white', 'shadow-md');
                btn.classList.add('bg-slate-100', 'text-slate-600');
            });
            
            // เพิ่มสีให้ปุ่มที่กำลังแอคทีฟอยู่ปัจจุบัน
            activeBtn.classList.remove('bg-slate-100', 'text-slate-600');
            activeBtn.classList.add('bg-slate-900', 'text-white', 'shadow-md');
        }

        // 3. ฟังก์ชันเปิดป๊อปอัพโหมดัล (Modal Window Open) มีแอนิเมชันเปิดแบบเฟดเข้า
        function openModal(modalId) {
            const modal = document.getElementById(modalId);
            modal.classList.remove('opacity-0', 'pointer-events-none');
            modal.classList.add('opacity-100', 'pointer-events-auto');
            
            // ใส่แอนิเมชันให้กับกล่องคอนเทนเนอร์ภายในตัวโหมดัล
            const contentBox = modal.querySelector('div');
            contentBox.classList.remove('scale-95');
            contentBox.classList.add('scale-100');
            
            // ล็อกหน้าจอหลักไม่ให้เลื่อนเมื่อเปิดป๊อปอัพซ้อนอยู่
            document.body.style.overflow = 'hidden';
        }

        // 4. ฟังก์ชันปิดป๊อปอัพโหมดัล (Modal Window Close)
        function closeModal(modalId) {
            const modal = document.getElementById(modalId);
            modal.classList.remove('opacity-100', 'pointer-events-auto');
            modal.classList.add('opacity-0', 'pointer-events-none');
            
            const contentBox = modal.querySelector('div');
            contentBox.classList.remove('scale-100');
            contentBox.classList.add('scale-95');
            
            // คืนค่าการเลื่อนหน้าจอหลักตามปกติ
            document.body.style.overflow = 'auto';
        }

        // 5. ปิดป๊อปอัพโดยอัตโนมัติเมื่อผู้ใช้คลิกโดนพื้นที่ Backdrop ว่างด้านนอกกล่องตาราง
        window.onclick = function(event) {
            const modals = ['factoryModal', 'microbytesModal', 'milbarModal', 'tbarModal', 'talconModal'];
            modals.forEach(id => {
                const modal = document.getElementById(id);
                if (event.target === modal) {
                    closeModal(id);
                }
            });
        }
    </script>
</body>
</html>
"""

# คำสั่งของ Streamlit ในการแสดงผลโค้ด HTML/JS ทั้งหมดออกไปยังเว็บบราวเซอร์แบบดั้งเดิม
st.components.v1.html(html_code, height=4500, scroller=False)
