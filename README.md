# pandoc-figref: A simple pandoc filter for automatically numbering figures (or whatever)

pandoc-figref is a simple tool for automatically numbering (and referencing) figures in a
[pandoc][] document. As a chemist, I often need to maintain several different types of figures with
their own separate numbering schemes (e.g., Figures, Schemes, Charts). pandoc-figref allows one to
do this easily. There are many such tools available, such as the excellent [pandoc-fignos][].
pandoc-figref is very simple and specifically designed for chemists writing manuscripts and
managing both figures and schemes.

## Installation

For LaTeX/pdf output, you will have to suppress automatic numbering in captions by modifying your
template. I do this using the [caption package][cap_pkg].

## Usage

The numbers for figures are tagged with the syntax `{#?:label}`, where `?` is a lowercase letter
giving the kind of figure and `label` is a (unique) identifier for the figure. The figures (or
whatever) are numbered in the order they appear and different kinds of figures are tracked
separately. So, for example, one could use `{#f:happy_face}`, `{#f:sad_face}`, and `{#s:synthesis}`
within the document, and these would be replaced with the numbers `1`, `2`, and `1`, respectively.
Of course, if a tag is reused it then gets the same number so that figures can be referred to in 
captions and in multiple places in the text.

[pandoc]: http://pandoc.org
[pandoc-fignos]: https://github.com/tomduck/pandoc-fignos
[cap_pkg]: https://www.ctan.org/pkg/caption