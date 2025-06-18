def get_words(str):
    new=str.split()
    return len(new)

def no_of_time(text):
    lower=text.lower()
    
    dict = {}
    for char in lower:
         dict[char]=dict.get(char,0)+1
    return dict

def sort_on(dict):
    return dict["num"]

def sorted_dict(dictionary):
    sorted=[]
    for character in dictionary:
        nom=dictionary[character]
        combined_dict={}
        if character.isalpha():
            combined_dict["char"]=character
            combined_dict["num"]=nom            
            sorted.append(combined_dict)
    sorted.sort(reverse=True,key=sort_on)
    
   
    return sorted