def multitable():
    f1 = .1
    f2 = .2
    f3 = .3

    print ("   " + str("%10.1f"%f1) + str("%10.1f"%f2) + str("%10.1f"%f3))
    print (str(f1) + str(("%10.2f"%(f1*f1))) + str(("%10.2f"%(f1*f2))) + str(("%10.2f"%(f1*f3))))
    print (str(f2) + str(("%10.2f"%(f2*f1))) + str(("%10.2f"%(f2*f2))) + str(("%10.2f"%(f2*f3))))
    print (str(f3) + str(("%10.2f"%(f3*f1))) + str(("%10.2f"%(f3*f2))) + str(("%10.2f"%(f3*f3))))
    
multitable()
