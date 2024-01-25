# German Embedding Dataset Generation 
Similar to the [intfloat/e5-mistral-7b-instruct](https://huggingface.co/intfloat/e5-mistral-7b-instruct) and the Paper "Improving Text Embeddings with Large Language Models" [ArXiv](https://arxiv.org/abs/2401.00368) a synthetic dataset should be generated. 
As of now we are only generating a dataset for retreival tasks with the following steps: 
1. Brainstorming Topics for such Retreival Tasks: Instead of the LLM asking to be creative, the tasks will be generated with the help of randomly sampled 5 topics from the quora dataset. An example for such topics and questions are:
```
topic: Heißwassererhitzer
questions:
["Suche nach Anleitungen zur Installation von Boilern",
"Finde Produktbeschreibungen von Heißwassererhitzern mit Energieffizenzklasse A.",
...
]
```
3. Generating Questions: The retreival quality can differ according to the style of the question. While short search strings were superior in short text chunks, questions were better for longer chunk sizes. We will be generating the following questions:
- Search String: short Keywords representing e.g. search engine interactions "example of IPv4 address in CIDR notation"
- Imperative Questions: Question formulated in imperative Form e.g. "Describe how to specify an IP address range using the IP-address and IP-mask fields."
- Question: standard Question e.g. "What is the difference between specifying an IP address range using the CIDR notation and using the IP-address and IP-mask fields?"
Examples:
```
Identifiziere Studien zur Bedeutung von Bildung für die persönliche Entwicklung
Imperative Form:  "Suche nach Studien, die die Bedeutung von Bildung für die persönliche Entwicklung untersuchen."
Question:  "Welche Studien gibt es zur Bedeutung von Bildung für die persönliche Entwicklung?"
Search String:  "Studien Bedeutung Bildung persönliche Entwicklung"
-----------------------------
Berichte über innovative Ansätze in der Medizinforschung und -praxis
Imperative Form:  "Finde Berichte über neue Ansätze in der Medizinforschung und -praxis."
Question:  "Wo kann ich Berichte über innovative Ansätze in der Medizinforschung und -praxis finden?"
Search String:  "Berichte innovative Ansätze Medizinforschung Praxis"
```
4. Generating the hard positive and hard negatie example: We have seen that variance here is also important! The generation will not just consist of the same structured text but will sample from predefined categories. 
