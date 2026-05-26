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
                        <span class="font-serif text
