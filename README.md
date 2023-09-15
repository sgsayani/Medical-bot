# An AI-Based Medical Chatbot Model for Infectious Disease Prediction

This project aims to demonstrate how chatbots can be effectively used in the medical sector to prevent the spread of infectious diseases. By raising awareness among users, we can provide them with accurate medical solutions to help them stay healthy. We developed a preliminary training model and conducted a study to improve human interaction with databases in 2021. Through natural language processing, we analyzed human behavior and characteristics in chatbots. Our proposed AI Chatbot interaction and prediction model utilizes a deep feedforward multilayer perceptron. We discovered a lack of theoretical guidelines and practical recommendations for creating AI chatbots for lifestyle improvement programs. In this paper, we provide a brief comparison of our proposed model's time complexity and testing accuracy. Our study achieved a minimum loss of 0.1232 and a highest accuracy of 94.32%. We discuss the functionalities and possible applications of medical chatbots and the challenges that come with using these emerging technologies during health crises, especially pandemics. We hope that our findings will provide researchers with a better understanding of medical chatbot functionality and help improve their applications. This will be crucial in preventing the spread of diseases such as COVID-19.

# INDEX TERMS:  Artificial intelligence, chatbot, LSTM algorithm, machine learning, natural language processing, query processing.

# Screenshot of the project: 
![shah20-3227208-large](https://github.com/sgsayani/Medical-bot/assets/71175346/11397b19-d35b-40a2-80ed-250824474f11)
![shah13-3227208-large](https://github.com/sgsayani/Medical-bot/assets/71175346/34f4c40b-93bb-4747-a30e-674fe424b11c)

# Algorithm :
Algorithm 1 Pseudocode of the Proposed Chatbot System<br>
Step 1:<br>
Make a json file along with tags, patterns and response. Here, tags will represent the group, patterns represent the question or query format of the user and the response represents how the bot will respond.<br>

Step2: <br>
load json file, intents =json.loads(open(‘intents.json’).read()<br>

Step3:<br>
ignore unnecessary letters, ignore_letters= [‘?’,’!’]<br>
step 4:<br>
Store each word of patterns and tags, lemmatize them.<br>
```
words=[lemmatizer.lemmatize(‘‘word’’) for
word in words if word is not in ignore_letters]
```
Step 5:<br>
sorts the words for not repeating the same word in model, words=sorted(set(words))<br>
Step 6:<br>
open the files in binary mode and make dump file for it,<br>
```
pickle.dump(words, open(‘words.pk1’, ’wb’))
pickle.dump(words, open(‘class.pk1’,’wb’))
```
Step7:<br>
add all words, patterns after lemmatizing, to training<br>
```
list training= [], empty list<br>
word_patterns=[lemmatizer.lemmatize(‘‘word.lower’’()) for
word in word_patterns], for lemmatizing Loop : word in<br>
words list -:(will take each element from words list to word)
bag.append(1) if word in word_patterns or if it is not in
word_patterns, bag append the value of ‘‘0’’
output_Row=list of output empty, list(output_empty)
output_Row of classes.index of documents=1
training.append(list of bag and output_Row)
```
Step 8: <br>
shuffle all words in training list, random.shuffle(training)<br>
step 9:<br>
store training list one part to train_x and another part to train_y<br>
```
train_x=stores list one part,0th index elements, list (:0)
train_y=stores 1st index elements, list (:1)
```
Step 10:<br>
make neural networking by adding Dense and dropout to model<br>
```
model=linear stack of layers
model.add(Dense of (128 and train_x))
model. add (Dropout of 0.6)
sequential () model. Add (Dense of (train_y[0])’s length)
```
Step 11:<br>
compile it and save the model<br>
```
Compile (model, for compiling)
Fit the model, model.fit()
```
Save it as.h5 file, save(chatbot_model.h5)<br>
Step 12:<br>
after successfully making the training model whenever a user writes the text on the chatbox, the text will be Prediction (message or text)<br>
step 13:<br>
give reply to the users<br>
```
response = chatbot_response for the message
chatbot.insert (inserting the ‘‘response’’ to chatbot interface)
```
Step 14:<br>
if the user wants to hear it on voice also<br>
```
engine = pyttsx.init()
engine.say(command)
engine.runAndWait()
```
Where the command is the bot’s reply, which is converted into the voice<br>
step 15:<br>
this cycle will continue until the users press exit button<br>
step 16:<br>
if the user presses the exit button, the application will close<br>
