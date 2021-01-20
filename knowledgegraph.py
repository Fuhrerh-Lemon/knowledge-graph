## ********** FuhrerhLemon ********* ##
import spacy
import networkx as nx
from spacy.lang.es import Spanish
import matplotlib.pyplot as plt

nlp_model = spacy.load('es_core_news_sm')

def ObtenerFrases(text):
    nlp = Spanish()
    nlp.add_pipe(nlp.create_pipe('sentencizer'))
    documento = nlp(text)
    return [sent.string.strip() for sent in documento.sents]

def ImprimirToken(token):
    print(token.text, "->", token.dep_)

def Fragmentos(original, chunk):
    return original + ' ' + chunk

def Relacion(token):
    deps = ['ROOT', 'adj', 'attr', 'agent', 'amod']
    return any(subs in token.dep_ for subs in deps)

def Construccion(token):
    deps = ['compound', 'prep', 'conj', 'mod']
    return any(subs in token.dep_ for subs in deps)

def ProcesoPares(tokens):
    subjecto = ''
    object = ''
    relacion = ''
    ConstruccionSujeto = ''
    objetoSujeto = ''
    for token in tokens:
        # Imprimiendo los tokens, para ver como los relaciona
        ImprimirToken(token)

        if 'punct' in token.dep_:
            continue

        if Relacion(token):
            relacion = Fragmentos(relacion, token.lemma_)

        if Construccion(token):
            if ConstruccionSujeto:
                ConstruccionSujeto = Fragmentos(ConstruccionSujeto, token.text)
            if objetoSujeto:
                objetoSujeto = Fragmentos(objetoSujeto, token.text)

        if 'subj' in token.dep_:
            subjecto = Fragmentos(subjecto, token.text)
            subjecto = Fragmentos(ConstruccionSujeto, subjecto)
            ConstruccionSujeto = ''

        if 'obj' in token.dep_:
            object = Fragmentos(object, token.text)
            object = Fragmentos(objetoSujeto, object)
            objetoSujeto = ''

    #print (subject.strip(), ",", relation.strip(), ",", object.strip())
    return (subjecto.strip(), relacion.strip(), object.strip())

def Proceso(sentence):
    tokens = nlp_model(sentence)
    return ProcesoPares(tokens)

def MostrarGrafo(triples):
    G = nx.Graph()
    for triple in triples:
        G.add_node(triple[0])
        G.add_node(triple[1])
        G.add_node(triple[2])
        G.add_edge(triple[0], triple[1])
        G.add_edge(triple[1], triple[2])

    pos = nx.spring_layout(G)
    plt.figure()
    nx.draw(G, pos, edge_color = 'black', width = 1, linewidths = 1,
            node_size = 500, node_color = 'seagreen', alpha = 0.9,
            labels = {node: node for node in G.nodes()})
    
    plt.savefig('KnowledgeGraph.jpg')

def main(text):
    frases = ObtenerFrases(text)

    triples = []
    for frase in frases:
        triples.append(Proceso(frase))

    MostrarGrafo(triples)