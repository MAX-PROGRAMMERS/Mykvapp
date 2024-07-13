from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: dp(20)
    spacing: dp(10)

    ScrollView:
        size_hint_y: None
        height: dp(200)
        MDList:
            id: history_list
            padding: dp(10)
            spacing: dp(10)

    MDTextField:
        id: display
        hint_text: "The Max Programers"
        font_size: "48sp"
        size_hint_y: None
        height: dp(100)
        readonly: True
        foreground_color: app.theme_cls.text_color  # Use text color from theme

    GridLayout:
        cols: 4
        spacing: dp(12)
        size_hint_y: None
        height: self.minimum_height
        row_default_height: dp(70)  # Increased button height
        pos_hint: {'center_x': 0.5}  # Center-align the GridLayout

        MDRaisedButton:
            text: "7"
            on_release: app.on_button_press(self)
            md_bg_color: app.get_color_from_hex("#B3E5FC")  # Soft blue color
            elevation_normal: 0  # No elevation
            ripple_behavior: True
            text_color: 0, 0, 0, 1  # Black text color
            font_size: "24sp"  # Increased font size

        MDRaisedButton:
            text: "8"
            on_release: app.on_button_press(self)
            md_bg_color: app.get_color_from_hex("#B3E5FC")
            elevation_normal: 0
            ripple_behavior: True
            text_color: 0, 0, 0, 1
            font_size: "24sp"

        MDRaisedButton:
            text: "9"
            on_release: app.on_button_press(self)
            md_bg_color: app.get_color_from_hex("#B3E5FC")
            elevation_normal: 0
            ripple_behavior: True
            text_color: 0, 0, 0, 1
            font_size: "24sp"

        MDRaisedButton:
            text: "DEL"
            on_release: app.on_del_button_down()
            on_release: app.on_del_button_up()
            md_bg_color: app.get_color_from_hex("#B3E5FC")
            elevation_normal: 0
            ripple_behavior: True
            text_color: 0, 0, 0, 1
            font_size: "24sp"

        MDRaisedButton:
            text: "4"
            on_release: app.on_button_press(self)
            md_bg_color: app.get_color_from_hex("#B3E5FC")
            elevation_normal: 0
            ripple_behavior: True
            text_color: 0, 0, 0, 1
            font_size: "24sp"

        MDRaisedButton:
            text: "5"
            on_release: app.on_button_press(self)
            md_bg_color: app.get_color_from_hex("#B3E5FC")
            elevation_normal: 0
            ripple_behavior: True
            text_color: 0, 0, 0, 1
            font_size: "24sp"

        MDRaisedButton:
            text: "6"
            on_release: app.on_button_press(self)
            md_bg_color: app.get_color_from_hex("#B3E5FC")
            elevation_normal: 0
            ripple_behavior: True
            text_color: 0, 0, 0, 1
            font_size: "24sp"

        MDRaisedButton:
            text: "*"
            on_release: app.on_button_press(self)
            md_bg_color: app.get_color_from_hex("#B3E5FC")
            elevation_normal: 0
            ripple_behavior: True
            text_color: 0, 0, 0, 1
            font_size: "24sp"

        MDRaisedButton:
            text: "1"
            on_release: app.on_button_press(self)
            md_bg_color: app.get_color_from_hex("#B3E5FC")
            elevation_normal: 0
            ripple_behavior: True
            text_color: 0, 0, 0, 1
            font_size: "24sp"

        MDRaisedButton:
            text: "2"
            on_release: app.on_button_press(self)
            md_bg_color: app.get_color_from_hex("#B3E5FC")
            elevation_normal: 0
            ripple_behavior: True
            text_color: 0, 0, 0, 1
            font_size: "24sp"

        MDRaisedButton:
            text: "3"
            on_release: app.on_button_press(self)
            md_bg_color: app.get_color_from_hex("#B3E5FC")
            elevation_normal: 0
            ripple_behavior: True
            text_color: 0, 0, 0, 1
            font_size: "24sp"

        MDRaisedButton:
            text: "-"
            on_release: app.on_button_press(self)
            md_bg_color: app.get_color_from_hex("#B3E5FC")
            elevation_normal: 0
            ripple_behavior: True
            text_color: 0, 0, 0, 1
            font_size: "24sp"

        MDRaisedButton:
            text: "0"
            on_release: app.on_button_press(self)
            md_bg_color: app.get_color_from_hex("#B3E5FC")
            elevation_normal: 0
            ripple_behavior: True
            text_color: 0, 0, 0, 1
            font_size: "24sp"

        MDRaisedButton:
            text: "."
            on_release: app.on_button_press(self)
            md_bg_color: app.get_color_from_hex("#B3E5FC")
            elevation_normal: 0
            ripple_behavior: True
            text_color: 0, 0, 0, 1
            font_size: "24sp"

        MDRaisedButton:
            text: "="
            on_release: app.on_button_press(self)
            md_bg_color: app.get_color_from_hex("#B3E5FC")
            elevation_normal: 0
            ripple_behavior: True
            text_color: 0, 0, 0, 1
            font_size: "24sp"

        MDRaisedButton:
            text: "+"
            on_release: app.on_button_press(self)
            md_bg_color: app.get_color_from_hex("#B3E5FC")
            elevation_normal: 0
            ripple_behavior: True
            text_color: 0, 0, 0, 1
            font_size: "24sp"

        MDRaisedButton:
            text: "AC"
            on_release: app.on_clear_button_press()
            md_bg_color: app.get_color_from_hex("#B3E5FC")
            elevation_normal: 0
            ripple_behavior: True
            text_color: 0, 0, 0, 1
            font_size: "24sp"

        MDIconButton:
            icon: "cog"
            theme_text_color: "Custom"
            text_color: app.get_color_from_hex("#B3E5FC")  # Soft blue color
            on_press: app.open_settings()
