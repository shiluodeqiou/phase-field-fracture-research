from html import unescape
from html.parser import HTMLParser
from pathlib import Path
import re


class TurnParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.turns = []
        self.current = None
        self.skip_depth = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if self.current is None and "data-conversation-share-turn" in attrs:
            self.current = []
            self.skip_depth = 0
            return
        if self.current is not None and tag in {"script", "style", "svg", "template"}:
            self.skip_depth += 1

    def handle_endtag(self, tag):
        if self.current is None:
            return
        if self.skip_depth and tag in {"script", "style", "svg", "template"}:
            self.skip_depth -= 1
            return
        if not self.skip_depth and tag == "div":
            text = " ".join(self.current)
            text = re.sub(r"\s+", " ", unescape(text)).strip()
            if text:
                self.turns.append(text)
            self.current = None

    def handle_data(self, data):
        if self.current is not None and not self.skip_depth:
            data = data.strip()
            if data:
                self.current.append(data)


src = Path(r"E:\安装包\e68b1ab1-5a76-48d7-ae14-56c538055299.htm")
parser = TurnParser()
parser.feed(src.read_text(encoding="utf-8", errors="ignore"))
Path(r"zcode_work\share_turns.txt").write_text(
    "\n\n".join(f"TURN {i}: {t}" for i, t in enumerate(parser.turns, 1)),
    encoding="utf-8",
)
print(f"turns={len(parser.turns)}")
