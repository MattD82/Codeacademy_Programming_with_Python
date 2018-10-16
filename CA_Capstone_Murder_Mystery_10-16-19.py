murder_note = """You may call me heartless, a killer, a monster, a murderer, but I'm still NOTHING compared to 
the villian that Jay was. This whole contest was a sham, an elaborate plot to shame the contestants and feed Jay's 
massive, massive ego. SURE you think you know him! You've seen him smiling for the cameras, laughing, joking, telling 
stories, waving his money around like a prop but off camera he was a sinister beast, a cruel cruel taskmaster, he 
treated all of us like slaves, like cattle, like animals! Do you remember Lindsay, she was the first to go, he called 
her such horrible things that she cried all night, keeping up all up, crying, crying, and more crying, he broke her 
with his words. I miss my former cast members, all of them very much. And we had to live with him, live in his home, 
live in his power, deal with his crazy demands. AND FOR WHAT! DID YOU KNOW THAT THE PRIZE ISN'T REAL? He never intended 
to marry one of us! The carrot on the stick was gone, all that was left was stick, he told us last night that we were 
all a terrible terrible disappointment and none of us would ever amount to anything, and that regardless of who won the 
contest he would never speak to any of us again! It's definitely the things like this you can feel in your gut how 
wrong he is! Well I showed him, he got what he deserved all right, I showed him, I showed him the person I am! I wasn't 
going to be pushed around any longer, and I wasn't going to let him go on pretending that he was some saint when all he 
was was a sick sick twisted man who deserved every bit of what he got. The fans need to know, Jay Stacksby is a vile 
amalgamation of all things evil and bad and the world is a better place without him."""

lily_trebuchet_intro = """Hi, I'm Lily Trebuchet from East Egg, Long Island. I love cats, hiking, and curling up under 
a warm blanket with a book. So they gave this little questionnaire to use for our bios so lets get started. What are 
some of my least favorite household chores? Dishes, oh yes it's definitely the dishes, I just hate doing them, don't 
you? Who is your favorite actor and why? Hmm, that's a hard one, but I think recently I'll have to go with Michael B. 
Jordan, every bit of that man is handsome, HANDSOME! Do you remember seeing him shirtless? I can't believe what he does 
for the cameras! Okay okay next question, what is your perfect date? Well it starts with a nice dinner at a delicious 
but small restaurant, you know like one of those places where the owner is in the back and comes out to talk to you and 
ask you how your meal was. My favorite form of art? Another hard one, but I think I'll have to go with music, music you 
can feel in your whole body and it is electrifying and best of all, you can dance to it! Okay final question, let's see, 
What are three things you cannot live without? Well first off, my beautiful, beautiful cat Jerry, he is my heart and 
spirit animal. Second is pasta, definitely pasta, and the third I think is my family, I love all of them very much and 
they support me in everything I do. I know Jay Stacksby is a handsome man and all of us want to be the first to walk 
down the aisle with him, but I think he might truly be the one for me. Okay that's it for the bio, I hope you have fun 
watching the show!"""

myrtle_beech_intro = """Salutations. My name? Myrtle. Myrtle Beech. I am a woman of simple tastes. I enjoy reading, 
thinking, and doing my taxes. I entered this competition because I want a serious relationship. I want a commitment. 
The last man I dated was too whimsical. He wanted to go on dates that had no plan. No end goal. Sometimes we would just 
end up wandering the streets after dinner. He called it a "walk". A "walk" with no destination. Can you imagine? I like 
every action I take to have a measurable effect. When I see a movie, I like to walk away with insights that I did not 
have before. When I take a bike ride, there better be a worthy destination at the end of the bike path. Jay seems 
frivolous at times. This worries me. However, it is my staunch belief that one does not make and keep money without 
having a modicum of discipline. As such, I am hopeful. I will now list three things I cannot live without. Water. 
Emery boards. Dogs. Thank you for the opportunity to introduce myself. I look forward to the competition."""

gregg_t_fishy_intro = """A good day to you all, I am Gregg T Fishy, of the Fishy Enterprise fortune. I am 37 years 
young. An adventurous spirit and I've never lost my sense of childlike wonder. I do love to be in the backyard 
gardening and I have the most extraordinary time when I'm fishing. Fishing for what, you might ask? Why, fishing for 
compliments of course! I have a stunning pair of radiant blue eyes. They will pierce the soul of anyone who dare gaze 
upon my countenance. I quite enjoy going on long jaunts through garden paths and short walks through greenhouses. I 
hope that Jay will be as absolutely interesting as he appears on the television. I find that he has some of the most 
curious tastes in style and humor. When I'm out and about I quite enjoy hearing tales that instill in my heart of 
hearts the fascination that beguiles my every day life. Every fiber of my being scintillates and vascillates with 
extreme pleasure during one of these charming anecdotes and significantly pleases my beautiful personage. I cannot wait 
to enjoy being on A Brand New Jay. It certainly seems like a grand time to explore life and love."""

def get_average_sentence_length(text):
	# Added in the "_" in order to preserve the original punctuation w/ respect to sentence length.
	sentence_punctuation_replaced = text.replace(".","._").replace("!", "!_").replace("?", "?_")
	
	# Split the paragraph into a list of sentences, remove any "\n", and remove leading whitespace.
	# I removed the leading whitespace so that the first sentence in a paragraph would not have one less character.
	sentences_split = sentence_punctuation_replaced.split("_")
	sentences_clean = []
	for sentence in sentences_split:
		sentences_clean.append(sentence.replace("\n", "").lstrip(" "))
	
	# Removing last list item that gets created since paragraph ends with puncuation. 
	# sentences_clean = list(filter(None, sentences_clean)) <<< alternate way to do this
	del sentences_clean[-1]
	# Create list of the lengths of each sentence, then sum those values, and return the average.
	list_of_sentence_lengths = []
	for sentence in sentences_clean:
		list_of_sentence_lengths.append(len(sentence))

	sum_of_lengths = 0	
	for value in list_of_sentence_lengths:
		sum_of_lengths += value

	return sum_of_lengths / len(list_of_sentence_lengths)

