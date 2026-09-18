import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_banner():
    # Scale factor 2 for retina anti-aliased sharpness (2800x1000 -> 1400x500)
    S = 2
    W, H = 1400 * S, 500 * S
    
    img = Image.new("RGBA", (W, H), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # 1. Background Gradient (White to very light soft blue)
    for y in range(H):
        r = int(255 - (y / H) * 12)
        g = int(255 - (y / H) * 8)
        b = int(255 - (y / H) * 3)
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))
        
    # Subtle radial highlight at top-left & bottom-right
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    
    # Top right soft decorative circle
    odraw.ellipse([W - 600*S, -100*S, W + 100*S, 450*S], fill=(219, 234, 254, 70))
    # Bottom right soft circle
    odraw.ellipse([W - 900*S, H - 300*S, W - 100*S, H + 300*S], fill=(239, 246, 255, 120))
    # Bottom left soft circle
    odraw.ellipse([-150*S, H - 250*S, 350*S, H + 250*S], fill=(224, 236, 254, 90))
    
    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img)
    
    # Load fonts
    font_dir = "C:\\Windows\\Fonts"
    f_segoe = os.path.join(font_dir, "segoeui.ttf")
    f_segoeb = os.path.join(font_dir, "segoeuib.ttf")
    f_segoez = os.path.join(font_dir, "segoeuiz.ttf") # Semibold/Bold
    f_arialb = os.path.join(font_dir, "arialbd.ttf")
    f_consolab = os.path.join(font_dir, "consolab.ttf")
    
    font_badge = ImageFont.truetype(f_segoeb, 15 * S)
    font_name = ImageFont.truetype(f_segoeb, 54 * S)
    font_title = ImageFont.truetype(f_segoeb, 21 * S)
    font_tagline = ImageFont.truetype(f_segoeb, 19 * S)
    font_subtag = ImageFont.truetype(f_segoe, 15 * S)
    font_pill = ImageFont.truetype(f_segoeb, 13 * S)
    font_card_title = ImageFont.truetype(f_segoeb, 14 * S)
    font_card_sub = ImageFont.truetype(f_segoe, 11 * S)
    font_code = ImageFont.truetype(f_consolab, 12 * S)
    font_footer = ImageFont.truetype(f_segoeb, 12 * S)
    
    # --- TOP STATUS BADGE ---
    # Shadow box
    badge_x, badge_y, badge_w, badge_h = 60 * S, 35 * S, 330 * S, 36 * S
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow)
    sdraw.rounded_rectangle([badge_x, badge_y + 4*S, badge_x + badge_w, badge_y + badge_h + 4*S], radius=18*S, fill=(30, 58, 138, 15))
    shadow = shadow.filter(ImageFilter.GaussianBlur(6*S))
    img = Image.alpha_composite(img, shadow)
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + badge_h], radius=18*S, fill=(255, 255, 255, 255), outline=(219, 234, 254, 255), width=1*S)
    draw.ellipse([badge_x + 16*S, badge_y + 13*S, badge_x + 26*S, badge_y + 23*S], fill=(16, 185, 129, 255))
    draw.text((badge_x + 36*S, badge_y + 9*S), "ASPIRING  |  INNOVATING  |  BUILDING", font=font_badge, fill=(71, 85, 105, 255))
    
    # --- MAIN NAME ---
    # EXACTLY: DHINESHKUMAR S
    draw.text((60 * S, 90 * S), "DHINESHKUMAR S", font=font_name, fill=(15, 23, 42, 255))
    
    # --- MAIN TITLE ---
    draw.text((60 * S, 160 * S), "AI / ML  ×  DATA SCIENCE  ×  FULL STACK", font=font_title, fill=(37, 99, 235, 255))
    
    # --- TAGLINES ---
    # Blue accent bar
    draw.rounded_rectangle([60 * S, 202 * S, 100 * S, 206 * S], radius=2*S, fill=(37, 99, 235, 255))
    draw.text((115 * S, 195 * S), "Turning Ideas Into Working Systems", font=font_tagline, fill=(30, 41, 59, 255))
    draw.text((115 * S, 224 * S), "Building intelligent solutions for real-world problems", font=font_subtag, fill=(100, 116, 139, 255))
    
    # --- SECONDARY IDENTITY PILLS ---
    pills = ["Computer Vision", "Data Intelligence", "Hackathons"]
    px = 60 * S
    py = 260 * S
    for pill in pills:
        bbox = font_pill.getbbox(pill)
        pw = (bbox[2] - bbox[0]) + 28 * S
        ph = 28 * S
        draw.rounded_rectangle([px, py, px + pw, py + ph], radius=14*S, fill=(239, 246, 255, 255), outline=(191, 219, 254, 255), width=1*S)
        draw.text((px + 14*S, py + 5*S), pill, font=font_pill, fill=(29, 78, 216, 255))
        px += pw + 12 * S
        
    # --- 5 CORE FIELD CARDS ---
    cards = [
        {"title": "AI / ML", "sub": "Intelligent Systems", "icon": "ai", "bg": (255,255,255), "accent": (37, 99, 235)},
        {"title": "Data Science", "sub": "Data to Insights", "icon": "ds", "bg": (255,255,255), "accent": (2, 132, 199)},
        {"title": "Full Stack", "sub": "End-to-End Apps", "icon": "fs", "bg": (255,255,255), "accent": (79, 70, 229)},
        {"title": "Computer Vision", "sub": "Visual Intelligence", "icon": "cv", "bg": (255,255,255), "accent": (14, 165, 233)},
        {"title": "Hackathons", "sub": "Rapid Innovation", "icon": "hk", "bg": (255,255,255), "accent": (217, 119, 6)}
    ]
    
    card_y = 312 * S
    card_w = 168 * S
    card_h = 105 * S
    card_gap = 14 * S
    start_x = 60 * S
    
    for i, c in enumerate(cards):
        cx = start_x + i * (card_w + card_gap)
        
        # Shadow
        cshadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        csdraw = ImageDraw.Draw(cshadow)
        csdraw.rounded_rectangle([cx, card_y + 4*S, cx + card_w, card_y + card_h + 4*S], radius=16*S, fill=(15, 23, 42, 12))
        cshadow = cshadow.filter(ImageFilter.GaussianBlur(5*S))
        img = Image.alpha_composite(img, cshadow)
        draw = ImageDraw.Draw(img)
        
        # Card body
        draw.rounded_rectangle([cx, card_y, cx + card_w, card_y + card_h], radius=16*S, fill=(255, 255, 255, 255), outline=(226, 232, 240, 255), width=1*S)
        
        # Icon Circle
        ic_x, ic_y = cx + 22 * S, card_y + 24 * S
        draw.ellipse([ic_x - 16*S, ic_y - 16*S, ic_x + 16*S, ic_y + 16*S], fill=(239, 246, 255, 255))
        
        acc = c["accent"]
        # Draw vector icon inside
        if c["icon"] == "ai":
            # Nodes & Connections
            draw.line([(ic_x - 7*S, ic_y), (ic_x + 7*S, ic_y)], fill=acc, width=2*S)
            draw.line([(ic_x, ic_y - 7*S), (ic_x, ic_y + 7*S)], fill=acc, width=2*S)
            draw.ellipse([ic_x - 4*S, ic_y - 4*S, ic_x + 4*S, ic_y + 4*S], fill=acc)
            draw.ellipse([ic_x - 9*S, ic_y - 2*S, ic_x - 5*S, ic_y + 2*S], fill=acc)
            draw.ellipse([ic_x + 5*S, ic_y - 2*S, ic_x + 9*S, ic_y + 2*S], fill=acc)
        elif c["icon"] == "ds":
            # Bar Chart
            draw.rectangle([ic_x - 8*S, ic_y + 2*S, ic_x - 4*S, ic_y + 8*S], fill=acc)
            draw.rectangle([ic_x - 2*S, ic_y - 3*S, ic_x + 2*S, ic_y + 8*S], fill=acc)
            draw.rectangle([ic_x + 4*S, ic_y - 8*S, ic_x + 8*S, ic_y + 8*S], fill=acc)
        elif c["icon"] == "fs":
            # Code </>
            draw.text((ic_x - 12*S, ic_y - 11*S), "</>", font=ImageFont.truetype(f_segoeb, 13*S), fill=acc)
        elif c["icon"] == "cv":
            # Eye / Vision
            draw.ellipse([ic_x - 10*S, ic_y - 6*S, ic_x + 10*S, ic_y + 6*S], outline=acc, width=2*S)
            draw.ellipse([ic_x - 4*S, ic_y - 4*S, ic_x + 4*S, ic_y + 4*S], fill=acc)
        elif c["icon"] == "hk":
            # Lightning / Flame
            draw.polygon([(ic_x, ic_y - 9*S), (ic_x - 6*S, ic_y + 1*S), (ic_x - 1*S, ic_y + 1*S), (ic_x - 3*S, ic_y + 9*S), (ic_x + 6*S, ic_y - 1*S), (ic_x + 1*S, ic_y - 1*S)], fill=acc)
            
        # Card Text
        draw.text((cx + 18*S, card_y + 50*S), c["title"], font=font_card_title, fill=(15, 23, 42, 255))
        draw.text((cx + 18*S, card_y + 74*S), c["sub"], font=font_card_sub, fill=(100, 116, 139, 255))

    # --- RIGHT SIDE: WORKSPACE (DESK, LAPTOP, BOOKS, PLANT) ---
    ws_x = 980 * S
    ws_y = 70 * S
    ws_w = 370 * S
    ws_h = 360 * S
    
    # Workspace background card container
    wshadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    wsdraw = ImageDraw.Draw(wshadow)
    wsdraw.rounded_rectangle([ws_x, ws_y, ws_x + ws_w, ws_y + ws_h], radius=24*S, fill=(15, 23, 42, 15))
    wshadow = wshadow.filter(ImageFilter.GaussianBlur(8*S))
    img = Image.alpha_composite(img, wshadow)
    draw = ImageDraw.Draw(img)
    
    # Container body with glassmorphism / soft gradient
    draw.rounded_rectangle([ws_x, ws_y, ws_x + ws_w, ws_y + ws_h], radius=24*S, fill=(255, 255, 255, 235), outline=(226, 232, 240, 255), width=1*S)
    
    # Desk Surface Line
    desk_y = ws_y + 270 * S
    draw.line([(ws_x + 20*S, desk_y), (ws_x + ws_w - 20*S, desk_y)], fill=(203, 213, 225, 255), width=2*S)
    
    # 1. LAPTOP (Center right of workspace)
    lap_w = 175 * S
    lap_h = 115 * S
    lap_x = ws_x + 85 * S
    lap_y = desk_y - lap_h - 10 * S
    
    # Laptop Screen Lid (Dark Blue Slate frame)
    draw.rounded_rectangle([lap_x, lap_y, lap_x + lap_w, lap_y + lap_h], radius=8*S, fill=(15, 23, 42, 255))
    # Screen Display Inner
    scr_margin = 6 * S
    draw.rounded_rectangle([lap_x + scr_margin, lap_y + scr_margin, lap_x + lap_w - scr_margin, lap_y + lap_h - scr_margin], radius=5*S, fill=(30, 41, 59, 255))
    
    # Code & Visuals on Laptop Screen
    code_lines = [
        ("import tensorflow as tf", (56, 189, 248, 255)),
        ("model = tf.keras.Sequential()", (244, 114, 182, 255)),
        ("data = pd.read_csv('argo.csv')", (74, 222, 128, 255)),
        ("accuracy = 0.984 # Trained", (250, 204, 21, 255)),
        ("Deploying full-stack API...", (226, 232, 240, 255))
    ]
    for ly, (line_txt, col) in enumerate(code_lines):
        draw.text((lap_x + 14*S, lap_y + 14*S + ly * 18*S), line_txt, font=font_code, fill=col)
        
    # Laptop Base / Keyboard
    base_w = 205 * S
    base_h = 10 * S
    base_x = lap_x - 15 * S
    base_y = desk_y - base_h
    draw.rounded_rectangle([base_x, base_y, base_x + base_w, base_y + base_h], radius=4*S, fill=(148, 163, 184, 255))
    draw.rounded_rectangle([base_x + 80*S, base_y + 2*S, base_x + 125*S, base_y + 5*S], radius=2*S, fill=(203, 213, 225, 255))
    
    # 2. BOOKS STACK (Left of laptop)
    book_x = ws_x + 25 * S
    book_y = desk_y
    book_colors = [(37, 99, 235), (16, 185, 129), (217, 119, 6)]
    book_titles = ["AI & ML", "DATA SCI", "PYTHON"]
    
    for bi, (bcol, btitle) in enumerate(zip(book_colors, book_titles)):
        bw = 48 * S
        bh = 13 * S
        by = book_y - (bi + 1) * bh
        draw.rounded_rectangle([book_x, by, book_x + bw, by + bh - 1*S], radius=2*S, fill=bcol)
        draw.rectangle([book_x + 2*S, by + 1*S, book_x + 6*S, by + bh - 2*S], fill=(255, 255, 255, 180))
        draw.text((book_x + 9*S, by + 1*S), btitle, font=ImageFont.truetype(f_segoeb, 7*S), fill=(255, 255, 255, 255))
        
    # Notebook / Pen on top of books
    nb_y = book_y - 3 * 13*S - 5*S
    draw.rounded_rectangle([book_x + 2*S, nb_y, book_x + 42*S, nb_y + 5*S], radius=1*S, fill=(241, 245, 249, 255), outline=(203, 213, 225, 255))
    # Pen
    draw.line([(book_x + 30*S, nb_y - 2*S), (book_x + 45*S, nb_y + 3*S)], fill=(30, 41, 59, 255), width=2*S)

    # 3. POTTED PLANT (Right of laptop)
    plant_x = ws_x + 305 * S
    plant_y = desk_y
    # White ceramic pot
    pot_w = 32 * S
    pot_h = 35 * S
    draw.polygon([
        (plant_x, plant_y - pot_h),
        (plant_x + pot_w, plant_y - pot_h),
        (plant_x + pot_w - 4*S, plant_y),
        (plant_x + 4*S, plant_y)
    ], fill=(248, 250, 252, 255), outline=(203, 213, 225, 255))
    
    # Plant Leaves (Vibrant natural greens)
    leaf_center = (plant_x + 16*S, plant_y - pot_h)
    draw.ellipse([leaf_center[0] - 20*S, leaf_center[1] - 30*S, leaf_center[0] + 5*S, leaf_center[1]], fill=(16, 185, 129, 255))
    draw.ellipse([leaf_center[0] - 5*S, leaf_center[1] - 35*S, leaf_center[0] + 20*S, leaf_center[1] - 5*S], fill=(5, 150, 105, 255))
    draw.ellipse([leaf_center[0] - 12*S, leaf_center[1] - 40*S, leaf_center[0] + 12*S, leaf_center[1] - 15*S], fill=(52, 211, 153, 255))

    # Tech Floating Badges above workspace
    draw.rounded_rectangle([ws_x + 30*S, ws_y + 25*S, ws_x + 130*S, ws_y + 55*S], radius=15*S, fill=(239, 246, 255, 255), outline=(191, 219, 254, 255), width=1*S)
    draw.text((ws_x + 42*S, ws_y + 32*S), "⚡ Smart AI", font=ImageFont.truetype(f_segoeb, 11*S), fill=(29, 78, 216, 255))
    
    draw.rounded_rectangle([ws_x + 230*S, ws_y + 25*S, ws_x + 340*S, ws_y + 55*S], radius=15*S, fill=(240, 253, 244, 255), outline=(187, 247, 208, 255), width=1*S)
    draw.text((ws_x + 242*S, ws_y + 32*S), "📊 Data Flow", font=ImageFont.truetype(f_segoeb, 11*S), fill=(21, 128, 61, 255))

    # Workspace Title
    draw.text((ws_x + 30*S, ws_y + 310*S), "DEVELOPER WORKSPACE", font=ImageFont.truetype(f_segoeb, 12*S), fill=(15, 23, 42, 255))
    draw.text((ws_x + 30*S, ws_y + 330*S), "Clean code • Real data • Scalable architecture", font=ImageFont.truetype(f_segoe, 10*S), fill=(100, 116, 139, 255))

    # --- FOOTER BAR ---
    draw.text((60 * S, 445 * S), "INDIA  |  STUDENT DEVELOPER  |  REAL-WORLD IMPACT", font=font_footer, fill=(100, 116, 139, 255))
    draw.text((W - 370 * S, 445 * S), "MAKE IDEAS WORK  🚀", font=font_footer, fill=(37, 99, 235, 255))

    # Downsample with LANCZOS to 1400x500 for crisp anti-aliasing
    final_banner = img.resize((1400, 500), Image.Resampling.LANCZOS)
    
    out_dir = r"C:\Users\dines\.gemini\antigravity-ide\scratch\Dhinesh2510-hub\assets"
    os.makedirs(out_dir, exist_ok=True)
    banner_path = os.path.join(out_dir, "banner.png")
    final_banner.save(banner_path, "PNG", optimize=True)
    print(f"Banner successfully created at: {banner_path}")

if __name__ == "__main__":
    create_banner()
