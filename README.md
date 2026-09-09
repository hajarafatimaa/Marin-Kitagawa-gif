# 🌸 Marin's Mini GIF Maker 🌸

A sweet and simple Python script that magically stitches your favorite static images into a continuously looping GIF using `imageio`! 🌸 
Just update the file list, run the script, and watch your pictures come to life! ✨

## ✨ What it does
* **Image Stitching:** Reads a list of pictures (like `Image 1.png` through `Image 4.png`) and bundles them together.
* **Animation Magic:** Uses the `imageio.v3` library to seamlessly turn your frames into a moving picture.
* **Perfect Pacing:** Sets a custom delay (currently **350ms**) between frames for a smooth transition.
* **Infinite Loops:** Keeps the fun going forever with the `loop=0` setting!

## 🛠️ How to use it
1. Make sure you have the required library installed by running `pip install imageio`.
2. Drop the images you want to animate into the same folder as the script.
3. Open `Marin.py` and update the `filenames` list with your own image names.
4. Run the script, and your newly minted `Kitagawa.gif` will pop up in your folder!