#print(get_average_sentence_length(murder_note))
#print(get_average_sentence_length(lily_trebuchet_intro))
#print(get_average_sentence_length(myrtle_beech_intro))
#print(get_average_sentence_length(gregg_t_fishy_intro))

def prepare_text(text):
	# Creates a clean list of all words in a block of text
	# Replace all puncuation so it's the same, then change all puncuation to spaces, remove extra spaces, convert to lowercase, 
	# remove line splits, and then split by space
	clean_word_list = text.replace("!", ".").replace("?", ".").replace(".", " ").replace("  ", " ").replace(",", "").lower().replace("\n", "").split(" ")
	del clean_word_list[-1]
	return clean_word_list

def build_frequency_table(corpus):
	frequency_table = {}
	for word in corpus:
		if word not in frequency_table:
			frequency_table[word] = 1
		else:
			frequency_table[word] += 1
	return frequency_table

def ngram_creator(text_list):
	list_of_ngrams = []
	for i in range(len(text_list)-1):
		list_of_ngrams.append(text_list[i] + " " + text_list[i + 1])
	return list_of_ngrams

def frequency_comparison(table1, table2):
	appearances = 0
	mutual_appearances = 0
	# Iterate through all keys in table 1, see if they are in table 2, and if so, compare the value in table 1 vs. value in table 2 for that key.
	for key in table1.keys():
		if key in table2.keys():
			# If the value in table 1 > value in table 2, add table 1 value to appearances (since it represents total overal appearances b/w the two)
			# and add table 2 value to mutual appearances. 
			if table1[key] >= table2[key]:
				appearances += table1[key]
				mutual_appearances += table2[key]
			# Reverse that if table 2 value > table 1 value
			else:
				appearances += table2[key]
				mutual_appearances += table1[key]
		# if table 1 key not in table 2, add table 1 value to appearances
		else:
			appearances += table1[key]
	# iterate through all table 2 keys not in table 1, and add those to appearances as well
	for key in table2.keys():
		if key not in table1.keys():
			appearances += table2[key]

	return mutual_appearances / appearances

def percent_difference(avg_length_1, avg_length_2):
	return abs(avg_length_1 - avg_length_2) / ((avg_length_1 + avg_length_2) / 2)

def find_text_similarity(TextSample1, TextSample2):
	# Calculate sentence length similarity
	sentence_length_difference = percent_difference(TextSample1.average_sentence_length, TextSample2.average_sentence_length)
	sentence_length_similarity = abs(1 - sentence_length_difference)

  # Calcualte word count similarity
	word_count_similarity = frequency_comparison(TextSample1.word_count_frequency, TextSample2.word_count_frequency)

  # Calculate ngram similarity
	ngram_similarity = frequency_comparison(TextSample1.ngram_frequency, TextSample2.ngram_frequency)
	# print(ngram_similarity)
	# print((sentence_length_similarity + word_count_similarity + ngram_similarity) / 3)
	return (sentence_length_similarity + word_count_similarity + ngram_similarity) / 3


class TextSample:
	def __init__(self, text, author):
	  self.raw_text = text
	  self.author = author

	  # Calculates average sentence length for the block of text
	  self.average_sentence_length = get_average_sentence_length(self.raw_text)
	  
	  # Creates a clean list of all words in a block of text
	  self.prepared_text = prepare_text(self.raw_text)

	  # Creates a word frequency table using the prepared text
	  self.word_count_frequency = build_frequency_table(self.prepared_text)

	  # Creates an ngram frequency table using the prepared text, ngram creator, and build freq table
	  self.all_ngrams = ngram_creator(self.prepared_text)
	  self.ngram_frequency = build_frequency_table(self.all_ngrams)
	    
	def __repr__(self):
		return "The author of this paragraph is '{author}', and their average sentence length is: {avg_length:.1f} characters.".format(author = self.author, avg_length = self.average_sentence_length)

murderer_sample = TextSample(murder_note, "The Murderer")
lily_sample = TextSample(lily_trebuchet_intro, "Lily Trebuchet")
myrtle_sample = TextSample(myrtle_beech_intro, "Myrtle Beech")
gregg_sample = TextSample(gregg_t_fishy_intro, "Gregg T Fishy")

# print(murderer_sample)
# print(lily_sample)
# print(myrtle_sample)
# print(gregg_sample)

test2 = find_text_similarity(murderer_sample, lily_sample)
test3 = find_text_similarity(murderer_sample, myrtle_sample)
test1 = find_text_similarity(murderer_sample, gregg_sample)
print(test2)
print(test3)
print(test1)

list_of_suspects = [lily_sample, myrtle_sample, gregg_sample]
print("""There are three contestants on 'A Brand New Jay' who could be the murderer!
Here are the similarity scores comparing their intro paragraphs vs. the murder letter:""")
for suspect in list_of_suspects:
	print("   {name} has a similarity score of: {score:.2f}".format(name = suspect.author, score = find_text_similarity(murderer_sample, suspect)))

print("The murderer is: {name}.".format(name = lily_sample.author))






