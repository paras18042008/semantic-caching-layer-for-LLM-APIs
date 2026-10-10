import time 

cache={}
hits=0
miss=0

def fake_llm(question):
    time.sleep(2)
    return "the answer=" + question

def ask_question(question):
    global hits,miss

    if question in cache:
        hits=+1
        return cache[question]
    
    miss+=1
    answer=fake_llm(question)
    cache[question]=answer
    return answer


questions = [
    "How do I reset my password?",
    "How do I reset my password?",
    "how do i reset mypassword",
    "I forgot my password, how can I change it?"
]

start = time.time()

for question in questions:
    answer=ask_question(question)
    print (answer)

    end = time.time()

print("\n--- Results ---")
print("Cache hits:", hits)
print("Cache misses:", miss)
print("Time taken:", round(end - start, 2), "seconds")
