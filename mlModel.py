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
    print("Process data: ", *processData)

    
    text = ''.join(processData)
    print("Final Text: ", text)

    from expertai.nlapi.cloud.client import ExpertAiClient
    client = ExpertAiClient()

    language= 'en'
    
    output = client.specific_resource_analysis(body={"document": {"text": text}}, params={'language': language, 'resource': 'relevants'})


# Main lemmas
    x=[]
    print("Main lemmas:")

    for lemma in output.main_lemmas:
        print(lemma.value)
        
        x.append(lemma.value)
    print(*x)
    return x

  