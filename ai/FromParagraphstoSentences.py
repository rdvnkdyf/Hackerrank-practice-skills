import sys
import re

def segment_sentences(text):
    """
    Splits a given text into sentences based on punctuation and common exceptions.

    Args:
        text (str): The input text to be segmented.

    Returns:
        list: A list of sentences.
    """
    # Define a list of common abbreviations to prevent false sentence breaks.
    # The regex will look for these followed by a period and a space.
    abbreviations = [
        'Dr', 'Mr', 'Mrs', 'Ms', 'Jr', 'Sr', 'Prof', 'Capt', 'Gen', 'Col', 'Sgt',
        'Maj', 'Rev', 'Ave', 'St', 'Rd', 'Blvd', 'Co', 'Corp', 'Inc', 'Ltd',
        'e.g', 'i.e', 'etc', 'p.m', 'a.m'
    ]
    # Create a regex pattern from the abbreviations list
    abbrev_pattern = '|'.join([re.escape(abbr) for abbr in abbreviations])
    
    # Use a regex to find all sentence-ending punctuation.
    # The regex looks for a period, question mark, or exclamation mark
    # followed by a space or a newline, but it tries to avoid matching
    # periods in common abbreviations.
    #
    # (?<!...): Negative lookbehind to ensure the period is not preceded by an abbreviation.
    # (?=[.?!]): Lookahead for a period, question mark, or exclamation mark.
    # \s+|$): Matches one or more spaces or the end of the string.
    
    # First, handle quoted sentences and other specific cases by normalizing them.
    # The input sample shows a quoted sentence ending with a question mark within the quote.
    # This regex attempts to find punctuation at the end of a sentence, but not
    # in the middle of a word or after an abbreviation.
    
    # The pattern:
    # (([.?!])\s+(?=[A-Z]|$)|([.?!])(?=\s*\"))
    # (?:[.?!]) : Matches a sentence-ending punctuation (., ?, !).
    # (?!['"A-Za-z0-9]) : Negative lookahead to ensure it's not followed by a quote, a letter, or a number.
    # This helps avoid splitting on abbreviations like Dr. or numbers like 1.5.
    
    sentences = re.split(r'(?<=[.?!])\s+(?=[A-Z"])|(?<=[.?!])(?=\s*")', text)
    
    # Filter out empty strings that can result from the split.
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # This approach is not perfect due to the complexity of the task, so let's
    # use a more robust tokenization library if available, but for a simple Python
    # solution, a rule-based regex is the most common approach. Let's try to refine the regex
    # for better results, based on the provided sample cases.

    # A more advanced regex to handle abbreviations and quotes better.
    # This pattern works by finding a period/question mark/exclamation point
    # that is NOT preceded by a common abbreviation.
    # It also handles the case of a period followed by a quote.
    
    # Find all potential sentence-ending markers
    # We will use a more controlled approach, replacing problematic points with a marker first,
    # then splitting on the others.
    
    # Replace periods in abbreviations with a placeholder
    temp_text = text
    temp_text = re.sub(r'(\b(' + abbrev_pattern + r')\.(\s|$))', r'\1_ABBR_PLACEHOLDER_', temp_text)
    
    # Split the text by '.', '!', or '?' if they are followed by a space and an uppercase letter,
    # or followed by a quote and an uppercase letter.
    raw_sentences = re.split(r'([.!?])\s+(?=[A-Z])|([.!?])(?=")', temp_text)
    
    final_sentences = []
    current_sentence = ""

    if raw_sentences:
        for i, segment in enumerate(raw_sentences):
            # Check for None values before calling string methods
            if segment is None:
                continue
            
            if segment.strip() in ['.', '?', '!']:
                current_sentence += segment.strip()
                # If we encounter a punctuation and the next segment starts with a quote,
                # combine them.
                if i + 1 < len(raw_sentences) and raw_sentences[i+1] and raw_sentences[i+1].startswith('"'):
                    current_sentence += raw_sentences[i+1]
                    raw_sentences[i+1] = "" # Clear the next part
                    
                final_sentences.append(current_sentence.strip())
                current_sentence = ""
            elif segment.startswith('"') and current_sentence:
                current_sentence += " " + segment.strip()
            elif segment:
                # Replace the placeholder back with a period
                segment = segment.replace('_ABBR_PLACEHOLDER_', '.')
                if current_sentence:
                    current_sentence += " " + segment.strip()
                else:
                    current_sentence = segment.strip()
        
    # Append the last sentence if it wasn't ended by punctuation
    if current_sentence:
        final_sentences.append(current_sentence.strip())

    # Final cleanup of extra spaces
    final_sentences = [re.sub(r'\s+', ' ', s.strip()) for s in final_sentences]
    
    # The provided sample output has a different behavior than simple split.
    # Let's use a simpler, more direct approach based on the sample.
    
    # The problem appears to want splits at . ? ! when they are followed by a space and a capital letter,
    # and also handle cases within quotes.
    
    # A simple but powerful regex approach:
    # Split the text by a period, question mark, or exclamation mark
    # that is followed by a space and a capital letter OR the end of the string.
    # Use a lookbehind to keep the punctuation with the sentence.
    
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z"\'(])', text)
    
    # Handle the "No!" case which is a sentence by itself.
    # A period or exclamation mark followed by a newline or end of string.
    # Also handle periods after initials, such as "W.".
    
    # Let's try this regex which is specifically crafted for the provided sample.
    # It handles periods, questions, and exclamations, and prevents splitting on common abbreviations.
    sentences = re.split(r'(?<![A-Z][a-z])(?<=[.!?])\s(?=[A-Z])|(?<=[.!?])(?=\s*")', text)
    
    # A more robust regex that handles both abbreviations and quote cases from the sample.
    # This pattern splits on .?! only if they are not preceded by a common single-letter initial
    # or an abbreviation like Dr. and are followed by a space and an uppercase letter.
    
    # Add a special case to handle the "No!" type of sentences.
    # We will first handle the "What good are they?..." quote example.
    # The entire quoted text is a single sentence. Let's find quotes and treat them as single units.
    
    # Let's go back to a simpler approach that is more likely to work for a variety of cases.
    
    sentences = re.findall(r'[^.!?]+[.!?]+(?:\s|$)|".*?"[.!?]+\s*', text)
    
    # The provided sample seems to have some tricky edge cases not covered by a single regex.
    # Let's use a more programmatic approach.

    current_sentence = ""
    result = []
    
    i = 0
    while i < len(text):
        char = text[i]
        current_sentence += char
        
        if char in ['.', '?', '!']:
            # Check for a space and a capital letter next, or end of string
            is_end_of_sentence = False
            
            if i + 1 >= len(text):
                is_end_of_sentence = True
            elif text[i+1] in [' ', '\n', '\t']:
                # Skip whitespace
                j = i + 1
                while j < len(text) and text[j].isspace():
                    j += 1
                
                if j < len(text) and text[j].isupper():
                    # It's a capital letter, so it's likely a new sentence.
                    is_end_of_sentence = True
                elif j >= len(text):
                    is_end_of_sentence = True
            
            # Check for exceptions
            if char == '.':
                # Check for abbreviations
                # This check is fragile. Let's use a simpler heuristic.
                # If the previous word is 1-2 letters, it's likely an abbreviation
                temp_words = current_sentence.strip().split()
                if len(temp_words) > 1 and len(temp_words[-1]) <= 3:
                    # It's a potential abbreviation, so don't split.
                    is_end_of_sentence = False
            
            # Handle quotes
            if char == '"' and current_sentence[-2] in ['.', '?', '!']:
                 # A quoted sentence end. This should be treated as a sentence break.
                 is_end_of_sentence = True

            if is_end_of_sentence:
                sentences.append(current_sentence.strip())
                current_sentence = ""
        
        i += 1
    
    if current_sentence:
        sentences.append(current_sentence.strip())

    return [s for s in sentences if s]

# Read input from stdin
input_text = sys.stdin.read().replace('\n', ' ')

# Get the segmented sentences
result = segment_sentences(input_text)

# Print each sentence on a new line
for sentence in result:
    print(sentence)
