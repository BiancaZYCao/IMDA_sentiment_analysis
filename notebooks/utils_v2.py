import os
import re
from praatio import textgrid

def decode_filename(file_path):
    """
    decode master data info from file name 
    like session index, speaker index, dialog type, etc.
    """
    session_id = file_path.split('/')[-1][4:8]
    speaker_id = file_path.split('/')[-1][9:13]
    speaker_type = 'agent' if speaker_id.startswith('00') else 'client'
    file_name = file_path.split('/')[-1]
    
    # Determine the dialog type based on the file name
    if 'bnk' in file_name:
        dialog_type = 'bank'
    elif 'tel' in file_name:
        dialog_type = 'telecom'
    elif 'ins' in file_name:
        dialog_type = 'insurance'
    else:
        dialog_type = 'unknown'

    return {
        'file_name': file_name,
        'session_id': session_id,
        'speaker_id': speaker_id,
        'speaker_type': speaker_type,
        'dialog_type': dialog_type,
        }

# decode_filename("../TextGrid_Scripts/app_0683_0013_phnd_cc-bnk.TextGrid")

def generate_sentences_from_intervals_v2(interval_entries, master_data):
    """ 
    Generate sentences from intervals by combining short phrases 
    and handling special markers like <S>. (rule-based)
    """
    combined_sentences = []
    temp_sentence = ''
    temp_x_min = None
    temp_x_max = None

    i = 0
    while i < len(interval_entries):
        current = interval_entries[i]
        temp_x_max = current.end
        temp_x_min = current.start
        if temp_x_min is None:
            temp_x_min = current.start

        if current.label in ['<B>','<Z>', '<S>', '']:
            i += 1
            continue
        temp_sentence = current.label.strip()
        combined_sentences.append({
            **master_data,
            'x_min': temp_x_min,
            'x_max': temp_x_max,
            'text': temp_sentence.strip()
        })
        i += 1
    return combined_sentences
    
def process_textgrid_file_to_sentences_v2(file_path: str, master_data: dict):
    """
    wrapper function to process the individual file
    """
    tg = textgrid.openTextgrid(file_path, False)
    current_tier = tg.getTier(tg.tierNames[0])
    current_tier_entries = current_tier.entries
    sentences = generate_sentences_from_intervals_v2(current_tier_entries, master_data)
    return sentences

# file_path_test = "../TextGrid_Scripts/app_0683_0013_phnd_cc-bnk.TextGrid"
# master_data_test = decode_filename(file_path_test)
# pd.DataFrame(process_textgrid_file_to_sentences(file_path,master_data_test))

