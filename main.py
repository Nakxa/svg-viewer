import tkinter as tk
from tksvg import SvgImage
import io
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import ttk, colorchooser
from tksvg import SvgImage
import io
import xml.etree.ElementTree as ET
import math
import tkinter as tk
from tkinter import ttk, colorchooser, messagebox
from tksvg import SvgImage
import xml.etree.ElementTree as ET
import math
from tkinter import filedialog
import re


# Function to generate the SVG icons
def generate_ai_fill_book(color, width, height):
    svg = ET.Element("svg", {"fill": color,"viewBox": "0 0 1024 1024", "width": width, "height": height})
    path = ET.SubElement(svg, "path", {
        "d": "M832 64H192c-17.7 0-32 14.3-32 32v832c0 17.7 14.3 32 32 32h640c17.7 0 32-14.3 32-32V96c0-17.7-14.3-32-32-32zM668 345.9L621.5 312 572 347.4V124h96v221.9z"
    })
    return ET.tostring(svg, encoding="unicode", method="xml")


def generate_ai_fill_box_plot(color, width, height):
    svg = ET.Element("svg", {"fill": color,"viewBox": "0 0 1024 1024", "width": width, "height": height})
    path = ET.SubElement(svg, "path", {
        "d": "M952 224h-52c-4.4 0-8 3.6-8 8v248h-92V304c0-4.4-3.6-8-8-8H448v432h344c4.4 0 8-3.6 8-8V548h92v244c0 4.4 3.6 8 8 8h52c4.4 0 8-3.6 8-8V232c0-4.4-3.6-8-8-8zm-728 80v176h-92V232c0-4.4-3.6-8-8-8H72c-4.4 0-8 3.6-8 8v560c0 4.4 3.6 8 8 8h52c4.4 0 8-3.6 8-8V548h92v172c0 4.4 3.6 8 8 8h152V296H232c-4.4 0-8 3.6-8 8z"
    })
    return ET.tostring(svg, encoding="unicode", method="xml")


def generate_ai_fill_bug(color, width, height):
    svg = ET.Element("svg", {"fill": color,"viewBox": "0 0 1024 1024", "width": width, "height": height})
    path1 = ET.SubElement(svg, "path", {
        "d": "M304 280h416c4.4 0 8-3.6 8-8 0-40-8.8-76.7-25.9-108.1-17.2-31.5-42.5-56.8-74-74C596.7 72.8 560 64 520 64h-16c-40 0-76.7 8.8-108.1 25.9-31.5 17.2-56.8 42.5-74 74C304.8 195.3 296 232 296 272c0 4.4 3.6 8 8 8z"
    })
    path2 = ET.SubElement(svg, "path", {
        "d": "M940 512H792V412c76.8 0 139-62.2 139-139 0-4.4-3.6-8-8-8h-60c-4.4 0-8 3.6-8 8 0 34.8-28.2 63-63 63H232c-34.8 0-63-28.2-63-63 0-4.4-3.6-8-8-8h-60c-4.4 0-8 3.6-8 8 0 76.8 62.2 139 139 139v100H84c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h148v96c0 6.5.2 13 .7 19.3C164.1 728.6 116 796.7 116 876c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8 0-44.2 23.9-82.9 59.6-103.7 6 17.2 13.6 33.6 22.7 49 24.3 41.5 59 76.2 100.5 100.5 28.9 16.9 61 28.8 95.3 34.5 4.4 0 8-3.6 8-8V484c0-4.4 3.6-8 8-8h60c4.4 0 8 3.6 8 8v464.2c0 4.4 3.6 8 8 8 34.3-5.7 66.4-17.6 95.3-34.5 41.5-24.3 76.2-59 100.5-100.5 9.1-15.5 16.7-31.9 22.7-49C812.1 793.1 836 831.8 836 876c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8 0-79.3-48.1-147.4-116.7-176.7.4-6.4.7-12.8.7-19.3v-96h148c4.4 0 8-3.6 8-8v-56c0-4.4-3.6-8-8-8z"
    })
    return ET.tostring(svg, encoding="unicode", method="xml")


