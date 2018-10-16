def main():
    """Prints a table of fahrenheit temperatures 
       and their Celsius equivalents"""
   
    lower = 0
    upper = 300
    step = 20

    fahr = lower
    print("F\tC")
    while(fahr <= upper):
        celsius = 5 * (fahr-32) / 9
        print("%d\t%d" % (fahr, celsius))
        fahr = fahr + step

if __name__ == "__main__":
    main()
