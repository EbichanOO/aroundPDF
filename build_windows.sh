docker run --rm -v "$(pwd):/src/" cdrx/pyinstaller-windows -c \
  "pip install -r requirements.txt && \
  pyinstaller main.py --onedir --onefile --clean --noconsole && \
  mv dist/main.exe mytoolkit_w.exe && \
  rm -rf __pycache__/ build/ dist/ main.spec"