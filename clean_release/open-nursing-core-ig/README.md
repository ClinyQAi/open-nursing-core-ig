# Open Nursing Core IG

This repository contains the source code for the Open Nursing Core Implementation Guide.

## Build Instructions

To generate the full website (docs folder):
1.  Ensure you have `fsh-sushi` and the IG Publisher installed.
2.  Run `sushi .` to generate resources.
3.  Run `java -jar publisher.jar -ig .` to generate the HTML.
4.  The output will be in `output/`. Move this to `docs/` to publish to GitHub Pages.

## Note on Submission
Due to file size limits, the full `docs/` folder was not included in this commit. Please run the build to populate it.
