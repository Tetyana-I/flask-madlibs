from flask import Flask, request, render_template
from stories import Story, story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__) 

app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

STORIES = [
    (["place", "noun", "verb", "adjective", "plural_noun"],"Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."),
    (["noun", "verb"], "I love to {verb} a good {noun}.")
    ]
# story = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."""
# )

@app.route("/")
def homepage():
    """homepage for the app"""
    number_of_stories = len(STORIES)

    return render_template("homepage.html", number = number_of_stories)

@app.route("/form")
def form():
    """page that prompts for the list of story questions"""
    return render_template("form.html", prompts=story.prompts)

# @app.route("/form/<story_num>")
# def form(story_num):
#     """page that prompts for the list of story questions"""
#     prompts,text = STORIES[int(story_num)]
#     return render_template("form.html", prompts=prompts)

@app.route("/story")
def generated_story():
    """page that shows the resulting story for user's answers"""
    answers= {prompt: request.args.get(f"{prompt}") for prompt in story.prompts}
    story_text = story.generate(answers)
    return render_template("story.html", story_text=story_text)