try:
    f=open('simple.txt','r')
    f.write("TEST write to simple text!")
except IOError:
    # or just   general except:
    print("Error:could NOT FIND FILE OR READ DATA!")
finally:
    print("SUCCESS!")
    f.close()

