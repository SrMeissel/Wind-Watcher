import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

def display():
    #Init=====================================================================

    dpg.create_context()

    #make things stylish
    with dpg.theme() as global_theme:

        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 140, 23), category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

        with dpg.theme_component(dpg.mvInputInt):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (140, 255, 23), category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

    dpg.bind_theme(global_theme)
    dpg.show_style_editor()

    #define event handles
    def example_handler(sender, app_data):
        print("handle happened :)")

    with dpg.item_handler_registry(tag="Widget Handler"):
        dpg.add_item_clicked_handler(callback=example_handler)

    #define direct callbacks
    def button_callback(sender, app_data, user_data):
        print("button pressed in " + user_data)

    def file_select_callback(sender, app_data):
        print('OK was clicked.')
        print("Sender: ", sender)
        print("App Data: ", app_data)

    def file_cancel_callback(sender, app_data):
        print('Cancel was clicked.')
        print("Sender: ", sender)
        print("App Data: ", app_data)

    #define file dialog 
    with dpg.file_dialog(directory_selector=False, show=False, callback=file_select_callback, cancel_callback=file_cancel_callback, tag="file dialog", width=700 ,height=400):
        dpg.add_file_extension(".*")
        dpg.add_file_extension("", color=(150, 255, 150, 255))
        dpg.add_file_extension("Source files (*.cpp *.h *.hpp){.cpp,.h,.hpp}", color=(0, 255, 255, 255))
        dpg.add_file_extension(".h", color=(255, 0, 255, 255), custom_text="[header]")
        dpg.add_file_extension(".py", color=(0, 255, 0, 255), custom_text="[Python]")

    #define window objects
    with dpg.window(tag="Primary Window") as window:
        dpg.add_text("Click Me", tag = "text")
        dpg.add_button(enabled=True, label="Press me", tag="item", callback=button_callback, user_data="toronto")

        dpg.add_button(label="Directory Selector", callback=lambda: dpg.show_item("file dialog"))
        

    #bind handlers to objects
    dpg.bind_item_handler_registry("text", "Widget Handler")

    #prepare to render
    dpg.create_viewport(title='Wind Watcher', width=600, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)

    #Run =====================================================================

    while dpg.is_dearpygui_running():
        # this code runs every frame while events happens depending on IO
        # you can manually stop by using stop_dearpygui()
        
        dpg.render_dearpygui_frame() 

    #die
    dpg.destroy_context()