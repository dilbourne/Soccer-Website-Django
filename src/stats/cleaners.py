import re
from more_itertools import unique_everseen
from datetime import datetime as dt
# CLEANERS
def clean_player_page(stats):
    # extract stat names and values from raw html
    names_and_values = []
    for t in stats:
        names_and_values.append(t.text.strip())
    
    # filter out stat titles such as 'Attack', 'Defence', 'Discipline'
    names_and_values = list(filter(lambda x: '\n' in x,names_and_values))

    # split into stat name and value
    names_and_values = list(map(lambda x: x.split('\n'),names_and_values))
    
    # remove whitespace and convert to dict
    stats_dict = {t[0].strip():t[1].strip() for t in names_and_values}

    # convert percentage values to a range between [0,1] & get rid of commas in values
    for key, val in stats_dict.items():
        if '%' in val:
            stats_dict[key] = float(float(val.strip('%'))/100)
        elif ',' in val:
            stats_dict[key] = val.replace(',','')
        else:
            stats_dict[key] = float(val)
    
    return stats_dict

def clean_player_overview(arr):
    a = list(unique_everseen([t.text.strip() for t in arr]))
    try:
        b = [*a[:4],*a[6:]]
        # if a[4] is a shirtnumber
        if re.search("[0-9]+",b[4]):
            return {"Club":b[0], "Role":b[1][0], "Country":b[2], "Dob": dt.strptime(b[3].split(" ")[0],"%d/%m/%Y"),
                    "Shirtnum":int(b[4]), "Name":b[5]}
        else:
            return {"Club":b[0], "Role":b[1][0], "Country":b[2], "Dob": dt.strptime(b[3].split(" ")[0],"%d/%m/%Y")
               , "Shirtnum": 0, "Name":b[4]}
    except IndexError:
        try:
            b = [*a[:4],*a[5:]]
            if re.search("[0-9]+",b[4]):
                #if a[4] is a shirt number.....
                return {"Club":b[0], "Role":b[1][0], "Country":b[2], "Dob": dt.strptime(b[3].split(" ")[0],"%d/%m/%Y"),
                        "Shirtnum":int(b[4]), "Name":b[5]}
            else:
                return {"Club":b[0], "Role":b[1][0], "Country":b[2], "Dob": dt.strptime(b[3].split(" ")[0],"%d/%m/%Y")
                   , "Shirtnum": 0, "Name":b[4]}
        except IndexError:
            b = [*a[:4],*[a[4]]]
            if re.search("[0-9]+",b[4]):
                #if a[4] is a shirt number.....
                return {"Club":b[0], "Role":b[1][0], "Country":b[2], "Dob": dt.strptime(b[3].split(" ")[0],"%d/%m/%Y"),
                        "Shirtnum":int(b[4]), "Name":b[5]}
            else:
                return {"Club":b[0], "Role":b[1][0], "Country":b[2], "Dob": dt.strptime(b[3].split(" ")[0],"%d/%m/%Y")
                   , "Shirtnum": 0, "Name":b[4]}