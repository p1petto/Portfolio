shader_type canvas_item;
uniform vec4 oldcolor1 : source_color;
uniform vec4 oldcolor2 : source_color;
uniform vec4 oldcolor3 : source_color;

uniform vec4 newcolor1 : source_color;
uniform vec4 newcolor2 : source_color;
uniform vec4 newcolor3 : source_color;

void fragment() {
    vec4 curr_color = texture(TEXTURE,UV); 
	
    if(distance(COLOR, oldcolor1) < 0.1){
        COLOR = newcolor1;
	}
	else if(distance(COLOR, oldcolor2) < 0.1)
	{
		 COLOR = newcolor2;
    }
	else if (distance(COLOR, oldcolor3) < 0.1)
	{
        COLOR = newcolor3;
    }
	else
	{
        COLOR = curr_color;
    }
}