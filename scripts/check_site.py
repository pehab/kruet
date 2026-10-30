"""Validate local site references and document structure without dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1] / 'site'

class Document(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.source = source
        self.refs = []
        self.ids = set()
        self.h1_count = 0
        self.viewport = False
        self.errors = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h1':
            self.h1_count += 1
        if tag == 'meta' and attrs.get('name') == 'viewport':
            self.viewport = True
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                self.errors.append(f"Duplicate id: {attrs['id']}")
            self.ids.add(attrs['id'])
        if tag == 'img' and 'alt' not in attrs:
            self.errors.append('Image has no alt attribute')
        for key in ('href', 'src'):
            if key in attrs:
                self.refs.append(attrs[key])


def main():
    documents = {}
    for path in ROOT.glob('*.html'):
        doc = Document(path)
        doc.feed(path.read_text(encoding='utf-8'))
        documents[path.name] = doc
    errors = []
    for name, doc in documents.items():
        errors.extend(f'{name}: {error}' for error in doc.errors)
        if doc.h1_count != 1 or not doc.viewport:
            errors.append(f'{name}: expected one h1 and a viewport meta tag')
        for ref in doc.refs:
            url = urlsplit(ref)
            if url.scheme or url.netloc:
                continue
            target = url.path or name
            if not (ROOT / target).is_file():
                errors.append(f'{name}: missing file {ref}')
            if url.fragment and target in documents and url.fragment not in documents[target].ids:
                errors.append(f'{name}: missing anchor {ref}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'OK: {len(documents)} HTML pages; local links, anchors, images and basic structure checked.')

if __name__ == '__main__':
    main()
