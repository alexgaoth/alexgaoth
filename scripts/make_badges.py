#!/usr/bin/env python3
"""Generate the README Stack section.

Entries are sourced from the resume, the project list in alexgaoth.github.io, and
declared dependencies across the local repos (see CLAUDE.md). Each entry is
(label, simple-icons slug, Wikipedia title); the badge links to that article.
Add rows here, then: python3 scripts/make_badges.py
An unknown simple-icons slug still returns HTTP 200 with no icon, so verify with
scripts/check_badges.sh after editing.
"""
from urllib.parse import quote

BG = "161b22"
WIKI = "https://en.wikipedia.org/wiki/"

GROUPS = [
 ("Languages", [
   ("Python","python","Python (programming language)"),
   ("TypeScript","typescript","TypeScript"),("JavaScript","javascript","JavaScript"),
   ("Rust","rust","Rust (programming language)"),("C","c","C (programming language)"),
   ("C++","cplusplus","C++"),("C#","dotnet","C Sharp (programming language)"),
   ("Java","openjdk","Java (programming language)"),("SQL","","SQL"),
   ("Bash","gnubash","Bash (Unix shell)"),("PowerShell","","PowerShell"),
   ("GDScript","godotengine","GDScript"),("Solidity","solidity","Solidity"),
   ("HTML5","html5","HTML5"),("CSS","css","CSS")]),
 ("Frameworks", [
   ("React","react","React (software)"),("Next.js","nextdotjs","Next.js"),
   ("Svelte / SvelteKit","svelte","Svelte"),("Astro","astro","Static site generator"),
   ("Vite","vite","Vite"),("Tailwind CSS","tailwindcss","Tailwind CSS"),
   ("Three.js","threedotjs","Three.js"),("Node.js","nodedotjs","Node.js"),
   ("Bun","bun","Bun (software)"),("Express","express","Express.js"),
   ("FastAPI","fastapi","FastAPI"),("Flask","flask","Flask (web framework)"),
   ("Prisma","prisma","Object–relational mapping"),
   ("Electron","electron","Electron (software framework)"),
   ("Unity","unity","Unity (game engine)"),("Godot","godotengine","Godot (game engine)")]),
 ("Data & infrastructure", [
   ("PostgreSQL","postgresql","PostgreSQL"),("MySQL","mysql","MySQL"),
   ("MongoDB","mongodb","MongoDB"),("SQLite","sqlite","SQLite"),("Redis","redis","Redis"),
   ("Apache Kafka","apachekafka","Apache Kafka"),("Avro","apacheavro","Apache Avro"),
   ("BullMQ","","Job queue"),("Qdrant","qdrant","Qdrant"),("Chroma","","ChromaDB"),
   ("Supabase","supabase","Backend as a service"),("MinIO","minio","MinIO"),
   ("Docker","docker","Docker (software)"),("Podman","podman","Podman"),
   ("AWS","","Amazon Web Services"),("Cloudflare","cloudflare","Cloudflare"),
   ("Vercel","vercel","Vercel"),("GitHub Actions","githubactions","GitHub Actions")]),
 ("ML, data & robotics", [
   ("PyTorch","pytorch","PyTorch"),("OpenCV","opencv","OpenCV"),("NumPy","numpy","NumPy"),
   ("pandas","pandas","Pandas (software)"),("Apache Arrow","apachearrow","Apache Arrow"),
   ("Jupyter","jupyter","Project Jupyter"),("Hugging Face","huggingface","Hugging Face"),
   ("ONNX Runtime","onnx","Open Neural Network Exchange"),("OpenAI","","OpenAI"),
   ("Google Gemini","googlegemini","Gemini (language model)"),
   ("ORB-SLAM3","","Simultaneous localization and mapping"),
   ("YOLO11","","You Only Look Once"),("Jetson","nvidia","Nvidia Jetson"),
   ("WebGL","webgl","WebGL"),("WebAssembly","webassembly","WebAssembly"),
   ("GeoPandas","","GeoPandas"),("OSRM","","Open Source Routing Machine")]),
 ("Automation & tooling", [
   ("Playwright","","Playwright (software)"),("Puppeteer","puppeteer","Puppeteer (software)"),
   ("Selenium","selenium","Selenium (software)"),
   ("BeautifulSoup","","Beautiful Soup (HTML parser)"),("pytest","pytest","Pytest"),
   ("ESLint","eslint","ESLint"),("Git","git","Git"),("Linux","linux","Linux"),
   ("GNOME","gnome","GNOME"),("Claude Code","anthropic","Claude Code"),
   ("PyPI","pypi","Python Package Index"),("npm","npm","Npm")]),
]


def slug(label):
    s = label.replace("-", "--").replace("_", "__")
    for a, b in (("+", "%2B"), ("#", "%23"), (" ", "%20"), ("&", "%26"), ("/", "%2F")):
        s = s.replace(a, b)
    return s


def render():
    out = []
    for title, items in GROUPS:
        out.append(f"**{title}**  ")
        out.append(" ".join(
            f"[![{l}](https://img.shields.io/badge/{slug(l)}-{BG}?style=flat-square"
            + (f"&logo={g}" if g else "") + "&logoColor=white)]"
            + f"({WIKI}{quote(w.replace(' ', '_'), safe='#')})"
            for l, g, w in items))
        out.append("")
    return "\n".join(out).rstrip()


if __name__ == "__main__":
    print(render())
