import streamlit as st

# ตั้งค่าหน้าเพจของ Streamlit ให้เป็นแบบกว้าง (Wide Layout) และตั้งชื่อ Title
st.set_page_config(
    page_title="Asia Mineral Supply (AMS) - Premium Mineral Supplier",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# โค้ด HTML, CSS (Tailwind), และ JavaScript สำหรับเว็บไซต์หน้าเดียว (SPA)
html_code = """<!DOCTYPE html>
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
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                        </svg>
                    </div>
                    <h4 class="text-lg font-bold mb-2">Strict PSD Control</h4>
                    <p class="text-xs text-slate-400 leading-relaxed">Narrow-range Particle Size Distribution (PSD) managed by elite, veteran quality control specialists and structural engineers.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="applications" class="py-24 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-3xl mx-auto mb-16">
            <span class="text-xs font-bold tracking-widest text-[#c5a059] uppercase block mb-2">Cross-Industry Solutions</span>
            <h2 class="font-serif text-3xl sm:text-4xl font-bold text-[#0b2c3d]">Tailored Industry Performance</h2>
        </div>

        <div class="grid md:grid-cols-3 gap-8">
            <div class="bg-white p-8 rounded-xl shadow-sm border border-slate-100 hover:shadow-xl transition-all duration-300">
                <div class="w-12 h-12 rounded-lg bg-slate-100 flex items-center justify-center text-[#c5a059] mb-6">
                    <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01" />
                    </svg>
                </div>
                <h3 class="text-xl font-bold text-[#0b2c3d] mb-4">Color, Paint & Extenders</h3>
                <ul class="text-sm text-slate-600 space-y-3">
                    <li class="flex items-start"><span class="text-[#c5a059] mr-2">•</span> Specialized 15% loading formulas for high-end powder coating.</li>
                    <li class="flex items-start"><span class="text-[#c5a059] mr-2">•</span> Serves as an architectural filler to optimize scrub-resistance in decorative paints.</li>
                    <li class="flex items-start"><span class="text-[#c5a059] mr-2">•</span> Exceptionally low dispersion time curves in commercial liquid matrices.</li>
                </ul>
            </div>
            
            <div class="bg-white p-8 rounded-xl shadow-sm border border-slate-100 hover:shadow-xl transition-all duration-300">
                <div class="w-12 h-12 rounded-lg bg-slate-100 flex items-center justify-center text-[#c5a059] mb-6">
                    <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" />
                    </svg>
                </div>
                <h3 class="text-xl font-bold text-[#0b2c3d] mb-4">Plastics & Polymers</h3>
                <ul class="text-sm text-slate-600 space-y-3">
                    <li class="flex items-start"><span class="text-[#c5a059] mr-2">•</span> Ideal structural weighting agent integrated into technical PP compounding.</li>
                    <li class="flex items-start"><span class="text-[#c5a059] mr-2">•</span> Low-cost functional white base extenders for sound-dampening thermoplastics.</li>
                </ul>
            </div>

            <div class="bg-white p-8 rounded-xl shadow-sm border border-slate-100 hover:shadow-xl transition-all duration-300">
                <div class="w-12 h-12 rounded-lg bg-slate-100 flex items-center justify-center text-[#c5a059] mb-6">
                    <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                    </svg>
                </div>
                <h3 class="text-xl font-bold text-[#0b2c3d] mb-4">Friction, Seals & Drilling</h3>
                <ul class="text-sm text-slate-600 space-y-3">
                    <li class="flex items-start"><span class="text-[#c5a059] mr-2">•</span> Heavy-duty structural base for automotive break pad/shoe lining applications.</li>
                    <li class="flex items-start"><span class="text-[#c5a059] mr-2">•</span> Primers, dense wood fillers, and architectural plywood sealants (Milbar D45).</li>
                    <li class="flex items-start"><span class="text-[#c5a059] mr-2">•</span> Fully compliant API standard oil-drilling grade mud-weighting agents (T-Bar 200).</li>
                </ul>
            </div>
        </div>
    </section>

    <section id="contact" class="py-24 bg-slate-50 border-t border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid lg:grid-cols-12 gap-16">
                <div class="lg:col-span-5">
                    <span class="text-xs font-bold tracking-widest text-[#c5a059] uppercase block mb-2">Connect With Us</span>
                    <h2 class="font-serif text-3xl font-bold text-[#0b2c3d] mb-6">Request Samples & Technical Documentation</h2>
                    <p class="text-slate-600 mb-8 leading-relaxed">
                        Secure certified copies of our Certificate of Analysis (COA), Technical Data Sheets (TDS), or request specific laboratory-grade samples for your compounding trials.
                    </p>
                    
                    <div class="space-y-6">
                        <div class="flex items-start">
                            <div class="text-[#c5a059] mt-1 mr-4">
                                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                                </svg>
                            </div>
                            <div>
                                <h4 class="font-bold text-[#0b2c3d]">Production Plant Location</h4>
                                <p class="text-sm text-slate-600 mt-1">Saraburi Industrial Grinding Hub (120 km from Bangkok Port), Thailand.</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="lg:col-span-7 bg-white p-8 rounded-xl shadow-lg border border-slate-100">
                    <h3 class="text-xl font-bold text-[#0b2c3d] mb-6 font-serif">Direct Correspondence Channels</h3>
                    
                    <div class="grid sm:grid-cols-2 gap-6">
                        <div class="p-6 bg-slate-50 rounded-lg border border-slate-200 hover:border-[#c5a059] transition-all">
                            <div class="flex items-center space-x-3 mb-3">
                                <div class="bg-[#0b2c3d] text-white p-2 rounded-md">
                                    <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L22 8m-9 13h4a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                                    </svg>
                                </div>
                                <div>
                                    <h4 class="font-bold text-slate-800">Srisuphat</h4>
                                    <p class="text-xs text-slate-500 font-medium uppercase tracking-wider">Customer Service & Export</p>
                                </div>
                            </div>
                            <p class="text-xs text-slate-400 mb-2">For international bookings, logistics, container tracking, and customer supply schedules:</p>
                            <a href="mailto:export@amsth.com" class="text-sm font-semibold text-[#0b2c3d] hover:text-[#c5a059] break-all flex items-center gap-1">
                                export@amsth.com
                                <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                            </a>
                        </div>

                        <div class="p-6 bg-slate-50 rounded-lg border border-slate-200 hover:border-[#c5a059] transition-all">
                            <div class="flex items-center space-x-3 mb-3">
                                <div class="bg-[#c5a059] text-[#0b2c3d] p-2 rounded-md">
                                    <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                                    </svg>
                                </div>
                                <div>
                                    <h4 class="font-bold text-slate-800">Prin Wangtanapat</h4>
                                    <p class="text-xs text-slate-500 font-medium uppercase tracking-wider">Assistant Manager</p>
                                </div>
                            </div>
                            <p class="text-xs text-slate-400 mb-2">For contract negotiations, raw material specifications, custom milling meshes, and B2B pricing setup:</p>
                            <a href="mailto:prinwtp@amsth.com" class="text-sm font-semibold text-[#0b2c3d] hover:text-[#c5a059] break-all flex items-center gap-1">
                                prinwtp@amsth.com
                                <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <footer class="bg-[#0b2c3d] text-slate-400 py-12 border-t border-slate-800 text-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row justify-between items-center gap-4">
            <div>
                <span class="font-serif text-white font-bold tracking-wider">AMS</span> | Asia Mineral Supply. All rights reserved.
            </div>
            <div class="flex space-x-6 text-xs">
                <a href="#about" class="hover:text-white">About</a>
                <a href="#products" class="hover:text-white">Products</a>
                <a href="#contact" class="hover:text-white">Contact</a>
            </div>
        </div>
    </footer>

    <script>
        function switchTab(tabName) {
            const baso4Panel = document.getElementById('baso4-panel');
            const talcPanel = document.getElementById('talc-panel');
            const baso4Btn = document.getElementById('baso4-btn');
            const talcBtn = document.getElementById('talc-btn');

            if (tabName === 'baso4') {
                baso4Panel.classList.remove('hidden');
                talcPanel.classList.add('hidden');
                baso4Btn.className = "px-4 py-2 text-sm rounded font-medium bg-[#c5a059] text-[#0b2c3d] transition-all";
                talcBtn.className = "px-4 py-2 text-sm rounded font-medium text-slate-400 hover:text-white transition-all";
            } else {
                baso4Panel.classList.add('hidden');
                talcPanel.classList.remove('hidden');
                talcBtn.className = "px-4 py-2 text-sm rounded font-medium bg-[#c5a059] text-[#0b2c3d] transition-all";
                baso4Btn.className = "px-4 py-2 text-sm rounded font-medium text-slate-400 hover:text-white transition-all";
            }
        }

        const menuBtn = document.getElementById('mobile-menu-button');
        const mobileMenu = document.getElementById('mobile-menu');
        
        menuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    </script>
</body>
</html>"""

# แสดงผล HTML ในหน้าเว็บ Streamlit
st.components.v1.html(html_code, height=900, scrolling=True)
