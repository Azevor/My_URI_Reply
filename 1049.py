'''
In this problem, your job is to read three Portuguese words. These words
define an animal according to the table below, from left to right.
After, print the chosen animal defined by these three words.
'''

m_Animals = {
    'vertebrado': {
        'ave': {
            'carnivoro': 'aguia',
            'onivoro': 'pomba',
        },
        'mamifero': {
            'onivoro': 'homem',
            'herbivoro': 'vaca',
        },
    },
    'invertebrado': {
        'inseto': {
            'hematofago': 'pulga',
            'herbivoro': 'lagarta',
        },
        'anelideo': {
            'hematofago': 'sanguessuga',
            'onivoro': 'minhoca',
        },
    },
}

m_Subphylum = input().lower()
m_Class = input().lower()
m_Group = input().lower()

print(m_Animals[m_Subphylum][m_Class][m_Group])
