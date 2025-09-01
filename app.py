from flask import Flask, render_template, url_for, redirect
import os

app = Flask(__name__)

IMAGE_FOLDER = os.path.join('static', 'images')

@app.route('/')
def index():
    images = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    wallpapers = [{"id": i+1, "image": img} for i, img in enumerate(images)]
    return render_template("index.html", wallpapers=wallpapers)

@app.route('/wallpaper/<int:wallpaper_id>')
def wallpaper_detail(wallpaper_id):
    images = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    wallpapers = [{"id": i+1, "image": img} for i, img in enumerate(images)]
    wallpaper = next((w for w in wallpapers if w["id"] == wallpaper_id), None)
    if wallpaper:
        return render_template("wallpaper.html", wallpaper=wallpaper)
    return "Wallpaper not found", 404


if __name__ == '__main__':
    app.run(debug=True)
