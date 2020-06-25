from cc_markov import MarkovChain
import fetch_data

mc = MarkovChain()
mc.add_file('musician-bio.txt')

result = mc.generate_text(50)

result = ' '.join(result)

print("Your favourite musician...")
print("..."+result+"...")
