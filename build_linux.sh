docker run --rm -v "$(pwd):/src/" cdrx/pyinstaller-linux -c \
  "pip install -r requirements.txt && \
  pyinstaller main.py --onedir --onefile --clean --noconsole && \
  mv dist/main mytoolkit_L && \
  rm -rf __pycache__/ build/ dist/ main.spec"