shader_type canvas_item;
uniform float blue; // you can assign a default value to uniforms
/*
void fragment(){
  COLOR = texture(TEXTURE, UV); //read from texture
  COLOR.b = blue;
}
*/
uniform vec4 oldcolor1 : source_color;
uniform vec4 oldcolor2 : source_color;
uniform vec4 oldcolor3 : source_color;

uniform vec4 newcolor1 : source_color;
uniform vec4 newcolor2 : source_color;
uniform vec4 newcolor3 : source_color;

void fragment() {
    vec4 curr_color = texture(TEXTURE,UV); // Get current color of pixel
	
	//Lets check that our current pixel colour is any of the OLDCOLORs we wish to swap
	//If our pixel is an old colour then swap COLOR to NEWCOLOR, very simple
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
		//We didn't find any old colors for this pixel so keep it's original color
        COLOR = curr_color;
    }
}