def generate_bs_android2(color, width, height):
    svg = ET.Element("svg", {"fill": color,"viewBox": "0 0 16 16", "width": width, "height": height})
    path = ET.SubElement(svg, "path", {
        "d": "M1.226 10.88H0l2.056-6.26h1.42l2.047 6.26h-1.29l-.48-1.61H1.707l-.48 1.61ZM2.76 5.818h-.054l-.75 2.532H3.51zm3.217 5.062V4.62h2.56c1.09 0 1.808.582 1.808 1.54 0 .762-.444 1.22-1.05 1.372v.055c.736.074 1.365.587 1.365 1.528 0 1.119-.89 1.766-2.133 1.766zM7.18 5.55v1.675h.8c.812 0 1.171-.308 1.171-.853 0-.51-.328-.822-.898-.822zm0 2.537V9.95h.903c.951 0 1.342-.312 1.342-.909 0-.591-.382-.954-1.095-.954zm5.089-.711v.775c0 1.156.49 1.803 1.347 1.803.705 0 1.163-.454 1.212-1.096H16v.12C15.942 10.173 14.95 11 13.607 11c-1.648 0-2.573-1.073-2.573-2.849v-.78c0-1.775.934-2.871 2.573-2.871 1.347 0 2.34.849 2.393 2.087v.115h-1.172c-.05-.665-.516-1.156-1.212-1.156-.849 0-1.347.67-1.347 1.83"
    })
    return ET.tostring(svg, encoding="unicode", method="xml")




