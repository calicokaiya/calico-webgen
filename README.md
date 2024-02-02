# calico-webgen
Simple website generator.
This is the website generator I use for [my website](calicocali.neocities.org)


# How do I install this ?
1. Create a virtual environment
2. Enter the virtual environment
3. Install the dependencies using `pip install -r requirements.txt`
4. You're all set :o


# How do I use this ?
1. Put your website tree in the `pages` folder. Whatever you want to be rendered in your html template should be defined as a .txt file. Anything else can just be dumped in here, be it a css or a js file or whatever.
2. Put your html template and call it `template.html` in the `templates` folder (see: How do I make a template?).
3. Run `main.py`
4. Get your results from the `result` folder
5. Voila 


# How do I make a template ?
## Page title
Your HTML template should have the following characteristics:
`{{page_title}}` is the placeholder for the title of the page. You can set a page title by adding `$title = [TITLE GOES HERE]` to the first line of your page text file.

## Page content
```
{% for line in content -%}
    {{line}}
{%- endfor %}
```
Adding these lines to your your template will define the placeholder for the content of your website.
Whatever text files you put in the `pages` folder will be read line by line, formatted and rendered wherever you put these lines.


# Contributing
Just for and do whatever you want, so long as you're not breaking the License.


# This documentation and this generator sucks
Probably. I made this as a tool for my own personal website. It is simple and it doesn't need to be any more complicated than what it is. Feel free to fork it and do whatever.