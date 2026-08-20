#!/usr/bin/env python3
"""Generate the README Stack section.

The wall is deliberately exhaustive (see CLAUDE.md). Entries are sourced from the
resume, the project list in alexgaoth.github.io, and declared dependencies across
the local repos. Add rows here, then: python3 scripts/make_badges.py
An unknown simple-icons slug still returns HTTP 200 with no icon, so verify with
scripts/check_badges.sh after editing.
"""
BG = "161b22"

GROUPS = [
 ("Languages", [
   ("Python","python"),("TypeScript","typescript"),("JavaScript","javascript"),
   ("Rust","rust"),("C","c"),("C++","cplusplus"),("C#","dotnet"),("Java","openjdk"),
   ("SQL",""),("Bash","gnubash"),("PowerShell",""),("GDScript","godotengine"),
   ("Solidity","solidity"),("HTML5","html5"),("CSS","css")]),
 ("Frameworks & UI", [
   ("React","react"),("Next.js","nextdotjs"),("Svelte / SvelteKit","svelte"),
   ("Astro","astro"),("Vite","vite"),("Tailwind CSS","tailwindcss"),
   ("shadcn/ui","shadcnui"),("Three.js","threedotjs"),("React Three Fiber","threedotjs"),
   ("Electron","electron"),("Unity","unity"),("Godot","godotengine")]),
 ("Backend & APIs", [
   ("Node.js","nodedotjs"),("Bun","bun"),("Express","express"),("FastAPI","fastapi"),
   ("Flask","flask"),("Uvicorn",""),("Gunicorn","gunicorn"),("Prisma","prisma"),
   ("SQLAlchemy","sqlalchemy"),("Pydantic","pydantic"),("Zod","zod"),
   ("OpenAPI / Swagger","swagger"),("Stripe","stripe")]),
 ("Data & infrastructure", [
   ("PostgreSQL","postgresql"),("MySQL","mysql"),("MongoDB","mongodb"),("SQLite","sqlite"),
   ("Redis","redis"),("Apache Kafka","apachekafka"),("Avro","apacheavro"),("BullMQ",""),
   ("Qdrant","qdrant"),("Chroma",""),("Supabase","supabase"),("MinIO","minio"),
   ("Docker","docker"),("Podman","podman"),("AWS",""),
   ("Cloudflare","cloudflare"),("Vercel","vercel"),("GitHub Actions","githubactions")]),
 ("ML, data & robotics", [
   ("PyTorch","pytorch"),("OpenCV","opencv"),("NumPy","numpy"),("pandas","pandas"),
   ("Apache Arrow","apachearrow"),("Jupyter","jupyter"),("Hugging Face","huggingface"),
   ("ONNX Runtime","onnx"),("OpenAI",""),("Google Gemini","googlegemini"),
   ("Vercel AI SDK","vercel"),("ORB-SLAM3",""),("YOLO11",""),("Jetson","nvidia"),
   ("WebGL","webgl"),("WebAssembly","webassembly"),("GeoPandas",""),("OSRM","")]),
 ("Automation & tooling", [
   ("Playwright",""),("Puppeteer","puppeteer"),("Selenium","selenium"),
   ("BeautifulSoup",""),("Apify",""),("pytest","pytest"),("Vitest","vitest"),
   ("ESLint","eslint"),("Prettier","prettier"),("Git","git"),("Linux","linux"),
   ("GNOME","gnome"),("Claude Code","anthropic"),("PyPI","pypi"),("npm","npm")]),
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
            f"![{l}](https://img.shields.io/badge/{slug(l)}-{BG}?style=flat-square"
            + (f"&logo={g}" if g else "") + "&logoColor=white)"
            for l, g in items))
        out.append("")
    return "\n".join(out).rstrip()


if __name__ == "__main__":
    print(render())
