# -*- coding: utf-8 -*-

#Importing all dependencies
from requests.models import to_native_string


# def ABC(text1):
#     import os
#     os.environ["EAI_USERNAME"] = "devansh.sharma110@gmail.com"
#     os.environ["EAI_PASSWORD"] = 'Devansh170501!'


#     from expertai.nlapi.cloud.client import ExpertAiClient
#     client = ExpertAiClient()

#     list= [] #Declaring crucial variables
#     sum= 0

#     text=(text1)
#     print(type(text1))
    
#     output = client.specific_resource_analysis(
#             body={"document": {"text": text}}, 
#             params={'language': 'en', 'resource': 'sentiment'})
#     m= output.sentiment.overall
#     return m
 
def impTopics():
    import os
    os.environ["EAI_USERNAME"] = "devansh.sharma110@gmail.com"
    os.environ["EAI_PASSWORD"] = 'Devansh170501!'
    text= "I feel sad because my dog died. It was rough on me. I feel sometimes my emotions are being undermined. I dont do well in school as well."
    from expertai.nlapi.cloud.client import ExpertAiClient
    client = ExpertAiClient()
    language= 'en'
    output = client.specific_resource_analysis(body={"document": {"text": text}}, params={'language': language, 'resource': 'relevants'})

    for lemma in output.main_lemmas:
        return(lemma.value)



# #Input Section

# # language= input()
# age= input("Are you 18 years or older?(type y or n)")


# print("\nPlease answer the following questions. Be as descriptive as possible\n")

# if(age=='y'):

#     text1= input("aRE YOU OK?\n")
#     list.append(text1)

#     text2= input('''\n How frequently have you had little pleasure or interest in the activities you usually enjoy? Would you tell me more?\n''')
#     list.append(text2)

#     text3= input('''How often during the past X months have you felt as though your moods, or your life, were under your control?\n''')
#     list.append(text3)

#     text4= input('''How often have you felt as though the future was bleak, over the past few weeks?\n''')
#     list.append(text4)

#     print(len(list))

# else:
    
#     text1= input("Is something making you scared?")
#     list.append(text1)

#     text2= input("Do you have any problem paying attention?")
#     list.append(text2)

#     text3= input("What are you doing during recess? Who are you spending time with?")
#     list.append(text3)
#     print(len(list))

# #Output analysis

# for i in list:

#     output = client.specific_resource_analysis(
#         body={"document": {"text": i}}, 
#         params={'language': 'en', 'resource': 'sentiment'})
#     print("sentiment:", output.sentiment.overall)
#     sum= sum+ output.sentiment.overall
# print(sum)


# mean_score= sum/len(list)
# print(mean_score)





      