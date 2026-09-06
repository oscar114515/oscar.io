# Python script to update about-cards with background images
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 更新 CSS
old_css = '''        .about-card {
            background: #ffffff;
            border-radius: 20px;
            padding: 30px 24px;
            text-align: center;
            border: 1px solid #eef2f7;
            box-shadow: 0 4px 16px rgba(0,0,0,0.04);
            transition: all 0.25s ease;
        }'''

new_css = '''        .about-card {
            background: #ffffff;
            background-size: contain;
            background-position: center;
            background-repeat: no-repeat;
            border-radius: 20px;
            padding: 30px 24px;
            text-align: center;
            border: 1px solid #eef2f7;
            box-shadow: 0 4px 16px rgba(0,0,0,0.04);
            transition: all 0.25s ease;
        }'''

if old_css in content:
    content = content.replace(old_css, new_css)
    print('CSS updated')
else:
    print('CSS not found')

# 2. 为第一张卡片添加背景图片 (Minecraft)
old_card1 = '<div class="about-card minecraft">'
new_card1 = '<div class="about-card minecraft" style="background-image: url(https://i.mcmod.cn/class/cover/20210723/1626978462_14273_psym.jpg@480x300.jpg);">'
if old_card1 in content:
    content = content.replace(old_card1, new_card1)
    print('Card 1 updated')

# 3. 为第二张卡片添加背景图片 (Android)
old_card2 = '''            <div class="about-card">
                <div class="card-icon">💻</div>
                <div class="card-title">技術興趣</div>'''
new_card2 = '''            <div class="about-card" style="background-image: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbfqtcaKrMZ6Bk5fNmjrhFCF_C6C-HVThGHOcVgPg-aA&s=10);">
                <div class="card-icon">💻</div>
                <div class="card-title">技術興趣</div>'''
if old_card2 in content:
    content = content.replace(old_card2, new_card2)
    print('Card 2 updated')

# 4. 为第三张卡片添加背景图片 (Music)
old_card3 = '<div class="about-card for">'
new_card3 = '<div class="about-card" style="background-image: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-WrmU6fdEq4-pvo0SGU-9vE1VVnttmEhTbrk41pGC9A&s=10);">'
if old_card3 in content:
    content = content.replace(old_card3, new_card3)
    print('Card 3 updated')

# 5. 为第四张卡片添加背景图片 (Project)
old_card4 = '''            <div class="about-card">
                <div class="card-icon">📁</div>
                <div class="card-title">專案經驗</div>'''
new_card4 = '''            <div class="about-card" style="background-image: url(https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=400&h=300&fit=crop);">
                <div class="card-icon">📁</div>
                <div class="card-title">專案經驗</div>'''
if old_card4 in content:
    content = content.replace(old_card4, new_card4)
    print('Card 4 updated')

# 6. 为第五张卡片添加背景图片 (Social)
old_card5 = '''            <div class="about-card">
                <div class="card-icon">👥</div>
                <div class="card-title">社群身份</div>'''
new_card5 = '''            <div class="about-card" style="background-image: url(https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=400&h=300&fit=crop);">
                <div class="card-icon">👥</div>
                <div class="card-title">社群身份</div>'''
if old_card5 in content:
    content = content.replace(old_card5, new_card5)
    print('Card 5 updated')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
