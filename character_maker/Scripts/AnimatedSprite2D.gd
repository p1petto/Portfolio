extends AnimatedSprite2D


func _on_color_picker_button_color_changed(color):
	material.set("shader_parameter/newcolor1",color)
	pass 


func _on_color_picker_button_2_color_changed(color):
	material.set("shader_parameter/newcolor2",color)
	pass # Replace with function body.


func _on_color_picker_button_3_color_changed(color):
	material.set("shader_parameter/newcolor3",color)
	pass # Replace with function body.
	
func _ready():
	var blue_value = 1
	material.set_shader_parameter("blue", blue_value)
	#material.set_shader_parameter("OLDCOLOR1",Color(0.78, 0.78, 0.78));
	#print("ready")
	#print(material.get_shader_parameter("OLDCOLOR1"))
	#material.set_shader_parameter("NEWCOLOR1", Color(1, 1, 1, 1));
	pass

