# Python 3.8.6

#prep: import the following packages, and define a few functions 
from collections import Counter   #this package helps us get the most frequent words out of a list
import re    #we need this module to define regex
import os    
import os.path
import string
import nltk
nltk.download('punkt')
from nltk.tokenize import MWETokenizer  #import tokenizer
tokenizer = MWETokenizer()
nltk.download('stopwords')  #download the list of stopwords, if you have not already done so
from nltk.corpus import stopwords  #import the list of stopwords
from nltk.stem.snowball import SnowballStemmer  #import stemmer module
stemmer = SnowballStemmer('english')
import pandas as pd
import spacy    #this package helps us identify location (cities, states, rivers etc.)
nlp = spacy.load('en_core_web_sm') # Load in language package

#define the following functions
def cmp(a, b):
    return (a > b) - (a < b) 

def clean_tokenize (text):
    # remove numbers
    text_nonum = re.sub(r'\d+', '', text)
    text_nonum = text_nonum.replace('”', '')
    text_nonum = text_nonum.replace('“', '')
    text_nonum = text_nonum.replace('—', ' ')
    # remove punctuations and convert characters to lower case
    text_nopunct = "".join([char.lower() for char in text_nonum if char not in string.punctuation]) 
    # substitute multiple whitespace with single whitespace. Also, removes leading and trailing whitespaces
    text_cleaned = re.sub('\s+', ' ', text_nopunct).strip()
    text_output = tokenizer.tokenize(text_cleaned.split())
    text_stopwords = []
    for word in text_output:
        if word not in stopwords.words('english'):  #filter the stop words
            text_stopwords.append(word) 
    text_stemmed = ([stemmer.stem(w) for w in text_stopwords])
    return text_stemmed


# Set current working directory

wrkDir = 'C:/Users/willi/Documents/Data Science Practice Projects/Fordham Projects/Computational_Finance_Final_Project_NLP/'

#step 1: read-in the positive words list, and negative words list
curDir = os.getcwd()  
os.chdir(wrkDir) 
df1 = pd.read_excel('LM Sentiment Dictionary.xlsx', sheet_name='Positive') # can also index sheet by name or fetch all sheets
positive_temp = df1['WORD'].tolist()
positive_temp = [item.lower() for item in positive_temp]
positive=[]
for word in positive_temp:
    positive.append(' ' + word + ' ')

df2 = pd.read_excel('LM Sentiment Dictionary.xlsx', sheet_name='Negative') # can also index sheet by name or fetch all sheets
negative_temp = df2['WORD'].tolist()
negative_temp = [item.lower() for item in negative_temp]
negative=[]
for word in negative_temp:
    negative.append(' ' + word + ' ')

df3 = pd.read_excel('LM Sentiment Dictionary.xlsx', sheet_name='Riskqje') # can also index sheet by name or fetch all sheets
risk1 = df3['WORD'].tolist()
riskqje_temp = [item.lower() for item in risk1]
riskqje=[]
for word in riskqje_temp:
    riskqje.append(' ' + word + ' ')




#step 2: read-in the ESG and non-ESG training libraries. Build the ESG dictionaries
 
curDir = os.getcwd()
print('Current directory is ',curDir)   
os.chdir(wrkDir +'ESG Libraries/Environmental/')
curDir = os.getcwd() 
print('Current directory is ',curDir)
   
environmental_lib=''
for parent, dirnames, filenames in os.walk(curDir):
    for filename in filenames:
        basename, extname = os.path.splitext(filename)
        if(cmp(extname, '.txt') == 0):
            file_in = open(filename, encoding='utf-8', errors='ignore')
            text = file_in.read()
            doc = nlp(text)    #remove location names (city, state,countries)
            places=[]
            for ent in doc.ents:
                if ent.label_ in ['GPE', 'LOC']: #GPE:countries, cities, states, LOC:non gpe locations, mountain ranges, bodies of water
                    print (ent.text, ent.label_)
                    places.append(ent.text)
            for place in places:
                text = text.replace(place,'')
            environmental_lib = environmental_lib + ' ' + text
            file_in.close()

environmental_tokens = clean_tokenize(environmental_lib)

curDir = os.getcwd()   
os.chdir(wrkDir + 'ESG Libraries/Social/')
curDir = os.getcwd() 
social_lib=''
for parent, dirnames, filenames in os.walk(curDir):
    for filename in filenames:
        basename, extname = os.path.splitext(filename)
        if(cmp(extname, '.txt') == 0):
            file_in = open(filename, encoding='utf-8', errors='ignore')
            text = file_in.read()
            doc = nlp(text)    #remove location names (city, state,countries)
            places=[]
            for ent in doc.ents:
                if ent.label_ in ['GPE', 'LOC']: #GPE:countries, cities, states, LOC:non gpe locations, mountain ranges, bodies of water
                    print (ent.text, ent.label_)
                    places.append(ent.text)
            for place in places:
                text = text.replace(place,'')
            social_lib = social_lib + ' ' + text
            file_in.close()

