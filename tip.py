def dollars_to_float(d):
    dollars = d.replace("$", "")
    dollars = float(dollars)
    return(dollars)



def percent_to_float(p):
    percent = p.replace("%", "")
    percent = float(percent)
    percent = (percent /100)
    return(percent)


main()
