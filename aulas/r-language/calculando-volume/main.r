# Seja um tubo com raio de 10cm, com 1,5 metros de comprimento e com uma espessura de 1cm. Qual o volume deste cubo?
# Volume = pi · raio² · altura

raio <- 10 #cm
comprimento <- 70 
espessura <- 1 #cm

volume <- pi * (raio - espessura)^2 * comprimento 

print(volume)