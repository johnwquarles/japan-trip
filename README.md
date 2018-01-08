# To Contribute:

### Setup
> - Clone the repo.
> - Create a virtualenv if desired.
> - `pip install -r requirements.txt` from the project root directory.

### Add Content
> - Add a markdown file (or edit one) within the `/content` directory.
> - Make a PR.
> - Tell JQ to merge & publish.
> - Or have yourself added as a contributor and merge & publish yourself.

### Preview Locally

> - Run `make devserver` from the root directory (this will start the dev server, watch for changes & rebuilt output files).
> - Head to `localhost:2018` in your browser.

### Stop the Dev Server (it runs in the background until you access the page)
> - Run `make stopserver`

# To Publish:

Run `make github` from the root directory.