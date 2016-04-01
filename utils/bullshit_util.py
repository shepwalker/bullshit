import re


def get_bullshit_count(text, bullshit_list):
    bullshit_count = {}
    for line in text:
        split_text = re.findall(r"[\w']+|[.,!?;]", line)
        for idxI, i in enumerate(split_text):
            for idxJ, j in enumerate(bullshit_list):
                this_split_bullshit = j.split()
                idxIprime = idxI
                for idxK, k in enumerate(this_split_bullshit):
                    if split_text[idxIprime] == this_split_bullshit[idxK]:
                        if idxK == len(this_split_bullshit) - 1:
                            if j in bullshit_count:
                                bullshit_count[j] = bullshit_count[j] + 1
                            else:
                                bullshit_count[j] = 1
                        else:
                            idxIprime += 1
                    else:
                        break
    return bullshit_count

def get_word_count(text):
    count = 0
    for line in text:
        count += len(line.split())
    return count