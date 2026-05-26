import streamlit as st

# ตั้งค่าหน้าเพจของ Streamlit ให้เป็นแบบกว้าง (Wide Layout) และตั้งชื่อ Title
st.set_page_config(
    page_title="Asia Mineral Supply (AMS) - Premium Mineral Supplier",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# โค้ด HTML, CSS (Tailwind), และ JavaScript สำหรับเว็บไซต์หน้าเดียว (SPA)
html_code = """
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Asia Mineral Supply (AMS)</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <style>
        body {
            font-family: 'Plus Jakarta Sans', 'Inter', sans-serif;
            background-color: #f8fafc;
            color: #1e293b;
        }
        .font-serif {
            font-family: 'Playfair Display', serif;
        }
        /* Custom Brand Colors */
        .bg-brand-teal { background-color: #0b2c3d; }
        .text-brand-teal { color: #0b2c3d; }
        .border-brand-teal { border-color: #0b2c3d; }
        
        .bg-brand-gold { background-color: #c5a059; }
        .text-brand-gold { color: #c5a059; }
        .border-brand-gold { border-color: #c5a059; }
        .hover-bg-brand-gold:hover { background-color: #b38f48; }
    </style>
</head>
<body class="bg-[#f8fafc]">

    <nav class="sticky top-0 z-50 bg-[#0b2c3d] text-white shadow-xl border-b border-slate-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-20">
                <div class="flex items-center">
                    <div class="flex-shrink-0 flex flex-col">
                        <span class="font-serif text-2xl font-bold tracking-wider text-[#c5a059]">AMS</span>
                        <span class="text-xs tracking-widest text-slate-400 font-light -mt-1">ASIA MINERAL SUPPLY</span>
                    </div>
                </div>
                <div class="hidden md:block">
                    <div class="ml-10 flex items-center space-x-8 text-sm font-medium tracking-wide">
                        <a href="#about" class="hover:text-[#c5a059] transition-colors duration-300">About Us</a>
                        <a href="#products" class="hover:text-[#c5a059] transition-colors duration-300">Products</a>
                        <a href="#manufacturing" class="hover:text-[#c5a059] transition-colors duration-300">Manufacturing & QC</a>
                        <a href="#applications" class="hover:text-[#c5a059] transition-colors duration-300">Applications</a>
                        <a href="#contact" class="hover:text-[#c5a059] transition-colors duration-300">Contact Us</a>
                        <a href="#contact" class="bg-[#c5a059] text-[#0b2c3d] px-5 py-2.5 rounded font-semibold shadow-lg hover:bg-[#b38f48] transition-all duration-300 transform hover:-translate-y-0.5">Request Quote / COA</a>
                    </div>
                </div>
                <div class="md:hidden">
                    <button id="mobile-menu-button" class="text-slate-300 hover:text-white focus:outline-none">
                        <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                        </svg>
                    </button>
                </div>
            </div>
        </div>
        <div id="mobile-menu" class="hidden md:hidden bg-[#0b2c3d] px-4 pt-2 pb-4 space-y-2 border-t border-slate-800">
            <a href="#about" class="block text-slate-300 hover:text-white py-2">About Us</a>
            <a href="#products" class="block text-slate-300 hover:text-white py-2">Products</a>
            <a href="#manufacturing" class="block text-slate-300 hover:text-white py-2">Manufacturing & QC</a>
            <a href="#applications" class="block text-slate-300 hover:text-white py-2">Applications</a>
            <a href="#contact" class="block text-slate-300 hover:text-white py-2">Contact Us</a>
            <a href="#contact" class="block bg-[#c5a059] text-[#0b2c3d] text-center px-4 py-2 rounded font-semibold mt-4">Request Quote / COA</a>
        </div>
    </nav>

    <header class="relative bg-[#0b2c3d] text-white overflow-hidden py-24 lg:py-32">
        <div class="absolute inset-0 opacity-10">
            <div class="absolute top-0 left-0 w-full h-full bg-[radial-gradient(#c5a059_1px,transparent_1px)] [background-size:16px_16px]"></div>
        </div>
        <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="lg:w-2/3">
                <span class="inline-block border border-[#c5a059] text-[#c5a059] font-medium text-xs uppercase tracking-widest px-3 py-1 rounded-full mb-6">World-Class Industrial Minerals</span>
                <h1 class="font-serif text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight leading-tight mb-6">
                    Reliable supply of powder <br><span class="text-[#c5a059]">Barium Sulphate (BaSO₄)</span> & Talc
                </h1>
                <p class="text-lg sm:text-xl text-slate-300 max-w-2xl font-light leading-relaxed mb-10">
                    Partnering with Asian Mineral Resources (AMR). Over 30 years of premier mineral processing heritage in Saraburi, Thailand. Delivering ultra-pure minerals globally.
                </p>
                <div class="flex flex-col sm:flex-row gap-4">
                    <a href="#products" class="bg-[#c5a059] text-[#0b2c3d] px-8 py-3.5 rounded font-semibold shadow-lg text-center hover:bg-[#b38f48] transition-all duration-300 transform hover:-translate-y-0.5">
                        Download Technical Specs
                    </a>
                    <a href="#contact" class="border border-slate-500 text-white px-8 py-3.5 rounded font-semibold text-center hover:bg-slate-800 hover:border-white transition-all duration-300">
                        Contact Sales
                    </a>
                </div>
            </div>
        </div>
    </header>

    <section id="about" class="py-24 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid lg:grid-cols-12 gap-16 items-center">
            <div class="lg:col-span-5">
                <span class="text-xs font-bold tracking-widest text-[#c5a059] uppercase block mb-2">Corporate Profile</span>
                <h2 class="font-serif text-3xl sm:text-4xl font-bold text-[#0b2c3d] mb-6">Strategic Partnership in Mineral Processing</h2>
                <p class="text-slate-600 leading-relaxed mb-6">
                    <strong>Asia Mineral Supply (AMS)</strong> acts as the exclusive Sales & Marketing arm to <strong>Asian Mineral Resources (AMR)</strong>, our affiliated production hub with over 30 years of extensive grinding mill expertise.
                </p>
                <p class="text-slate-600 leading-relaxed mb-8">
                    Strategically located 120 kilometers east of Bangkok at the center of <strong>Saraburi</strong>—the historical heartland of Thailand's mineral grinding industry—our facility enables streamlined logistics directly to the Bangkok Port for rapid international shipment.
                </p>
                <div class="border-l-4 border-[#c5a059] pl-4 italic text-slate-700 bg-slate-100 p-4 rounded-r shadow-sm">
                    "Dedicated to supplying natural premium functional fillers ranging from ultra-fine 5 micron powders to industry-standard 325 mesh aggregates."
                </div>
            </div>
            
            <div class="lg:col-span-7">
                <h3 class="text-xl font-bold text-[#0b2c3d] mb-6 flex items-center">
                    <span class="bg-[#0b2c3d] text-white w-2 h-6 inline-block mr-3"></span>
                    Global Supply Diversity & Chain Security
                </h3>
                <div class="grid sm:grid-cols-3 gap-6">
                    <div class="bg-white p-6 rounded-lg shadow-md border-t-4 border-[#0b2c3d]">
                        <div class="text-[#c5a059] font-bold text-lg mb-2">China</div>
                        <p class="text-sm text-slate-600 leading-relaxed">High quality reserves backed by abundant, established geological deposits ensuring long-term volume stability.</p>
                    </div>
                    <div class="bg-white p-6 rounded-lg shadow-md border-t-4 border-[#c5a059]">
                        <div class="text-[#0b2c3d] font-bold text-lg mb-2">Laos</div>
                        <p class="text-sm text-slate-600 leading-relaxed">Immediate cross-border logistical access. Strict pre-wash and tailored ore selection controls enforced at the frontier.</p>
                    </div>
                    <div class="bg-white p-6 rounded-lg shadow-md border-t-4 border-slate-400">
                        <div class="text-slate-500 font-bold text-lg mb-2">Pakistan</div>
                        <p class="text-sm text-slate-600 leading-relaxed">Alternative supply channels offering highly acceptable grade quality, with ongoing supply capability verification.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="manufacturing" class="py-24 bg-slate-900 text-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <span class="text-xs font-bold tracking-widest text-[#c5a059] uppercase block mb-2">Industrial Capacity</span>
                <h2 class="font-serif text-3xl sm:text-4xl font-bold mb-4">Advanced Grinding Infrastructure</h2>
                <p class="text-slate-400">Operating 5 highly customized processing lines running 16 hours a day to deliver over 25,000+ MT annual output capacity of Barytes and high-grade Talc.</p>
            </div>

            <div class="grid sm:grid-cols-2 lg:grid-cols-5 gap-6 mb-20">
                <div class="bg-slate-800 p-6 rounded border border-slate-700 hover:border-[#c5a059] transition-all">
                    <div class="text-xs text-slate-400 uppercase tracking-wider mb-1">Line 1: Super Fine</div>
                    <div class="text-xl font-bold text-[#c5a059] mb-2">2,500 MT / Year</div>
                    <p class="text-xs text-slate-300">Down to 5 Micron ultra-fine classification for premium applications.</p>
                </div>
                <div class="bg-slate-800 p-6 rounded border border-slate-700 hover:border-[#c5a059] transition-all">
                    <div class="text-xs text-slate-400 uppercase tracking-wider mb-1">Line 2: Fine Grade</div>
                    <div class="text-xl font-bold text-[#c5a059] mb-2">7,500 MT / Year</div>
                    <p class="text-xs text-slate-300">Targeted sizing protocols at 5µ, 7µ, and 10µ distributions.</p>
                </div>
                <div class="bg-slate-800 p-6 rounded border border-slate-700 hover:border-[#c5a059] transition-all">
                    <div class="text-xs text-slate-400 uppercase tracking-wider mb-1">Line 3: Fine Grade</div>
                    <div class="text-xl font-bold text-[#c5a059] mb-2">7,500 MT / Year</div>
                    <p class="text-xs text-slate-300">Parallel manufacturing line specialized in sharp particle distribution.</p>
                </div>
                <div class="bg-slate-800 p-6 rounded border border-slate-700 hover:border-[#c5a059] transition-all">
                    <div class="text-xs text-slate-400 uppercase tracking-wider mb-1">Line 4: API Barytes</div>
                    <div class="text-xl font-bold text-[#c5a059] mb-2">15,000 MT / Year</div>
                    <p class="text-xs text-slate-300">Dedicated high-density milling for functional heavy weighting agents.</p>
                </div>
                <div class="bg-slate-800 p-6 rounded border border-slate-700 hover:border-[#c5a059] transition-all">
                    <div class="text-xs text-slate-400 uppercase tracking-wider mb-1">Line 5: API Barytes</div>
                    <div class="text-xl font-bold text-[#c5a059] mb-2">15,000 MT / Year</div>
                    <p class="text-xs text-slate-300">Scale replication ensuring zero downtime and continuous strategic output.</p>
                </div>
            </div>

            <div id="products" class="bg-slate-800 rounded-xl p-6 sm:p-8 border border-slate-700 shadow-2xl">
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center border-b border-slate-700 pb-6 mb-8 gap-4">
                    <div>
                        <h3 class="text-2xl font-bold font-serif text-white">Interactive Specifications Portal</h3>
                        <p class="text-xs text-slate-400 mt-1">Verified via SediGraph (Micromeritics) methodology & KETT Reflectometer controls</p>
                    </div>
                    <div class="flex bg-slate-900 p-1.5 rounded-lg border border-slate-700">
                        <button id="baso4-btn" onclick="switchTab('baso4')" class="px-4 py-2 text-sm rounded font-medium bg-[#c5a059] text-[#0b2c3d] transition-all">
                            Barium Sulphate (BaSO₄)
                        </button>
                        <button id="talc-btn" onclick="switchTab('talc')" class="px-4 py-2 text-sm rounded font-medium text-slate-400 hover:text-white transition-all">
                            Talc Ranges
                        </button>
                    </div>
                </div>

                <div id="baso4-panel" class="tab-content overflow-x-auto">
                    <table class="w-full text-left border-collapse text-sm">
                        <thead>
                            <tr class="border-b border-slate-700 text-[#c5a059] uppercase tracking-wider text-xs">
                                <th class="pb-3 pl-2">Product Name</th>
                                <th class="pb-3">BaSO₄ Min.</th>
                                <th class="pb-3">Top Cut (d98)</th>
                                <th class="pb-3">Average Size</th>
                                <th class="pb-3">Whiteness Index</th>
                                <th class="pb-3">Specific Gravity</th>
                                <th class="pb-3 pr-2">Moisture Max.</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-700 text-slate-300">
                            <tr class="hover:bg-slate-700/50">
                                <td class="py-3 pl-2 font-semibold text-white">Microbytes 2</td>
                                <td class="py-3">&gt;98.0%</td>
                                <td class="py-3">14 µ <span class="text-slate-500">(800 mesh)</span></td>
                                <td class="py-3">2 µ <span class="text-slate-500">(3,500 mesh)</span></td>
                                <td class="py-3">&gt;93%</td>
                                <td class="py-3">&gt;4.20</td>
                                <td class="py-3 pr-2">0.1%</td>
                            </tr>
                            <tr class="hover:bg-slate-700/50">
                                <td class="py-3 pl-2 font-semibold text-white">Microbytes 5</td>
                                <td class="py-3">96.7%</td>
                                <td class="py-3">20 µ <span class="text-slate-500">(625 mesh)</span></td>
                                <td class="py-3">5 µ <span class="text-slate-500">(2,500 mesh)</span></td>
                                <td class="py-3">91%</td>
                                <td class="py-3">&gt;4.20</td>
                                <td class="py-3 pr-2">0.1%</td>
                            </tr>
                            <tr class="hover:bg-slate-700/50">
                                <td class="py-3 pl-2 font-semibold text-white">Microbytes 7</td>
                                <td class="py-3">96.7%</td>
                                <td class="py-3">25 µ <span class="text-slate-500">(550 mesh)</span></td>
                                <td class="py-3">7 µ <span class="text-slate-500">(1,500 mesh)</span></td>
                                <td class="py-3">91%</td>
                                <td class="py-3">&gt;4.20</td>
                                <td class="py-3 pr-2">0.1%</td>
                            </tr>
                            <tr class="hover:bg-slate-700/50">
                                <td class="py-3 pl-2 font-semibold text-white">Microbytes 10</td>
                                <td class="py-3">96.7%</td>
                                <td class="py-3">30 µ <span class="text-slate-500">(450 mesh)</span></td>
                                <td class="py-3">10 µ <span class="text-slate-500">(1,250 mesh)</span></td>
                                <td class="py-3">91%</td>
                                <td class="py-3">&gt;4.20</td>
                                <td class="py-3 pr-2">0.1%</td>
                            </tr>
                            <tr class="hover:bg-slate-700/50">
                                <td class="py-3 pl-2 font-semibold text-white">Milbar 5 / 7 / 10</td>
                                <td class="py-3">96.7%</td>
                                <td class="py-3">20 / 25 / 30 µ</td>
                                <td class="py-3">5 / 7 / 10 µ</td>
                                <td class="py-3">89% <span class="text-slate-500">(±3)</span></td>
                                <td class="py-3">&gt;4.20</td>
                                <td class="py-3 pr-2">0.1%</td>
                            </tr>
                            <tr class="hover:bg-slate-700/50">
                                <td class="py-3 pl-2 font-semibold text-white">Milbar A45</td>
                                <td class="py-3">96.7%</td>
                                <td class="py-3">45 µ <span class="text-slate-500">(325 mesh)</span></td>
                                <td class="py-3">14 µ <span class="text-slate-500">(900 mesh)</span></td>
                                <td class="py-3">90%</td>
                                <td class="py-3">&gt;4.20</td>
                                <td class="py-3 pr-2">0.1%</td>
                            </tr>
                            <tr class="hover:bg-slate-700/50">
                                <td class="py-3 pl-2 font-semibold text-white">Milbar D45</td>
                                <td class="py-3">93.0%</td>
                                <td class="py-3">45 µ <span class="text-slate-500">(325 mesh)</span></td>
                                <td class="py-3">14 µ <span class="text-slate-500">(900 mesh)</span></td>
                                <td class="py-3">60%</td>
                                <td class="py-3">3.90 - 4.00</td>
                                <td class="py-3 pr-2">0.1%</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div id="talc-panel" class="tab-content hidden overflow-x-auto">
                    <table class="w-full text-left border-collapse text-sm">
                        <thead>
                            <tr class="border-b border-slate-700 text-[#c5a059] uppercase tracking-wider text-xs">
                                <th class="pb-3 pl-2">Product Name</th>
                                <th class="pb-3">Top Size Max</th>
                                <th class="pb-3">Median Particle Size</th>
                                <th class="pb-3">Whiteness Index</th>
                                <th class="pb-3">Primary Applications</th>
                                <th class="pb-3 pr-2">Sterilization Available</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-700 text-slate-300">
                            <tr class="hover:bg-slate-700/50">
                                <td class="py-4 pl-2 font-semibold text-white">Talcon BC20</td>
                                <td class="py-4">20 µ <span class="text-slate-500">(630 mesh)</span></td>
                                <td class="py-4">6.0 - 7.0 µ</td>
                                <td class="py-4 text-[#c5a059] font-medium">91%</td>
                                <td class="py-4">Industrial Rubber Thread Manufacture</td>
                                <td class="py-4 pr-2 text-emerald-400">Yes (Upon Request)</td>
                            </tr>
                            <tr class="hover:bg-slate-700/50">
                                <td class="py-4 pl-2 font-semibold text-white">Talcon BC45</td>
                                <td class="py-4">45 µ <span class="text-slate-500">(325 mesh)</span></td>
                                <td class="py-4">12.0 - 15.0 µ</td>
                                <td class="py-4 text-[#c5a059] font-medium">90%</td>
                                <td class="py-4">Premium Cosmetics & High-Grade Paints</td>
                                <td class="py-4 pr-2 text-emerald-400">Yes (Upon Request)</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="mt-16 grid md:grid-cols-3 gap-8 text-center sm:text-left">
                <div class="bg-slate-800/40 p-6 rounded-lg border border-slate-700">
                    <div class="text-[#c5a059] mb-3">
                        <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                        </svg>
                    </div>
                    <h4 class="text-lg font-bold mb-2">Zero Silica Certified</h4>
                    <p class="text-xs text-slate-400 leading-relaxed">Independent laboratory testing in Australia certifies that our Respirable Crystalline Silica content is strictly &lt; 0.001%, guaranteeing absolute industrial safety.</p>
                </div>
                <div class="bg-slate-800/40 p-6 rounded-lg border border-slate-700">
                    <div class="text-[#c5a059] mb-3">
                        <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4.871 4A17.926 17.926 0 003 12c0 2.871.67 5.59 1.871 8m14.13 0a17.93 17.93 0 01-14.13 0m14.13 0A17.926 17.926 0 0021 12c0-2.871-.67-5.59-1.871-8m-14.13 0a17.93 17.93 0 0114.13 0M9 9l3 3-3 3m5 0h.01" />
                        </svg>
                    </div>
                    <h4 class="text-lg font-bold mb-2">Pure Natural Product</h4>
                    <p class="text-xs text-slate-400 leading-relaxed">Zero chemical pre-treatment of our raw Barytes lump minerals. Our products maintain pure, natural, original physical characteristics.</p>
                </div>
                <div class="bg-slate-800/40 p-6 rounded-lg border border-slate-700">
                    <div class="text-[#c5a059] mb-3">
                        <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width
