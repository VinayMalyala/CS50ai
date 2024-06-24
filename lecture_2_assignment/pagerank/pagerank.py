import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    p = dict()
    for c in corpus:
        if corpus[c] == set():
            for cc in corpus:
                corpus[c].add(cc)
        if c == page:
            for cc in corpus:
                p[cc] = float((1-damping_factor) / len(corpus))
                if cc in corpus[c]:
                    p[cc] += float(damping_factor/len(corpus[c]))
    return p


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    p = dict()
    for c in corpus:
        p[c] = 0
    if n >= 1:
        page = random.choice(list(corpus.keys()))
        p[page] = int(p[page]) + 1

    for i in range(n-1):
        c = transition_model(corpus, page, damping_factor)
        page = random.choices(list(c.keys()), list(c.values()))[0]
        p[page] = int(p[page]) + 1
    for x in p:
        p[x] = float(p[x])/n
    return p


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    p = dict()
    numLinks = dict()
    for c in corpus:
        if corpus[c] == set():
            for cc in corpus:
                corpus[c].add(cc)
    for c in corpus:
        p[c] = 1/len(corpus)
        numLinks[c] = len(corpus[c])

    previous = list(p.values())
    needchange = True
    while needchange:
        needchange = False
        for i in p:
            add = 0
            for j in corpus:
                for k in corpus[j]:
                    if k == i:
                        add += damping_factor*p[j]/numLinks[j]
            p[i] = ((1-damping_factor)/len(corpus)) + add
        for x in range(len(previous)):
            diff = previous[x] - list(p.values())[x]
            if diff < -0.001 or diff > 0.001:
                needchange = True
        previous = list(p.values())
        if needchange == False:
            break

    return p


if __name__ == "__main__":
    main()
