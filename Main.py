import poiFinder

#Main File Runner
#fucntions File
res = input("Press 1 for Run\nPress any key to exit\n")
selection = str(res)

if(selection == str("1")):
    poiFinder.FetchPoi()
else:
    print("exiting")
