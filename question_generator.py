import requests

url = "https://question-generator.p.rapidapi.com/"

querystring = {"text":"Sensation - awareness resulting from the stimulation of a sense organ Perception - the organization and interpretation of sensations These work together seamlessly to help us experience the world. Our focus: the 6 senses: seeing, hearing, smelling, touching, tasting and monitoring the body's positions (proprioception) Transduction - the conversion of stimuli detected by receptor cells to electrical impulses that are then transported to the brain 5.1 We Experience Our World through Sensation Psychophysics - branch of psychology that studies the effects of physical stimuli on sensory perceptions and mental states - Founded by German psychologist Gustav Fechner (1801-1887) Studies relationship between strength of stimulus and a person's ability to detect it Absolute threshold of a sensation - the intensity of a stimulus that allows an organism to just barely detect it o a criterion to help determine the limits of human sensation Signal detection analysis - a technique used to determine the ability of the perceiver to separate true signals from background noise","nbr":"10"}

headers = {
    'x-rapidapi-key': "rapidapi-key",
    'x-rapidapi-host': "question-generator.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)