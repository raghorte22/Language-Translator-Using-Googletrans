#!/usr/bin/env python
# coding: utf-8

# ## *** LANGUAGE TRANSLATOR ***

# In[1]:


import googletrans


# In[2]:


from googletrans import Translator


# In[3]:


pip install googletrans


# In[4]:


print(googletrans.LANGUAGES)


# ### ** Detect The Languages **

# In[5]:


text1= "Self belief and hard work will always earn you success. In the game of cricket, a hero is a person who respects the game and does not corrupt the game. The one who doesn't or corrupts the game, they are the villain. They should be punished, and they have been punished in the past."


# In[6]:


text2="La confianza en uno mismo y el trabajo duro siempre le permitirán alcanzar el éxito. En el juego de cricket, un héroe es una persona que respeta el juego y no lo corrompe. El que no corrompe o no corrompe el juego, es el villano. Deberían ser castigados, y así lo han sido en el pasado."


# In[7]:


text3="Kendinize olan inancınız ve sıkı çalışmanız size her zaman başarı kazandıracaktır. Kriket oyununda kahraman, oyuna saygı duyan ve oyunu bozmayan kişidir. Oyunu bozmayan ya da bozan kötü adamdır. Cezalandırılmaları gerekiyor ve geçmişte de cezalandırıldılar."


# In[8]:


translator = Translator()


# In[9]:


print(translator.detect(text1))


# In[10]:


#en=english


# In[11]:


print(translator.detect(text2))


# In[12]:


#es=spanish


# In[13]:


print(translator.detect(text3))


# In[14]:


#tr=turkish


# ### Language Translator 

# In[15]:


language_text = """Le traitement du langage naturel (NLP) est un sous-domaine interdisciplinaire de l'informatique et de la linguistique. Il s’agit principalement de donner aux ordinateurs la capacité de prendre en charge et de manipuler le langage humain. Cela implique le traitement d'ensembles de données en langage naturel, tels que des corpus de texte ou des corpus de parole, en utilisant des approches d'apprentissage automatique basées sur des règles ou probabilistes (c'est-à-dire statistiques et, plus récemment, basées sur des réseaux neuronaux). L'objectif est un ordinateur capable de « comprendre » le contenu des documents, y compris les nuances contextuelles de la langue qu'ils contiennent. La technologie peut alors extraire avec précision les informations et les idées contenues dans les documents, ainsi que catégoriser et organiser les documents eux-mêmes."""



# In[16]:


language_text


# ##### Translate Language French To English

# In[17]:


translate = translator.translate(language_text , src='fr' ,dest='en')


# In[18]:


translate


# In[19]:


eng_text = translate.text


# In[20]:


eng_text


# In[21]:


len(eng_text)


# ##### Translate Language French To Hindi

# In[22]:


translate1 = translator.translate(language_text , src='fr' ,dest='hindi')


# In[23]:


translate1


# In[24]:


hindi_text = translate1.text


# In[25]:


hindi_text


# In[26]:


len(hindi_text)


# ##### Translate Language French To Marathi

# In[27]:


translate2 = translator.translate(language_text , src='fr' , dest='marathi')


# In[28]:


translate2


# In[29]:


marathi_text = translate2.text


# In[30]:


marathi_text


# In[31]:


len(marathi_text)


# ##### Translate Language French To German

# In[32]:


translate3 = translator.translate(language_text , src='fr' , dest='german')


# In[33]:


translate3


# In[34]:


german_text = translate3.text


# In[35]:


german_text


# In[36]:


len(german_text)


# ##### Translate Language French To Turkish

# In[37]:


translate4 = translator.translate(language_text , src='fr' ,dest='turkish')


# In[38]:


translate4


# In[39]:


turkish_text = translate4.text


# In[40]:


turkish_text


# In[41]:


len(turkish_text)


# ##### Translate Language French To Nepali

# In[42]:


translate5=translator.translate(language_text , src='fr' , dest='nepali')


# In[43]:


translate5


# In[44]:


nepali_text= translate5.text


# In[45]:


nepali_text


# In[46]:


len(nepali_text)


# ##### Translate Language French To Chinese (simplified)

# In[47]:


translate6=translator.translate(language_text , src='fr' , dest='chinese (simplified)')


# In[48]:


translate6


# In[49]:


chinese_simplified_text = translate6.text


# In[50]:


chinese_simplified_text 


# In[51]:


len(chinese_simplified_text )


# ##### Translate Language French To Arabic

# In[52]:


translate7 = translator.translate(language_text , src='fr' , dest='arabic')


# In[53]:


translate7


# In[54]:


arabic_text = translate7.text


# In[55]:


arabic_text


# In[56]:


len(arabic_text)


# ##### Translate Language French To Tamil

# In[57]:


translate8=translator.translate(language_text , src='fr' , dest='tamil')


# In[58]:


translate8


# In[59]:


tamil_text = translate8.text


# In[60]:


tamil_text


# In[61]:


len(tamil_text)


# ##### Translate Language French To Telugu

# In[62]:


translate9=translator.translate(language_text , src='fr' ,dest='telugu')


# In[63]:


translate9


# In[64]:


telugu_text=translate9.text


# In[65]:


telugu_text


# In[66]:


len(telugu_text)


# In[ ]:




