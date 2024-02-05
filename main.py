import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


#Init=====================================================================
dpg.create_context()
dpg.create_viewport(title='Wind Watcher', width=600, height=600)

#define event handles
def example_handler(sender, app_data):
    print("handle happened :) \n")

with dpg.item_handler_registry(tag="Widget Handler"):
    dpg.add_item_clicked_handler(callback=example_handler)

#define window objects
with dpg.window(tag="Primary Window"):
    dpg.add_text("Click Me", tag = "text")

#bind handlers to objects
dpg.bind_item_handler_registry("text", "Widget Handler")

#prepare to render
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)

#Run =====================================================================
while dpg.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    
    dpg.render_dearpygui_frame() 


    

dpg.destroy_context()