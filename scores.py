import sys
scores = [float(score)for score in sys.argv[1:]]
if not scores:
    print("Enter scores after the program name.")
else:
    print("sum:",sum(scores))
    print("Average:",sum(scores)/len(scores))
    print("Maximum:",max(scores))