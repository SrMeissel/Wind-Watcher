import dearpygui.dearpygui as dpg
import mysql.connector 

database = mysql.connector.connect( 
    host= "localhost",
    user= "client",
    password = "meissel",
    database = "WindWatcher"
)
print(database)

cursor = database.cursor()

#cursor.execute("CREATE DATABASE WindWatcher")
#cursor.execute("SHOW DATABASES")

#cursor.execute("CREATE TABLE Data (DeviceID VARCHAR(255), Temperature VARCHAR(255), Pressure VARCHAR(255))")
#cursor.execute("ALTER TABLE Data ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)

# GUI ================================================
dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300)

with dpg.window(label="Example Window"):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()