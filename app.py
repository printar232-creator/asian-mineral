import streamlit as st
import base64

# ตั้งค่าหน้าเพจของ Streamlit ให้เป็นแบบกว้าง (Wide Layout) และตั้งชื่อ Title
st.set_page_config(
    page_title="Asia Mineral Supply (AMS) - Premium Mineral Supplier",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ข้อมูลโค้ด HTML5 + Tailwind CSS + JavaScript ทั้งหมดที่ถูกเข้ารหัส Base64 ไว้เพื่อป้องกัน SyntaxError
raw_html = """
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
        body { font-family: 'Plus Jakarta Sans', 'Inter', sans-serif; background-color: #f8fafc; color: #1e293b; }
        .font-serif { font-family: 'Playfair Display', serif; }
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
                    <button id="mobile-menu-button" class="text-slate-300 hover:text-white focus:outline-none p-2">
                        <svg class="h-6 w-6" fill="none" viewBox="0
