import re

def lowercase(text):
    text = text.lower()
    return text

def remove_punctuation(text):
    text = re.sub(r'[^\w\s]', '', text)
    return text
    
def strip_whitespace(text):
    text = re.sub(r'^\s+|\s+$', '', text)
    return text

def lemmatizer(cleaned_text):
    word_mapping = {
        "am": "be",
        "is": "be",
        "are": "be",
        "running": "run",
        "runs": "run",
        "children": "child",
        "mice": "mouse",
        "better": "good",
        "best": "good"
    }
    
    words = cleaned_text.split()
    
    lemmatized_words = []
    for word in words:
        if word in word_mapping:
            lemmatized_words.append(word_mapping[word])
        else:
            lemmatized_words.append(word)
    
    return ' '.join(lemmatized_words)
    
def remove_stop_word(cleaned_text):
    
    #debug
    if cleaned_text is None:
        return ""
        
    words = cleaned_text.split()
    
    stop_words = {"the", "is", "on", "a", "an", "and", "or", "but", "in"}
    
    filtered_words = []
    for word in words:  
        if word.lower() not in stop_words: 
            filtered_words.append(word)
    

    joined_words = ' '.join(filtered_words)  
    return joined_words
    
    
    

def token_categorizer(text):
    if text.isalpha():
        return 'word'
    
    elif text.isnumeric():
        return 'number'
    
    elif '@' in text:
        return 'email'
    
    return text
    
    
def token_processor(cleaned_text):
    removed_stop_words = remove_stop_word(cleaned_text)
    
    lemmatization = lemmatizer(removed_stop_words)
    
    processed_token = lemmatization
    
    return processed_token

#---------significant components----------
def clean_text(text):
    lowercase_text = lowercase(text)
        
    none_punctuation_text = remove_punctuation(lowercase_text)
        
    stripped_whitespace_text = strip_whitespace(none_punctuation_text)
    
    cleaned_text = stripped_whitespace_text
    
    return cleaned_text


    

def split_into_words(text):
    token_categories = token_categorizer(text)
    
    print(token_categories)
    
    token_processing = token_processor(token_categories)
    
    return token_processing



if __name__ == '__main__':
    text = 'The children are running, and mice are better than before'
    cleaned_text = clean_text(text)
    print("After cleaning:", cleaned_text)
    splitted_text = split_into_words(cleaned_text)
    print("Final result:", splitted_text)
    

        
        
        
        
        
        
        
        
        