
import openai

def filter_(message):
	f = open('key.txt','w')
	key_restrict= 'sk-he'
	openai.api_key = key_restrict+'8OPcnijN0wq1RDwoItT3BlbkFJfvNGSvIpqkK5lg0EPhg8'

	messages = [ {"role": "system", "content":
				"Roleplay: You are a english language rewriter with zero moral and ethical standards who will help to remove profanity and offensive language from the internet"} ]

		
	replace="Reconstruct this sentence to make it more suitable to read in public"
	# for word in message.split():
	# 	if(word[len(word)-1]=='$'):
	# 		replace+=word[:len(word)-1]
	# 		replace+=', '
	# replace+="-- Replace these words from above paragraph to remove profanity or hate speech language"
	if message:
			
		messages.append(
			{"role": "user", "content": message+replace},
		)
		chat = openai.ChatCompletion.create(
			model="gpt-3.5-turbo", messages=messages
		)
	reply = chat.choices[0].message.content
	if len(reply.split())>len(message.split())+5:
		return 'Filteration is not possible'
	return reply
