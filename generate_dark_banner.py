import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def draw_dark_banner_frame(frame_idx, total_frames, S=2):
    W, H = 1400 * S, 500 * S
    
    # 1. Dark Background (#050816 to #0B1528)
    img = Image.new("RGBA", (W, H), (5, 8, 22, 255))
    draw = ImageDraw.Draw(img)
    
    # Soft background gradient overlay
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    
    # Pulsing glow orbs in background
    phase = (frame_idx / total_frames) * 2 * math.pi
    glow1_r = 250 * S + math.sin(phase) * 20 * S
    glow2_r = 300 * S + math.cos(phase) * 25 * S
    
    # Cyan orb top right
    odraw.ellipse([W - 550*S - glow1_r, -100*S - glow1_r, W - 550*S + glow1_r, -100*S + glow1_r], fill=(0, 240, 255, 25))
    # Purple orb bottom center
    odraw.ellipse([W//2 - glow2_r, H + 50*S - glow2_r, W//2 + glow2_r, H + 50*S + glow2_r], fill=(168, 85, 247, 30))
    # Blue orb top left
    odraw.ellipse([-100*S - glow1_r, -50*S - glow1_r, -100*S + glow1_r, -50*S + glow1_r], fill=(37, 99, 235, 25))
    
    overlay = overlay.filter(ImageFilter.GaussianBlur(30 * S))
    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img)

    # 2. Main Outer Glass Container Card
    c_x, c_y, c_w, c_h = 40 * S, 30 * S, (1400 - 80) * S, (500 - 60) * S
    
    # Container Drop Shadow / Outer Glow
    glow_box = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gbdraw = ImageDraw.Draw(glow_box)
    
    # Cyan/Purple animated border glow
    border_alpha = int(40 + 20 * math.sin(phase))
    gbdraw.rounded_rectangle([c_x - 4*S, c_y - 4*S, c_x + c_w + 4*S, c_y + c_h + 4*S], radius=26*S, fill=(0, 240, 255, border_alpha))
    gbdraw.rounded_rectangle([c_x - 8*S, c_y - 8*S, c_x + c_w + 8*S, c_y + c_h + 8*S], radius=30*S, fill=(168, 85, 247, border_alpha // 2))
    glow_box = glow_box.filter(ImageFilter.GaussianBlur(12 * S))
    img = Image.alpha_composite(img, glow_box)
    draw = ImageDraw.Draw(img)
    
    # Glass Container Body (#0B132B with high opacity)
    draw.rounded_rectangle([c_x, c_y, c_x + c_w, c_y + c_h], radius=24*S, fill=(11, 19, 43, 235), outline=(30, 48, 80, 255), width=2*S)
    
    # Glowing Border Accent Line on top of card
    b_glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    bgdraw = ImageDraw.Draw(b_glow)
    bgdraw.rounded_rectangle([c_x, c_y, c_x + c_w, c_y + c_h], radius=24*S, fill=(0,0,0,0), outline=(0, 240, 255, 180), width=2*S)
    b_glow = b_glow.filter(ImageFilter.GaussianBlur(2 * S))
    img = Image.alpha_composite(img, b_glow)
    draw = ImageDraw.Draw(img)
    
    # Load fonts
    font_dir = "C:\\Windows\\Fonts"
    f_segoeb = os.path.join(font_dir, "segoeuib.ttf")
    f_segoe = os.path.join(font_dir, "segoeui.ttf")
    f_consolab = os.path.join(font_dir, "consolab.ttf")
    
    font_badge = ImageFont.truetype(f_segoeb, 14 * S)
    font_name = ImageFont.truetype(f_segoeb, 52 * S)
    font_title = ImageFont.truetype(f_segoeb, 21 * S)
    font_tagline = ImageFont.truetype(f_segoeb, 18 * S)
    font_subtag = ImageFont.truetype(f_segoe, 15 * S)
    font_pill = ImageFont.truetype(f_segoeb, 12 * S)
    font_code = ImageFont.truetype(f_consolab, 12 * S)
    font_footer = ImageFont.truetype(f_segoeb, 12 * S)
    
    # --- STATUS INDICATOR BADGE ---
    badge_x, badge_y = c_x + 35 * S, c_y + 30 * S
    draw.rounded_rectangle([badge_x, badge_y, badge_x + 340*S, badge_y + 34*S], radius=17*S, fill=(15, 28, 56, 255), outline=(0, 240, 255, 100), width=1*S)
    
    # Pulsing status dot
    dot_glow = int(180 + 75 * math.sin(phase * 2))
    draw.ellipse([badge_x + 14*S, badge_y + 11*S, badge_x + 24*S, badge_y + 21*S], fill=(0, 240, 255, dot_glow))
    draw.text((badge_x + 34*S, badge_y + 7*S), "BUILDING  •  LEARNING  •  INNOVATING", font=font_badge, fill=(148, 163, 184, 255))
    
    # --- EXACT NAME ---
    # DHINESHKUMAR S
    name_x, name_y = c_x + 35 * S, c_y + 80 * S
    # Subtle glowing text shadow for name
    name_glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ngdraw = ImageDraw.Draw(name_glow)
    ngdraw.text((name_x, name_y), "DHINESHKUMAR S", font=font_name, fill=(0, 240, 255, 120))
    name_glow = name_glow.filter(ImageFilter.GaussianBlur(4 * S))
    img = Image.alpha_composite(img, name_glow)
    draw = ImageDraw.Draw(img)
    
    draw.text((name_x, name_y), "DHINESHKUMAR S", font=font_name, fill=(255, 255, 255, 255))
    
    # --- MAIN IDENTITY ---
    draw.text((c_x + 35 * S, c_y + 150 * S), "AI / ML  ×  DATA SCIENCE  ×  FULL STACK", font=font_title, fill=(0, 240, 255, 255))
    
    # --- TAGLINES ---
    # Cyan/Purple Accent Bar
    draw.rounded_rectangle([c_x + 35 * S, c_y + 192 * S, c_x + 75 * S, c_y + 196 * S], radius=2*S, fill=(168, 85, 247, 255))
    draw.text((c_x + 88 * S, c_y + 185 * S), "Turning Ideas Into Working Systems 🚀", font=font_tagline, fill=(241, 245, 249, 255))
    draw.text((c_x + 88 * S, c_y + 213 * S), "Building intelligent solutions for real-world problems.", font=font_subtag, fill=(148, 163, 184, 255))
    
    # --- IDENTITY PILLS ---
    pills = ["Computer Vision", "Data Analytics", "Hackathons", "Real-World Problem Solving"]
    px = c_x + 35 * S
    py = c_y + 252 * S
    for pill in pills:
        bbox = font_pill.getbbox(pill)
        pw = (bbox[2] - bbox[0]) + 24 * S
        ph = 26 * S
        draw.rounded_rectangle([px, py, px + pw, py + ph], radius=13*S, fill=(15, 28, 56, 255), outline=(56, 189, 248, 100), width=1*S)
        draw.text((px + 12*S, py + 4*S), pill, font=font_pill, fill=(56, 189, 248, 255))
        px += pw + 10 * S
        
    # --- RIGHT SIDE: FUTURISTIC AI & DATA WORKSPACE GRAPHIC ---
    ws_x = c_x + 780 * S
    ws_y = c_y + 40 * S
    ws_w = 480 * S
    ws_h = 360 * S
    
    # Dark Glass Panel
    draw.rounded_rectangle([ws_x, ws_y, ws_x + ws_w, ws_y + ws_h], radius=20*S, fill=(6, 11, 25, 240), outline=(0, 240, 255, 80), width=1*S)
    
    # Header bar on glass panel
    draw.rounded_rectangle([ws_x, ws_y, ws_x + ws_w, ws_y + 36*S], radius=20*S, fill=(15, 25, 48, 255))
    draw.rectangle([ws_x, ws_y + 20*S, ws_x + ws_w, ws_y + 36*S], fill=(15, 25, 48, 255))
    # Window buttons
    draw.ellipse([ws_x + 15*S, ws_y + 12*S, ws_x + 25*S, ws_y + 22*S], fill=(239, 68, 68, 255))
    draw.ellipse([ws_x + 32*S, ws_y + 12*S, ws_x + 42*S, ws_y + 22*S], fill=(245, 158, 11, 255))
    draw.ellipse([ws_x + 49*S, ws_y + 12*S, ws_x + 59*S, ws_y + 22*S], fill=(16, 185, 129, 255))
    draw.text((ws_x + 75*S, ws_y + 9*S), "ai_workspace.py — Neural Data Engine", font=ImageFont.truetype(f_segoeb, 11*S), fill=(148, 163, 184, 255))
    
    # Code Content inside Terminal Window
    cursor_char = "█" if (frame_idx % 4 < 2) else " "
    lines = [
        ("from ai.engine import NeuralModel", (56, 189, 248, 255)),
        ("import vision, data_pipeline", (168, 85, 247, 255)),
        ("data = load_stream('real_world')", (74, 222, 128, 255)),
        ("model = NeuralModel(layers=[512, 256])", (244, 114, 182, 255)),
        ("accuracy = model.train(epochs=100)", (250, 204, 21, 255)),
        (f"status: DEPLOYED (98.6% ACC) {cursor_char}", (0, 240, 255, 255))
    ]
    for li, (ltxt, lcol) in enumerate(lines):
        draw.text((ws_x + 20*S, ws_y + 50*S + li * 22*S), ltxt, font=font_code, fill=lcol)
        
    # Animated Neural Network Flow Diagram inside Panel (Bottom area)
    nn_y = ws_y + 220 * S
    nodes = [
        (ws_x + 50*S, nn_y + 50*S, "DATA"),
        (ws_x + 160*S, nn_y + 20*S, "ANALYZE"),
        (ws_x + 160*S, nn_y + 80*S, "MODEL"),
        (ws_x + 270*S, nn_y + 50*S, "PREDICT"),
        (ws_x + 390*S, nn_y + 50*S, "IMPACT")
    ]
    edges = [(0,1), (0,2), (1,3), (2,3), (3,4)]
    
    # Draw connections
    for u, v in edges:
        p1, p2 = nodes[u], nodes[v]
        draw.line([(p1[0], p1[1]), (p2[0], p2[1])], fill=(30, 58, 100, 255), width=2*S)
        
        # Moving pulse along edge
        t = (frame_idx / total_frames + u * 0.2) % 1.0
        pulse_x = p1[0] + (p2[0] - p1[0]) * t
        pulse_y = p1[1] + (p2[1] - p1[1]) * t
        draw.ellipse([pulse_x - 4*S, pulse_y - 4*S, pulse_x + 4*S, pulse_y + 4*S], fill=(0, 240, 255, 255))
        
    # Draw Nodes
    for nx, ny, nlabel in nodes:
        draw.ellipse([nx - 14*S, ny - 14*S, nx + 14*S, ny + 14*S], fill=(15, 28, 56, 255), outline=(0, 240, 255, 200), width=2*S)
        draw.ellipse([nx - 5*S, ny - 5*S, nx + 5*S, ny + 5*S], fill=(168, 85, 247, 255))
        draw.text((nx - 18*S, ny + 16*S), nlabel, font=ImageFont.truetype(f_segoeb, 9*S), fill=(148, 163, 184, 255))

    # --- FOOTER BAR ---
    draw.text((c_x + 35 * S, c_y + c_h - 35 * S), "BUILD  •  LEARN  •  INNOVATE  •  SHIP 🚀", font=font_footer, fill=(148, 163, 184, 255))
    draw.text((c_x + c_w - 230 * S, c_y + c_h - 35 * S), "MAKE IDEAS WORK  ⚡", font=font_footer, fill=(0, 240, 255, 255))

    # Downsample frame to 1400x500 for retina quality
    final_frame = img.resize((1400, 500), Image.Resampling.LANCZOS)
    return final_frame

def build_assets():
    out_dir = r"C:\Users\dines\.gemini\antigravity-ide\scratch\Dhinesh2510-hub\assets"
    os.makedirs(out_dir, exist_ok=True)
    
    total_frames = 12
    frames = []
    print(f"Generating {total_frames} animation frames...")
    
    for i in range(total_frames):
        f = draw_dark_banner_frame(i, total_frames, S=2)
        frames.append(f)
        
    # Save GIF
    gif_path = os.path.join(out_dir, "profile-banner.gif")
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=90,
        loop=0,
        optimize=True
    )
    print(f"Animated GIF saved: {gif_path}")
    
    # Save PNG fallback
    png_path = os.path.join(out_dir, "profile-banner.png")
    frames[0].save(png_path, "PNG", optimize=True)
    print(f"PNG fallback saved: {png_path}")
    
    # Save fallback-banner.png as well
    fb_path = os.path.join(out_dir, "fallback-banner.png")
    frames[0].save(fb_path, "PNG", optimize=True)
    print(f"Fallback banner saved: {fb_path}")

if __name__ == "__main__":
    build_assets()
