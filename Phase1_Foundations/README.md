### Phase 1: Foundations of Multilingual NLP

- This phase establishes the foundational methods and analytical perspective required for research in natural language processing, with an emphasis on cross-linguistic variation. The primary objective is to implement and evaluate core classical NLP techniques—language modeling, part-of-speech tagging, and syntactic parsing—across three typologically distinct languages: German, French, and Russian, using datasets from Universal Dependencies.

- The structure of this phase deliberately assigns a different language to each task: German for statistical language modeling, French for part-of-speech tagging, and Russian for syntactic parsing. This design is intended to surface language-specific challenges early in the learning process, such as compounding and sparsity in German, morphological agreement and contraction in French, and free word order and case marking in Russian. By decoupling tasks and languages, the phase encourages the development of comparative intuition and prevents overreliance on assumptions derived from English-centric NLP.

- The expected learning outcomes include: 

    1) A solid understanding of probabilistic and rule-based approaches to core NLP problems.

    2) Experience working with linguistically annotated corpora in CoNLL-U format. 

    3) the ability to implement baseline models such as n-grams, Hidden Markov Models, and context-free grammar parsers. 

    4) The development of research-oriented practices, including reproducible experimentation, systematic logging, and critical analysis of results.

- The expected outcome of Phase 1 is a set of fully implemented baseline models for each task, accompanied by quantitative evaluations and qualitative language-aware analysis. Additionally, this phase culminates in a comparative reflection across languages and methods, highlighting how linguistic structure impacts model performance. This foundation prepares the transition to neural methods and multilingual representation learning in subsequent phases, while establishing a research mindset aligned with work presented at venues such as ACL and EMNLP.