'''

class CalculatorApp(MDApp):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = None  # Initialize dialog attribute

    def build(self):
        self.theme_cls.primary_palette = 'BlueGray'  # Set primary color palette
        self.theme_cls.accent_palette = 'Amber'  # Set accent color palette
        self.theme_cls.theme_style = 'Light'  # Use light theme style

        self.title = 'Professional Calculator'
        return Builder.load_string(KV)

    def on_button_press(self, instance):
        button_text = instance.text

        if button_text == '=':
            try:
                expression = self.root.ids.display.text
                result = str(eval(expression))
                self.root.ids.display.text = result
                self.update_history(expression + ' = ' + result)
            except Exception as e:
                pass
        elif button_text == 'C':
            self.on_clear_button_press()
        else:
            self.root.ids.display.text += button_text

    def on_clear_button_press(self):
        self.root.ids.display.text = ''

    def on_del_button_down(self):
        # Start continuous deletion when button is pressed
        self.del_clock_event = Clock.schedule_interval(self.delete_character, 0.1)

    def on_del_button_up(self):
        # Stop continuous deletion when button is released
        if hasattr(self, 'del_clock_event'):
            self.del_clock_event.cancel()

    def delete_character(self, dt):
        # Function to delete a character from display
        current_text = self.root.ids.display.text
        if current_text:
            self.root.ids.display.text = current_text[:-1]

    def update_history(self, text):
        history_label = MDLabel(
            text=text,
            halign='right',
            theme_text_color='Secondary',
            size_hint_y=None,
            height=dp(50),
            padding=(dp(20), dp(10))
        )
        self.root.ids.history_list.add_widget(history_label)
        self.root.ids.history_list.parent.scroll_y = 0

    def open_settings(self):
        content = MDBoxLayout(orientation='vertical', padding=dp(-40), spacing=dp(0))
        spacer = MDBoxLayout()
        content.add_widget(spacer)
        toggle_btn = MDRaisedButton(
            text="Toggle Dark Mode",
            on_release=self.toggle_theme_mode,
            padding=(dp(20), dp(10)),  # Adjusted padding
            halign='right',
            valign='bottom'  # Align button to the bottom
        )
        content.add_widget(toggle_btn)

        self.dialog = MDDialog(
            title="Settings",
            type="custom",
            content_cls=content,
            size_hint=(0.8, None),  # Adjusted size_hint width, height will be computed
            height=toggle_btn.height + spacer.height,
            buttons=[MDFlatButton(text="Close", on_release=self.close_settings)],
            auto_dismiss=True
        )
        self.dialog.open()

    def close_settings(self, *args):
        self.dialog.dismiss()

    def toggle_theme_mode(self, instance):
        if self.theme_cls.theme_style == 'Dark':
            self.theme_cls.theme_style = 'Light'
            Window.clearcolor = self.theme_cls.bg_light
        else:
            self.theme_cls.theme_style = 'Dark'
            Window.clearcolor = self.theme_cls.bg_dark

        self.dialog.dismiss()  # Close the dialog after toggling theme mode

    def get_color_from_hex(self, hex_color):
        """Convert hex color to RGBA tuple."""
        return [int(hex_color[i:i+2], 16) / 255.0 for i in range(1, 7, 2)] + [1.0]

if __name__ == '__main__':
    CalculatorApp().run()