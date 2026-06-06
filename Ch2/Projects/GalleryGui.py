from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image
from kivy.uix.label import Label
import os


class ImageGalleryApp(App):
    def build(self):
        # لایه اصلی برنامه
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # ۱. دکمه بالا برای انتخاب فولدر
        self.btn_select_folder = Button(text="Select Folder with Images", size_hint_y=0.1)
        self.btn_select_folder.bind(on_release=self.show_folder_chooser)
        self.main_layout.add_widget(self.btn_select_folder)

        # ۲. فضایی برای نمایش اسلایدر یا متن راهنما
        self.gallery_area = BoxLayout(orientation='vertical')
        self.placeholder_label = Label(text="No folder selected yet.\nClick the button above to load images.",
                                       halign="center")
        self.gallery_area.add_widget(self.placeholder_label)
        self.main_layout.add_widget(self.gallery_area)

        # ۳. دکمه‌های ناوبری (بعدی / قبلی) که در ابتدا مخفی یا غیرفعال هستند
        self.nav_layout = BoxLayout(size_hint_y=0.1, spacing=10)
        self.btn_prev = Button(text="Previous", disabled=True)
        self.btn_next = Button(text="Next", disabled=True)

        self.btn_prev.bind(on_release=self.go_prev)
        self.btn_next.bind(on_release=self.go_next)

        self.nav_layout.add_widget(self.btn_prev)
        self.nav_layout.add_widget(self.btn_next)
        self.main_layout.add_widget(self.nav_layout)

        self.carousel = None
        return self.main_layout

    def show_folder_chooser(self, instance):
        box = BoxLayout(orientation='vertical', spacing=10)

        file_chooser = FileChooserListView(dirselect=True)
        file_chooser.path = os.path.expanduser("~")  # شروع از پوشه کاربری

        btn_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        btn_select = Button(text="Choose This Folder")
        btn_cancel = Button(text="Cancel")

        btn_layout.add_widget(btn_select)
        btn_layout.add_widget(btn_cancel)

        box.add_widget(file_chooser)
        box.add_widget(btn_layout)

        popup = Popup(title="Select Folder Containing Images", content=box, size_hint=(0.9, 0.9))

        btn_cancel.bind(on_release=popup.dismiss)
        btn_select.bind(
            on_release=lambda btn: self.load_images_from_folder(file_chooser.selection, file_chooser.path, popup))

        popup.open()

    def load_images_from_folder(self, selection, current_path, popup):
        folder_path = selection[0] if selection else current_path
        popup.dismiss()

        valid_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')

        image_paths = []
        try:
            for file in os.listdir(folder_path):
                if file.lower().endswith(valid_extensions):
                    full_path = os.path.join(folder_path, file)
                    image_paths.append(full_path)
        except Exception as e:
            print("Error reading directory:", e)
            return

        self.gallery_area.clear_widgets()

        if not image_paths:
            self.gallery_area.add_widget(Label(text="No images found in this folder!"))
            self.btn_prev.disabled = True
            self.btn_next.disabled = True
            return

        self.carousel = Carousel(direction='right', loop=True)

        for path in image_paths:
            img = Image(source=path, allow_stretch=True, keep_ratio=True)
            self.carousel.add_widget(img)

        self.gallery_area.add_widget(self.carousel)

        self.btn_prev.disabled = False
        self.btn_next.disabled = False

    def go_prev(self, instance):
        if self.carousel:
            self.carousel.load_previous()

    def go_next(self, instance):
        if self.carousel:
            self.carousel.load_next()


if __name__ == '__main__':
    ImageGalleryApp().run()
