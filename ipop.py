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

def choice_from_list(in_list,string="Nummer: ",print_list=False,out_list=False):
    for i,k in enumerate(in_list):
        print("  %d: %s"%(i,(print_list[k] if print_list else k)))
    inp = int_input(string,len(in_list)-1)
    if out_list: return out_list[ in_list[inp] ]
    return in_list[inp]
