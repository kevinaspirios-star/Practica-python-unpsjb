import argparse
import string 

def get_string(msg): 
  return ("Hola "+ msg) 

if __name__ == "__main__" : 
    parser = argparse.ArgumentParser( 
        description= "Script que te saluda solo si ingresas un argumento"
     ) 
    parser.add_argument( "--msg" , required=True,type=str,help = "Ingrese su nombre" ) 
    args = parser.parse_args() 

    msg = args.msg

    print (get_string(msg))