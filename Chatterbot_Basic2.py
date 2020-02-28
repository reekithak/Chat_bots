#!/usr/bin/env python
# coding: utf-8

# CHAT2BOT .....

# In[30]:


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


# In[31]:


my_bot = ChatBot(name='TestBot2', read_only=False,
                 logic_adapters=['chatterbot.logic.BestMatch'])



# In[ ]:
def responder2(k):
    x=my_bot.get_response(k)
    print(x)  
    

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')

x='a'
while(x!='q'):

    print("Enter q to quit after the initial Response!")
    k=input("Enter Your query!")
    if(k!='q'):
        responder2(k)
    else:

        exit()
            


    


