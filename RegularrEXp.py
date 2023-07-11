import re

str="""Death Note (stylized in all caps) is a Japanese manga series written by Tsugumi Ohba and illustrated by Takeshi Obata. It was serialized in Shueisha's shōnen manga magazine Weekly Shōnen Jump from December 2003 to May 2006, with its 108 chapters collected in 12 tankōbon volumes. The story follows Light Yagami, a teen genius who discovers a mysterious notebook: the "Death Note", which belonged to the shinigami Ryuk, and grants the user the supernatural ability to kill anyone whose name is written in its pages. The series centers around Light's subsequent attempts to use the Death Note to carry out a worldwide massacre of individuals whom he deems immoral and to create a crime-free society, using the alias of a god-like vigilante named "Kira", and the subsequent efforts of an elite Japanese police task force, led by enigmatic detective L, to apprehend him.

A 37-episode anime television ai aiaiiaia series adaptation, produced by Madhouse and directed by Tetsurō Araki, was broadcast on Nippon Television from October 2006 to June 2007. A light novel based on the series, written by Nisio Isin, was also released in 2006. Additionally, various video games have been published by Konami for the Nintendo DS. The series was adapted into three live action films released in Japan in June 2006, November 2006, and February 2008, and a television drama in 2015. A miniseries titled Death Note: New Generation and a fourth film were released in 2016. An American film adaptation was released exclusively on Netflix in August 2017 and a sequel is reportedly in the works."""

# a=re.compile(r'\n')
# a=re.compile(r'Death')
# a=re.compile(r'.')
a=re.compile(r'^Muskan')
a=re.compile(r'works$')
a=re.compile(r'ai*')
a=re.compile(r'ai+')
a = re.compile(r'(ai){1}')
a = re.compile(r'ai{1}|Death')



# Special Sequences
a = re.compile(r'Fax\b')
a = re.compile(r'27\b')
a = re.compile(r'\d{5}-\d{4}')

m=a.finditer(str)

for value in m:
    print(value)