class SVGViewer(tk.Tk):
    def __init__(self):
        super().__init__()


        self.title("Advanced SVG Icons Viewer")
        self.geometry("1400x800")
        self.config(bg="#f4f4f9")


        # Current settings dictionary
        self.current_settings = {
            'fill_color': '#fff000',
            'stroke_color': '#000000',
            'stroke_width': 0,
            'width': 25,
            'height': 25,
            'rotation': 0,
            'opacity': 1.0,
            'scale_x': 1.0,
            'scale_y': 1.0,
            'blur': 0,
            'brightness': 100,
            'contrast': 100,
            'skew_x': 0,
            'skew_y': 0,
            'animation': 'none',
            'animation_duration': 2,
            'shadow_offset': 0,
            'shadow_blur': 0,
            'shadow_color': '#000000',
            'gradient_start': '#ffffff',
            'gradient_end': '#000000',
            'gradient_type': 'none'
        }


        # Create main frames
        self.create_layout()
        self.create_sidebar()
        self.create_control_panel()
       
        # Initialize first SVG
        self.current_svg_generator = generate_ai_fill_book
        self.current_title = "Book Icon"
        self.update_svg()


    def create_layout(self):
        # Create a sidebar frame
        self.sidebar = tk.Frame(self, bg="#333", width=200)
        self.sidebar.pack(side="left", fill="y")


        # Create a main content frame
        self.main_content = tk.Frame(self, bg="#fff")
        self.main_content.pack(side="left", fill="both", expand=True)


        # Create a scrollable control panel frame
        self.control_panel_container = tk.Frame(self, bg="#eee", width=300)
        self.control_panel_container.pack(side="right", fill="y")


        # Add canvas and scrollbar for control panel
        self.canvas = tk.Canvas(self.control_panel_container, bg="#eee", width=280)
        self.scrollbar = ttk.Scrollbar(self.control_panel_container, orient="vertical", command=self.canvas.yview)
        self.control_panel = tk.Frame(self.canvas, bg="#eee")


        # Configure canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")


        # Create window in canvas for control panel
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.control_panel, anchor="nw")
        self.control_panel.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        # Add this after creating the sidebar
        import_button = ttk.Button(self.sidebar, text="Import SVG",
                                command=self.import_svg)
        import_button.pack(side="bottom", pady=10)


    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


    def on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_frame, width=event.width)


    def create_control_section(self, title, parent=None):
        if parent is None:
            parent = self.control_panel
        frame = tk.LabelFrame(parent, text=title, bg="#eee", padx=5, pady=5)
        frame.pack(fill="x", padx=5, pady=5)
        return frame


    def create_control_panel(self):
        # Basic Properties Section
        basic_frame = self.create_control_section("Basic Properties")
       
        # Fill Color
        self.create_color_picker(basic_frame, "Fill Color", 'fill_color')
       
        # Dimensions
        dim_frame = tk.Frame(basic_frame, bg="#eee")
        dim_frame.pack(fill="x", pady=2)
       
        tk.Label(dim_frame, text="Width:", bg="#eee").pack(side="left")
        width_scale = ttk.Scale(dim_frame, from_=10, to=200, orient="horizontal",
                              command=lambda v: self.update_setting('width', float(v)))
        width_scale.set(25)
        width_scale.pack(side="left", fill="x", expand=True, padx=5)
       
        dim_frame2 = tk.Frame(basic_frame, bg="#eee")
        dim_frame2.pack(fill="x", pady=2)
       
        tk.Label(dim_frame2, text="Height:", bg="#eee").pack(side="left")
        height_scale = ttk.Scale(dim_frame2, from_=10, to=200, orient="horizontal",
                               command=lambda v: self.update_setting('height', float(v)))
        height_scale.set(25)
        height_scale.pack(side="left", fill="x", expand=True, padx=5)


        # Stroke Properties Section
        stroke_frame = self.create_control_section("Stroke Properties")
       
        self.create_color_picker(stroke_frame, "Stroke Color", 'stroke_color')
       
        stroke_width_frame = tk.Frame(stroke_frame, bg="#eee")
        stroke_width_frame.pack(fill="x", pady=2)
       
        tk.Label(stroke_width_frame, text="Stroke Width:", bg="#eee").pack(side="left")
        stroke_scale = ttk.Scale(stroke_width_frame, from_=0, to=10, orient="horizontal",
                               command=lambda v: self.update_setting('stroke_width', float(v)))
        stroke_scale.pack(side="left", fill="x", expand=True, padx=5)


        # Transform Section
        transform_frame = self.create_control_section("Transformations")
       
        # Rotation
        self.create_slider(transform_frame, "Rotation", 'rotation', 0, 360)
       
        # Scale
        self.create_slider(transform_frame, "Scale X", 'scale_x', 0.1, 3)
        self.create_slider(transform_frame, "Scale Y", 'scale_y', 0.1, 3)
       
        # Skew
        self.create_slider(transform_frame, "Skew X", 'skew_x', -45, 45)
        self.create_slider(transform_frame, "Skew Y", 'skew_y', -45, 45)


        # Effects Section
        effects_frame = self.create_control_section("Effects")
       
        # Opacity
        self.create_slider(effects_frame, "Opacity", 'opacity', 0, 1)
       
        # Filters
        self.create_slider(effects_frame, "Blur", 'blur', 0, 10)
        self.create_slider(effects_frame, "Brightness", 'brightness', 0, 200)
        self.create_slider(effects_frame, "Contrast", 'contrast', 0, 200)


        # Shadow Section
        shadow_frame = self.create_control_section("Shadow")
       
        self.create_color_picker(shadow_frame, "Shadow Color", 'shadow_color')
        self.create_slider(shadow_frame, "Offset", 'shadow_offset', 0, 20)
        self.create_slider(shadow_frame, "Blur", 'shadow_blur', 0, 20)


        # Gradient Section
        gradient_frame = self.create_control_section("Gradient")
       
        self.create_color_picker(gradient_frame, "Start Color", 'gradient_start')
        self.create_color_picker(gradient_frame, "End Color", 'gradient_end')
       
        gradient_type_frame = tk.Frame(gradient_frame, bg="#eee")
        gradient_type_frame.pack(fill="x", pady=2)
       
        tk.Label(gradient_type_frame, text="Type:", bg="#eee").pack(side="left")
        gradient_types = ttk.Combobox(gradient_type_frame,
                                    values=['none', 'linear', 'radial'])
        gradient_types.set('none')
        gradient_types.pack(side="left", padx=5)
        gradient_types.bind('<<ComboboxSelected>>',
                          lambda e: self.update_setting('gradient_type', gradient_types.get()))


        # Animation Section
        animation_frame = self.create_control_section("Animation")
       
        anim_type_frame = tk.Frame(animation_frame, bg="#eee")
        anim_type_frame.pack(fill="x", pady=2)
       
        tk.Label(anim_type_frame, text="Type:", bg="#eee").pack(side="left")
        animation_types = ttk.Combobox(anim_type_frame,
                                     values=['none', 'rotate', 'pulse', 'bounce'])
        animation_types.set('none')
        animation_types.pack(side="left", padx=5)
        animation_types.bind('<<ComboboxSelected>>',
                           lambda e: self.update_setting('animation', animation_types.get()))
       
        self.create_slider(animation_frame, "Duration (s)", 'animation_duration', 0.1, 5)


    def create_slider(self, parent, label, setting_key, min_val, max_val):
        frame = tk.Frame(parent, bg="#eee")
        frame.pack(fill="x", pady=2)
       
        tk.Label(frame, text=f"{label}:", bg="#eee").pack(side="left")
        slider = ttk.Scale(frame, from_=min_val, to=max_val, orient="horizontal",
                          command=lambda v: self.update_setting(setting_key, float(v)))
        slider.set(self.current_settings[setting_key])
        slider.pack(side="left", fill="x", expand=True, padx=5)


    def create_color_picker(self, parent, label, setting_key):
        frame = tk.Frame(parent, bg="#eee")
        frame.pack(fill="x", pady=2)
       
        tk.Label(frame, text=f"{label}:", bg="#eee").pack(side="left")
        color_button = tk.Button(frame, text="Pick Color",
                               bg=self.current_settings[setting_key],
                               command=lambda: self.pick_color(setting_key, color_button))
        color_button.pack(side="left", padx=5)


    def create_sidebar(self):
        menu_items = [
            ("Book Icon", generate_ai_fill_book),
            ("Box Plot Icon", generate_ai_fill_box_plot),
            ("Bug Icon", generate_ai_fill_bug),
            ("Android Icon", generate_bs_android2)
        ]


        for item, generator in menu_items:
            button_frame = tk.Frame(self.sidebar, bg="#333")
           
            svg_data = generator(self.current_settings['fill_color'],
                               str(self.current_settings['width']),
                               str(self.current_settings['height']))
            svg_image = SvgImage(data=svg_data)
            image_label = tk.Label(button_frame, image=svg_image, bg="#333")
            image_label.image = svg_image
           
            name_label = tk.Label(button_frame, text=item, bg="#333", fg="white",
                                font=("Arial", 12))
           
            image_label.pack(side="left", padx=10, pady=10)
            name_label.pack(side="left", padx=10, pady=10)
            button_frame.pack(fill="x", pady=5)
           
            button_frame.bind("<Button-1>",
                            lambda e, gen=generator, item=item: self.select_svg(gen, item))


    def pick_color(self, setting_key, button):
        color = colorchooser.askcolor(color=self.current_settings[setting_key])[1]
        if color:
            self.current_settings[setting_key] = color
            button.configure(bg=color)
            self.update_svg()


    def update_setting(self, key, value):
        self.current_settings[key] = value
        self.update_svg()


    def select_svg(self, generator, title):
        self.current_svg_generator = generator
        self.current_title = title
        self.update_svg()


    def import_svg(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("SVG files", "*.svg"), ("All files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    svg_content = file.read()
                   
                # Extract fill color
                fill_match = re.search(r'fill="([^"]*)"', svg_content)
                if fill_match:
                    self.current_settings['fill_color'] = fill_match.group(1)
                   
                # Extract width/height
                width_match = re.search(r'width="([^"]*)"', svg_content)
                height_match = re.search(r'height="([^"]*)"', svg_content)
                if width_match:
                    self.current_settings['width'] = float(width_match.group(1))
                if height_match:
                    self.current_settings['height'] = float(height_match.group(1))
                   
                self.update_svg()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to import SVG: {str(e)}")


    def update_svg(self):
        # Clear the main content frame
        for widget in self.main_content.winfo_children():
            widget.destroy()


        # Create title
        title_label = tk.Label(self.main_content, text=self.current_title,
                             font=("Arial", 18, "bold"), bg="#fff", pady=20)
        title_label.pack()


        try:
            # Generate base SVG
            base_svg = self.current_svg_generator(
                self.current_settings['fill_color'],
                str(self.current_settings['width']),
                str(self.current_settings['height'])
            )


            # Parse SVG
            tree = ET.ElementTree(ET.fromstring(base_svg))
            root = tree.getroot()
           
            # Add defs section for filters and gradients
            defs = ET.SubElement(root, 'defs')
           
            # Add filters
            if any([self.current_settings['blur'],
                   self.current_settings['brightness'] != 100,
                   self.current_settings['contrast'] != 100,
                   self.current_settings['shadow_blur']]):
               
                filter_element = ET.SubElement(defs, 'filter', id='combined-filter')
               
                # Blur filter
                if self.current_settings['blur']:
                    ET.SubElement(filter_element, 'feGaussianBlur',
                                stdDeviation=str(self.current_settings['blur']))
               
                # Brightness filter
                if self.current_settings['brightness'] != 100:
                    matrix = str(self.current_settings['brightness'] / 100)
                    ET.SubElement(filter_element, 'feColorMatrix', type='matrix',
                                values=f"{matrix} 0 0 0 0 0 {matrix} 0 0 0 0 0 {matrix} 0 0 0 0 0 1 0")
               
                # Contrast filter
                if self.current_settings['contrast'] != 100:
                    contrast = self.current_settings['contrast'] / 100
                    intercept = (-0.5 * contrast + 0.5)
                    ET.SubElement(filter_element, 'feComponentTransfer')
               
                # Shadow filter
                if self.current_settings['shadow_blur']:
                    shadow_filter = ET.SubElement(defs, 'filter', id='shadow-filter')
                    # ET.SubElement(shadow_filter, 'feGaussianBlur',
                    #             stdDeviation=str(self.current_settings['shadow_blur']))
                    # ET.SubElement(shadow_filter, 'feOffset',
                    #             dx=str(self.current_settings['shadow_offset']),
                    #             dy=str(self
                                       
        # Continuing from the contrast filter setup
                if self.current_settings['contrast'] != 100:
                    contrast = self.current_settings['contrast'] / 100
                    intercept = (-0.5 * contrast + 0.5)
                    transfer = ET.SubElement(filter_element, 'feComponentTransfer')
                    for channel in ['R', 'G', 'B']:
                        ET.SubElement(transfer, 'feFunc' + channel,
                                    type='linear',
                                    slope=str(contrast),
                                    intercept=str(intercept))


            # Add gradient if selected
            if self.current_settings['gradient_type'] != 'none':
                gradient_id = 'svg-gradient'
                if self.current_settings['gradient_type'] == 'linear':
                    gradient = ET.SubElement(defs, 'linearGradient', id=gradient_id)
                    ET.SubElement(gradient, 'stop',
                                offset='0%',
                                style=f"stop-color:{self.current_settings['gradient_start']}")
                    ET.SubElement(gradient, 'stop',
                                offset='100%',
                                style=f"stop-color:{self.current_settings['gradient_end']}")
                else:  # radial gradient
                    gradient = ET.SubElement(defs, 'radialGradient', id=gradient_id)
                    ET.SubElement(gradient, 'stop',
