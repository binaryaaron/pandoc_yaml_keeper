# pandoc_yaml_keeper

I had a simple problem: I wanted to use Pandoc as a markdown converter for
Jekyll but things weren't playing well together with my template - I needed a
simple way to keep the YAML front matter in the output file from Pandoc. This
program does just that, using the pypandoc library to run pandoc and the pyyaml
package to work with the yaml front matter in a post. 

A post like this:

```{.markdown}
---
layout: post
title:  "wicked awesome blog post"
date:   2015-03-04
categories:
tags: []
published: true
excerpt: ""
description: "something"
comments: true
bibliography: ../sitebib.bib
---

## Section

See [@fenner2012a, @scikit-learn] or @ANEW.

Inline Math: $\sum_{i}^{n_i}$

display math:

$$
x | x \in \{0,1\}
$$

# References
```

Is correctly converted as this:

```{.html}
---
bibliography: ../sitebib.bib
categories: null
comments: true
date: 2015-03-04
description: something
excerpt: ''
layout: post
published: true
tags: []
title: 'wicked awesome blog post'
---

<h2 id="section">Section</h2>
<p>See <span class="citation" data-cites="fenner2012a">(Fenner 2012, <span class="citation" data-cites="scikit-learn">Pedregosa et al. (2011)</span>)</span> or <span class="citation" data-cites="ANEW">Nielsen (2011)</span>.</p>
<p>Inline Math: <span class="math">\(\sum_{i}^{n_i}\)</span></p>

<div class="references">
<h1 id="references" class="unnumbered">References</h1>
<p>Fenner, Martin. 2012. “One-Click Science Marketing.” <em>Nature Materials</em> 11 (4). Nature Publishing Group: 261–63. doi:<a href="http://dx.doi.org/10.1038/nmat3283">10.1038/nmat3283</a>.</p>
</div>

```

And is correctly parsed by Jekyll. I use this to power 
[my website](http://aarongonzales.net), whose source (yes, I suppose I consider
  the site a person) [lives here](http://github.com/xysmas/site_source).



## Installation

run 

```{.bash}
chmod +x pandoc_yaml_keeper.py
python3 -m pip install -r requirements.txt
```

To give the program execute permissions and install the required packages. 
You can symlink the program to usr or anywhere convenient from there.



