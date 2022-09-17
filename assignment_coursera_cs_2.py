
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def strip_punctuation  (x):
    for i in punctuation_chars:
        x = x.replace(i, '')
    return x
            
def get_pos (x):
    x = strip_punctuation(x)
    y = x.lower().split()
    count = 0
    for i in y:
        if i in positive_words:
            count = count + 1
    return count

def get_neg (x):
    x = strip_punctuation(x)
    y = x.lower().split()
    count = 0
    for i in y:
        if i in negative_words:
            count = count + 1
    return count
def strip_punctuation  (x):
    for i in punctuation_chars:
        x = x.replace(i, '')
    return x
outfile = open("resulting_data.csv","w")
outfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outfile.write("\n")
fileref = open("project_twitter_data.csv","r")
lines = fileref.readlines()[1:]
for line in lines:
    positive_score = get_pos(line) #using our pre-defined function
    negative_score = get_neg(line)
    net_score = positive_score - negative_score
    my_line = line.split(",")
    #print(my_line)
    retweets = int(my_line[1])
    n_reply = int(my_line[2])
    file_line = "{},{},{},{},{}".format(retweets, n_reply, positive_score, negative_score, net_score)
    outfile.write(file_line)
    outfile.write("\n")