social_tokens = clean_tokenize(social_lib)


curDir = os.getcwd()   
os.chdir(wrkDir + 'ESG Libraries/Governance/')
curDir = os.getcwd() 
governance_lib=''
for parent, dirnames, filenames in os.walk(curDir):
    for filename in filenames:
        basename, extname = os.path.splitext(filename)
        if(cmp(extname, '.txt') == 0):
            file_in = open(filename, encoding='utf-8', errors='ignore')
            text = file_in.read()
            doc = nlp(text)    #remove location names (city, state,countries)
            places=[]
            for ent in doc.ents:
                if ent.label_ in ['GPE', 'LOC']: #GPE:countries, cities, states, LOC:non gpe locations, mountain ranges, bodies of water
                    print (ent.text, ent.label_)
                    places.append(ent.text)
            for place in places:
                text = text.replace(place,'')
            governance_lib = governance_lib + ' ' + text
            file_in.close()

governance_tokens = clean_tokenize(governance_lib)

curDir = os.getcwd()   
os.chdir(wrkDir + 'Non ESG Libraries/')
curDir = os.getcwd() 

nonesg_lib=''
for parent, dirnames, filenames in os.walk(curDir):
    for filename in filenames:
        basename, extname = os.path.splitext(filename)
        if(cmp(extname, '.txt') == 0):
            file_in = open(filename, encoding='utf-8', errors='ignore')
            text = file_in.read()
            doc = nlp(text)    #remove location names (city, state,countries)
            places=[]
            for ent in doc.ents:
                if ent.label_ in ['GPE', 'LOC']: #GPE:countries, cities, states, LOC:non gpe locations, mountain ranges, bodies of water
                    print (ent.text, ent.label_)
                    places.append(ent.text)
            for place in places:
                text = text.replace(place,'')
            nonesg_lib = nonesg_lib + ' ' + text
            file_in.close()

nonesg_tokens = clean_tokenize(nonesg_lib)

nonesg=Counter(nonesg_tokens)      #note that counter is a class, not a list
most_frequent = nonesg.most_common(1000)
   
nonesg_final=set()
for x in nonesg.elements():
    if nonesg[x]>30:   #the number 30 is given at the programmer's discretion
        nonesg_final.add(x)

environmental_final = ([w for w in environmental_tokens if w not in nonesg_final])
environmental_final_len = len(environmental_final)
environmental_dict = Counter(environmental_final)

social_final = ([w for w in social_tokens if w not in nonesg_final])
social_final_len = len(social_final)
social_dict = Counter(social_final)

governance_final = ([w for w in governance_tokens if w not in nonesg_final])
governance_final_len = len(governance_final)
governance_dict = Counter(governance_final)

