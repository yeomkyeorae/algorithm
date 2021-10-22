def changeToAkbo(akbos, m):
    new_m = ''
    for ix, ch in enumerate(m):
        if ch == '#':
            continue
        if ix < len(m) - 1 and m[ix + 1] == '#':
            ch += '#'
        new_m += akbos[ch]
    return new_m


def getMinutes(start, end):    
    start_hour, start_minute = start.split(':')
    end_hour, end_minute = end.split(':')
    
    start_hour = int(start_hour)
    start_minute = int(start_minute)
    end_hour = int(end_hour)
    end_minute = int(end_minute)
    
    if start_hour == end_hour:
        return end_minute - start_minute
    
    if end_minute < start_minute:
        return (end_hour - start_hour - 1) * 60 + (end_minute + 60 - start_minute)
    else:
        return (end_hour - start_hour) * 60 + (end_minute - start_minute)
    

def make_full_akbo(minutes, akbo):
    while len(akbo) < minutes:
        akbo += akbo
    return akbo[:minutes]
    

def solution(m, musicinfos):
    answer = ''

    akbos = {
        'C': 'A',
        'C#': 'B',
        'D': 'C',
        'D#': 'D',
        'E': 'E',
        'F': 'F',
        'F#': 'G',
        'G': 'H',
        'G#': 'I',
        'A': 'J',
        'A#': 'K',
        'B': 'L',
        'E#': 'M'
    }
    
    m = changeToAkbo(akbos, m)
    m_length = len(m)
    
    candidate_answer = []
    for info in musicinfos:
        start, end, music_name, akbo = info.split(',')
        play_minutes = getMinutes(start, end)
        akbo = changeToAkbo(akbos, akbo)
        
        full_akbo = make_full_akbo(play_minutes, akbo)
        if m in full_akbo:
            candidate_answer.append([play_minutes, music_name])
            
    if not len(candidate_answer):
        return "(None)"
    else:
        max_play_minutes = 0
        for c in candidate_answer:
            if c[0] > max_play_minutes:
                max_play_minutes = c[0]
                answer = c[1]
    
    return answer