port := "8000"

# List available recipes
default:
    @just --list

# Serve the reveal.js presentation and open it in a browser
preso:
    (sleep 1 && open http://localhost:{{port}}/) &
    python3 -m http.server {{port}} --directory presentation