def docuanalyze(filename):
    #step 3: read-in the textual document to be analyzed
    curDir = os.getcwd()
    os.chdir(wrkDir + 'Annual Report Files/')  #check: change to the current working directory 
    curDir = os.getcwd()         
    for parent, dirnames, filenames in os.walk(curDir):  
        for filename in filenames:
            basename, extname = os.path.splitext(filename)
            if(cmp(extname, '.txt') == 0):
                file_in = open(filename, 'r', encoding='utf-8', errors='ignore') 
                docu=file_in.read()
                                
                #step 4: build a moving three sentences window, and identify all of the Environmental discussions
                sentences = nltk.tokenize.sent_tokenize(docu)
                
                x=0
                positive_environmental_weight=0
                negative_environmental_weight=0

                while x < len(sentences)-2:
                    threesentences1 = sentences[x] + ' ' + sentences[x+1] + ' ' + sentences[x+2]
                    positive_enviro_dummy=0
                    negative_enviro_dummy=0
                    for pword in positive:
                        if pword in threesentences1:
                            positive_enviro_dummy=1
                    for nword in negative:
                        if nword in threesentences1:
                            negative_enviro_dummy=1
                        
                    if positive_enviro_dummy==1:
                        #search for the words in the environmental library
                        three_tokens1 = clean_tokenize(threesentences1)
                        for t in three_tokens1:
                            if t in environmental_dict.elements():
                                positive_environmental_weight = positive_environmental_weight + environmental_dict[t]/environmental_final_len
                       
                    if negative_enviro_dummy==1:
                        #search for the words in the Environmental library
                        three_tokens1 = clean_tokenize(threesentences1)
                        for t in three_tokens1:
                            if t in environmental_dict.elements():
                                negative_environmental_weight = negative_environmental_weight + environmental_dict[t]/environmental_final_len
                
                    if negative_enviro_dummy + positive_enviro_dummy > 0:
                        x = x + 2
                                
                    x = x + 1
                
                
                #step 5: Aggregate total environmental discussions, forward-looking climate risk, historical climate risk, sentiment on climate issues           
                docu_tokens = clean_tokenize(docu)
                total_enviro_discuss= positive_environmental_weight + negative_environmental_weight
                total_enviro_points = positive_environmental_weight - negative_environmental_weight
                enviro_sentiment = (total_enviro_points) / len(docu_tokens)
                
                print('Total Discussion of Environmental Issues is: ' + str(total_enviro_discuss))
                print('Total Environmental Points is: ' + str(total_enviro_points) + ' points')
                print('Total Environmental Sentiment is: ' + str(enviro_sentiment))

                # REPEAT STEP 4 & 5 FOR EACH REMAINING CATEGORY
                
                x=0
                positive_social_weight=0
                negative_social_weight=0

                while x < len(sentences)-2:
                    threesentences1 = sentences[x] + ' ' + sentences[x+1] + ' ' + sentences[x+2]
                    positive_social_dummy=0
                    negative_social_dummy=0
                    for pword in positive:
                        if pword in threesentences1:
                            positive_social_dummy=1
                    for nword in negative:
                        if nword in threesentences1:
                            negative_social_dummy=1
                        
                    if positive_social_dummy==1:
                        #search for the words in the social library
                        three_tokens1 = clean_tokenize(threesentences1)
                        for t in three_tokens1:
                            if t in environmental_dict.elements():
                                positive_social_weight = positive_social_weight + social_dict[t]/social_final_len
                       
                    if negative_social_dummy==1:
                        #search for the words in the social library
                        three_tokens1 = clean_tokenize(threesentences1)
                        for t in three_tokens1:
                            if t in social_dict.elements():
                                negative_social_weight = negative_social_weight + social_dict[t]/social_final_len
                
                    if negative_social_dummy + positive_social_dummy > 0:
                        x = x + 2
                                
                    x = x + 1
                
                
                #step 5: Aggregate total social discussions, forward-looking climate risk, historical climate risk, sentiment on climate issues           
                docu_tokens = clean_tokenize(docu)
                total_social_discuss= positive_social_weight + negative_social_weight
                total_social_points = positive_social_weight - negative_social_weight
                social_sentiment = (total_social_points) / len(docu_tokens)
                
                print('Total Discussion of Social Issues is: ' + str(total_social_discuss))
                print('Total Social Points is: ' + str(total_social_points) + ' points')
                print('Total Environmental Sentiment is: ' + str(social_sentiment))
                
                x=0
                positive_govern_weight=0
                negative_govern_weight=0

                while x < len(sentences)-2:
                    threesentences1 = sentences[x] + ' ' + sentences[x+1] + ' ' + sentences[x+2]
                    positive_govern_dummy=0
                    negative_govern_dummy=0
                    for pword in positive:
                        if pword in threesentences1:
                            positive_govern_dummy=1
                    for nword in negative:
                        if nword in threesentences1:
                            negative_govern_dummy=1
                        
                    if positive_govern_dummy==1:
                        #search for the words in the governance library
                        three_tokens1 = clean_tokenize(threesentences1)
                        for t in three_tokens1:
                            if t in governance_dict.elements():
                                positive_govern_weight = positive_govern_weight + governance_dict[t]/governance_final_len
                       
                    if negative_govern_dummy==1:
                        #search for the words in the governance library
                        three_tokens1 = clean_tokenize(threesentences1)
                        for t in three_tokens1:
                            if t in governance_dict.elements():
                                negative_govern_weight = negative_govern_weight + governance_dict[t]/governance_final_len
                
                    if negative_govern_dummy + positive_govern_dummy > 0:
                        x = x + 2
                                
                    x = x + 1
                
                
                #step 5: Aggregate total governance discussions, forward-looking climate risk, historical climate risk, sentiment on climate issues           
                docu_tokens = clean_tokenize(docu)
                total_govern_discuss= positive_govern_weight + negative_govern_weight
                total_govern_points = positive_govern_weight - negative_govern_weight
                govern_sentiment = (total_govern_points) / len(docu_tokens)
                
                print('Total Discussion of Governance Issues is: ' + str(total_govern_discuss))
                print('Total Governance Points is: ' + str(total_govern_points) + ' points')
                print('Total Governance Sentiment is: ' + str(govern_sentiment))
                
                #Step 6: Aggregate total ESG Points for the company
                
                total_ESG_points= total_enviro_points + total_social_points + total_govern_points
                total_ESG_discussion = total_enviro_discuss + total_social_discuss + total_govern_discuss
                total_ESG_sentiment = total_ESG_points /  total_ESG_discussion
                print('The total ESG sentiment for ' + str(filename) + ' is: ' + str(total_ESG_points))
                print('='*75)
                
docuanalyze('GM Annual Report FY19')
docuanalyze('FCA Annual Report FY19')
docuanalyze('Ford Annual Report FY19')