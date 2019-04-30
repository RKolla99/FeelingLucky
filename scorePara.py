from kmp import KMPSearch

def score(paragraph, searchphrase):
    searchphraseWord1, searchphraseWord2, searchphraseWord3 = searchphrase.split()
    score3 = KMPSearch(searchphrase, paragraph)
    score12 = KMPSearch(searchphraseWord1 + " " + searchphraseWord2, paragraph) - score3
    score23 = KMPSearch(searchphraseWord2 + " " + searchphraseWord3, paragraph) - score3
    score13 = KMPSearch(searchphraseWord1 + " " + searchphraseWord3, paragraph)    
    score1 = KMPSearch(searchphraseWord1, paragraph) + KMPSearch(searchphraseWord2, paragraph) + KMPSearch(searchphraseWord3, paragraph) - (3 * score3) - (2 * score12) - (2 * score23) - (2 * score13)
    score2 = score13 + (2 * (score12 + score23))
    return (score3, score2, score1)
