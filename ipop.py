def int_input(string,max_val=False):# {{{
    while(1):
        try:
            inp = int(input(string))
            if max_val and inp > max_val:
                print("Eingegebener Wert zu groß! Maximal %d"%(max_val))
                continue
            return(inp)
        except ValueError:
            print("Eingabe fehlerhaft. Bitte Integer angeben.")
# }}}
