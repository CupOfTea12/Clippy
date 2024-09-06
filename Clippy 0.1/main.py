import os
from PIL import ImageGrab, Image, ImageTk
import tkinter as tk
from tkinter import filedialog, Label, Frame, ttk
from tkinterdnd2 import TkinterDnD, DND_FILES  # Import TkinterDnD for drag-and-drop functionality

# Global variables for light and dark themes
light_theme = {"bg": "#f4f4f4", "fg": "#000000", "button": "#e1e1e1", "label": "#f4f4f4", "image_bg": "#ffffff"}
dark_theme = {"bg": "#2b2b2b", "fg": "#ffffff", "button": "#444444", "label": "#2b2b2b", "image_bg": "#3c3c3c"}
current_theme = light_theme  # Default theme

# Function to apply theme
def apply_theme(theme):
    root.configure(bg=theme["bg"])
    image_frame.configure(bg=theme["image_bg"], bd=2, relief="solid")
    controls_frame.configure(bg=theme["bg"])
    img_label.configure(bg=theme["image_bg"])
    format_label.configure(bg=theme["bg"], fg=theme["fg"])
    resolution_label.configure(bg=theme["bg"], fg=theme["fg"])
    dark_mode_button.configure(bg=theme["button"], fg=theme["fg"])

# Function to toggle between light and dark mode
def toggle_dark_mode():
    global current_theme
    current_theme = dark_theme if current_theme == light_theme else light_theme
    apply_theme(current_theme)

# Function to grab the image from clipboard
def grab_image_from_clipboard():
    try:
        image = ImageGrab.grabclipboard()
        if isinstance(image, Image.Image):
            return image
        else:
            print("No image found in clipboard.")
            return None
    except Exception as e:
        print(f"Error grabbing image from clipboard: {e}")
        return None

# Function to display the image in the GUI and update resolution
def display_image(image):
    global img_display
    img_display = ImageTk.PhotoImage(image)  # Convert to Tkinter-compatible image
    img_label.config(image=img_display)  # Update the label with the image
    resolution_label.config(text=f"Resolution: {image.width} x {image.height}")

# Function to save the image
def save_image():
    if img_display:
        selected_format = format_var.get()
        file_ext = selected_format.lower()
        file_path = filedialog.asksaveasfilename(
            defaultextension=f".{file_ext}",
            filetypes=[(f"{selected_format} files", f"*.{file_ext}"), ("All files", "*.*")]
        )
        if file_path:
            img_pil.save(file_path, format=selected_format)
            print(f"Image saved as {selected_format} at {file_path}")
        else:
            print("Save operation failed")
    else:
        print("No image to save")

# Function to handle the paste event (Ctrl+V)
def paste_image(event=None):
    global img_pil
    img_pil = grab_image_from_clipboard()  # Grab image from clipboard
    if img_pil:
        img_resized = img_pil.resize((400, 300))  # Resize image for display
        display_image(img_resized)

# Function to rotate the image
def rotate_image():
    global img_pil
    if img_pil:
        img_pil = img_pil.rotate(90, expand=True)  # Rotate the image 90 degrees
        display_image(img_pil.resize((400, 300)))

# Function to zoom in the image
def zoom_in():
    global img_pil
    if img_pil:
        img_pil = img_pil.resize((int(img_pil.width * 1.2), int(img_pil.height * 1.2)))  # Zoom by 20%
        display_image(img_pil)

# Function to zoom out the image
def zoom_out():
    global img_pil
    if img_pil:
        img_pil = img_pil.resize((int(img_pil.width * 0.8), int(img_pil.height * 0.8)))  # Zoom out by 20%
        display_image(img_pil)

# Function to resize the image to custom dimensions
def resize_image():
    global img_pil
    if img_pil:
        new_width = int(width_entry.get())
        new_height = int(height_entry.get())
        img_pil = img_pil.resize((new_width, new_height))
        display_image(img_pil)

# Auto-check clipboard for new images
def auto_check_clipboard():
    img = grab_image_from_clipboard()
    if img:
        display_image(img.resize((400, 300)))  # Resize for display
        print("New image detected from clipboard")
    root.after(5000, auto_check_clipboard)  # Check every 5 seconds

# Drag and Drop Support
def drop_image(event):
    try:
        file_path = root.tk.splitlist(event.data)[0]  # Get file path from drag and drop
        global img_pil
        img_pil = Image.open(file_path)
        display_image(img_pil.resize((400, 300)))  # Resize for display
    except Exception as e:
        print(f"Failed to open image: {e}")

# Create the main TkinterDnD window
root = TkinterDnD.Tk()  # Initialize with TkinterDnD for drag-and-drop functionality
root.title("Clippy - Image Clipboard Tool")
root.geometry("600x600")
root.configure(bg=light_theme["bg"])  # Light background color

# Create the main container frame
main_frame = Frame(root, bg=light_theme["bg"])
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create a frame for the image display
image_frame = Frame(main_frame, bg=light_theme["image_bg"], bd=2, relief="solid")
image_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create and configure the image label to display the image
img_label = Label(image_frame, bg=light_theme["image_bg"])
img_label.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a label to show image resolution
resolution_label = Label(main_frame, text="Resolution: N/A", bg=light_theme["bg"], fg=light_theme["fg"])
resolution_label.pack(pady=5)

# Create a frame for the control buttons
controls_frame = Frame(main_frame, bg=light_theme["bg"])
controls_frame.pack(fill=tk.X, padx=10, pady=10)

# Add buttons and dropdown menu
save_button = ttk.Button(controls_frame, text="Save Image", command=save_image)
save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

rotate_button = ttk.Button(controls_frame, text="Rotate Image", command=rotate_image)
rotate_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

zoom_in_button = ttk.Button(controls_frame, text="Zoom In", command=zoom_in)
zoom_in_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

zoom_out_button = ttk.Button(controls_frame, text="Zoom Out", command=zoom_out)
zoom_out_button.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

format_label = Label(controls_frame,    text="Format:", bg=light_theme["bg"], fg=light_theme["fg"])
format_label.grid(row=0, column=4, padx=5, pady=5)

format_var = tk.StringVar(root)
format_var.set("PNG")  # Default value
format_menu = ttk.OptionMenu(controls_frame, format_var, "PNG", "JPEG", "BMP")
format_menu.grid(row=0, column=5, padx=5, pady=5)

# Add fields to input custom dimensions
width_entry = ttk.Entry(controls_frame, width=5)
width_entry.grid(row=1, column=0, padx=5, pady=5)
width_entry.insert(0, "400")

height_entry = ttk.Entry(controls_frame, width=5)
height_entry.grid(row=1, column=1, padx=5, pady=5)
height_entry.insert(0, "300")

resize_button = ttk.Button(controls_frame, text="Resize Image", command=resize_image)
resize_button.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

# Add a button to toggle dark mode
dark_mode_button = tk.Button(controls_frame, text="Toggle Dark Mode", command=toggle_dark_mode, bg=light_theme["button"],
                             fg=light_theme["fg"])
dark_mode_button.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

# Bind the paste event (Ctrl+V) to the paste_image function
root.bind("<Control-v>", paste_image)

# Enable drag and drop for the main window
root.drop_target_register(DND_FILES)  # Register the window for file drops
root.dnd_bind('<<Drop>>', drop_image)  # Bind the drop event to the drop_image function

# Start auto-checking clipboard
root.after(5000, auto_check_clipboard)  # Check clipboard every 5 seconds

# Apply the light theme by default
apply_theme(light_theme)

# Run the Tkinter event loop
root.mainloop()

