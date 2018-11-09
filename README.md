_If you just want the words list, [here it is](https://github.com/nicolas-raoul/anki-deck-for-duolingo-chinese/blob/master/words.tsv)._

# Anki deck for Duolingo Chinese

Anki is a natural companion to Duolingo. Duolingo is good at introducing new concepts and words, and Anki is going at making you actually remember them.

1. [Download the apkg file](https://github.com/nicolas-raoul/anki-deck-for-duolingo-chinese/blob/master/Chinese%20Duolingo%20for%20English%20speakers.apkg).
2. Open it in AnkiDroid, AnkiMobile, or Anki Desktop.
3. Each day after using Duolingo, use Anki.

# Help us fix mistakes

The deck contains many mistakes, there is a lot of room for improvement. The good news: You can help. Here is how to do.

1. Find a desktop computer.
2. Create a [Github](https://github.com) account if you don't have one already.
3. Install [GitHub Desktop](https://desktop.github.com/) (if you are already familiar with Git, feel free to use your favorite Git tool instead).
4. [Fork](https://help.github.com/articles/fork-a-repo/) this [repository](https://github.com/nicolas-raoul/anki-deck-for-duolingo-chinese).
5. [Clone](https://help.github.com/articles/cloning-a-repository/#cloning-a-repository-to-github-desktop) your forked repository. Be sure to clone YOUR own repository (with your name in the URL), not ours.
6. Find the `words.tsv` and open it with a spreasheet program such as LibreOffice (free).
7. Fix stuff (see rules below) and save the file.
8. Within that folder that you created, put all of the screenshots.
9. [Commit the TSV file](https://help.github.com/desktop/guides/contributing-to-projects/committing-and-reviewing-changes-to-your-project/#2-selecting-changes-to-include-in-a-commit), then push.
10. Go to https://github.com/nicolas-raoul/anki-deck-for-duolingo-chinese/pulls and click the button "New pull request", then submit the pull request to us ([tutorial about pull requests](https://help.github.com/articles/creating-a-pull-request-from-a-fork/)).
11. We will review your contribution, merge it into our repository, and re-generate the apkg file. Thanks! :-)

# Guidelines

## Copyright

- This deck contains only words, not sentences. The reason is that sentence can be considered as intellectual property, whereas a list of words can not. So, please do not add sentences from Duolingo or from elsewhere.
- Do not copy English translations from any other source (and especially, not from Duolingo). Just simplify or fix the existing definitions.

## Content

- Most English definitions needs to be simplified. The meanings that are not used in Duolingo should be removed. For instance, if `三`'s definition is `surname San<br /><br />three  / 3`, then it should be simplified to just "three".
- The line for `加拿大` is very useful, but I think we don't need the individual character notes `加`, `拿`, `大`, so these ones can be deleted.

# TODO

- Add pronunciation audio files
- Fix all of the content problems
- Once this is done, I will push the deck to the Anki shared decks
- In parallel, implement a web page that shows the list in a nice way, for people who just want to see the list on the web

# Thanks

Huge thanks to Anish for creating the words list.
