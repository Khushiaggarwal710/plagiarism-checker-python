import re
from difflib import SequenceMatcher

# Function to remove punctuations
def remove_punctuation(text):
    res = re.sub(r'[^\w\d\s.]','',text)
    return res

# Function to check longest match
def find_best_longest_match(line,paragraph):
    lines2 = paragraph.split(".")

    best_match = ""
    best_score = 0.5

    for line2 in lines2:
        sm = SequenceMatcher(None,line,line2)
        match = sm.find_longest_match(0,len(line),0,len(line2))
        score = sm.ratio()

        if score > best_score:
            best_match = line2[match.b:match.b + match.size]
            best_score = score

    return best_match

# Function to check plagiarism in given text
# main function
def check_plagiarism(text1,text2):
    output = []

    data1 = text1.lower()
    data2 = text2.lower()

    data1 = remove_punctuation(data1)
    data2 = remove_punctuation(data2)
   
    lines1 = data1.split(".")
    for line1 in lines1:
        output.append(find_best_longest_match(line1,data2))
    
    output = [res for res in output if res != ""]
    return output
