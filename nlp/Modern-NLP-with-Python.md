# Modern NLP with Python (Udemy Course)

### Materials
Course curriculum, Colab toolkit and data links
Hi, and welcome to this modern NLP course! Here is a quick summary of the different parts of the course and the links to the Google Colab file for each application. Enjoy!

1. Introduction

2. CNN for NLP - Intuition

3. CNN for NLP - Application (sentimental analyser):
        Google Colab file: https://colab.research.google.com/drive/1sFa6yosp2bBoB19YLQ07jn_Ic1urU836
        Data link: http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip

4. Transformer - Intuition
        "Attention is all you need" paper: https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf

5. Transformer - Application (Eng - Fr translator):
        Google Colab file: https://colab.research.google.com/drive/1i4a26jVRVsAIfAGCe5pnl4l51B6GvjWs
        Data link: http://www.statmt.org/europarl/ for all pairs
    http://www.statmt.org/europarl/v7/fr-en.tgz for the En-Fr in the course
    https://drive.google.com/file/d/14wOcOrg8YJWXze6RvMy1cisDJKaFukff/view?usp=sharing for nonbreaking_prefix.en
    https://drive.google.com/file/d/1z4iM2n4t1guAxHZ0URfmzrjz3zknW64L/view?usp=sharing for nonbreaking_prefix_fr



### 2. CNN for NLP - Intuition
Process:
    - Convolution: Create feature detectors that parse thru the image
    - Max Pooling: reduce size anc cost by being more global
    - Flattening: flatten all matrices into 1D vector
    - Full Connection: standard FCN to learn classification task

Applying Process above done to images to text instead.
- Search for local features... in sentences.

We can do one-hot encoding, however, does not retain any information or relationship of words. "not" can exist in both and yet that meaning is lost in one-hot encoding of a 1-gram. e.g "not bad" and "not good" could be only differences in those 2 sentences but one-hot encoding would lose that meaning and label them incorrectly as "bad" and "good" respectively.

One Hot Encoding => Word Embedding (Better!)

- Differences in looking at TEXT vs IMAGES in CNN Matrices
- In images, going Top Down or L<-->R doesn't make a difference, all related, but for text, that's a different sentence as each sentence is 'i' row so it doesn't relate to row below in same way. So Top<-->Bottom would be a single sentence in NLP application of CNN and has meaning in n-gram models, e.g. 2, 3, 4, etc.

### Sentiment Analysis with NLP
- Data Sets: http://help.sentiment140.com/for-students


The most valuable thing you have in your life at any given moment is that moment and that moment is a measurement of time. Money, possessions, etc are all factors of time and can all be re-acquired given time. But you can't get your time back. 

If recruiters and managers are playing trivial pursuit or not disclosing the vision of the role and the problems they have to overcome for you and the company to be successful in that role -- it's going to feel like a tough job. 

If there's no learning, it's too easy. If there's no support or vision or focus it's going to be too hard to create something other than a big idea that puts wind behind a sale but can never be built.

