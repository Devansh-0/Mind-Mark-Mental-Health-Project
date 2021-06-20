mean_score=1
def modelFile(LIST):

    import os
    os.environ["EAI_USERNAME"] = "devansh.sharma110@gmail.com"
    os.environ["EAI_PASSWORD"] = 'Devansh170501!'


    from expertai.nlapi.cloud.client import ExpertAiClient
    client = ExpertAiClient()

    processData= LIST #Declaring crucial variables
    sum= 0
    
    for i in processData:
        
        output = client.specific_resource_analysis(
            body={"document": {"text": i}}, 
            params={'language': 'en', 'resource': 'sentiment'})
        print("sentiment:", output.sentiment.overall)
        sum= sum+ output.sentiment.overall
    mean_score= sum/len(LIST)
    mean_score= round(mean_score,2)
    return mean_score

def impTopics(LIST):
    import os
    os.environ["EAI_USERNAME"] = "devansh.sharma110@gmail.com"
    os.environ["EAI_PASSWORD"] = 'Devansh170501!'

    processData= LIST 
    elements = ''
    for element in LIST:
        elements += str(element)
    print(elements)

    from expertai.nlapi.cloud.client import ExpertAiClient
    client = ExpertAiClient()

    language= 'en'
    for i in processData:
        output = client.specific_resource_analysis(body={"document": {"text":elements}}, params={'language': language, 'resource': 'relevants'})
        for lemma in output.main_lemmas:
            print(lemma.value)
            return(lemma.value)
    

  