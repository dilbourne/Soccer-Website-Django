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