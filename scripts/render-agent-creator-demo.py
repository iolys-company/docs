"""Render the illustrated agent-creator GIF (Pillow and Windows Segoe UI fonts)."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets/diagrams/agent-creator-workflow.gif"
PREVIEW = ROOT / ".preview/agent-creator"
WIDTH, HEIGHT = 960, 600
COLORS = {
    "canvas": "#100d1c",
    "panel": "#1b172a",
    "subtle": "#29233e",
    "text": "#f5efff",
    "muted": "#c5bad7",
    "border": "#47367e",
    "gold": "#d8a85d",
    "cyan": "#69c7d6",
}
FONTS = Path("C:/Windows/Fonts")
STEPS = ["Describe", "Choose scope", "Choose tools", "Generate", "Use"]


def text(draw, xy, value, size=24, color="text", bold=False, mono=False):
    filename = "consola.ttf" if mono else "segoeuib.ttf" if bold else "segoeui.ttf"
    font = ImageFont.truetype(str(FONTS / filename), size)
    draw.text(xy, value, font=font, fill=COLORS[color], anchor="lt", spacing=10)


def card(draw, box, label, lines, accent="cyan"):
    x, y, right, bottom = box
    draw.rounded_rectangle(box, radius=14, fill=COLORS["panel"], outline=COLORS["border"], width=2)
    text(draw, (x + 24, y + 22), label, 19, accent, bold=True)
    for i, line in enumerate(lines):
        text(draw, (x + 24, y + 60 + i * 36), line, 25)


def render(step):
    im = Image.new("RGB", (WIDTH, HEIGHT), COLORS["canvas"])
    draw = ImageDraw.Draw(im)
    text(draw, (36, 24), "agent-creator", 22, "cyan", bold=True)
    text(draw, (670, 28), "ILLUSTRATED WALKTHROUGH", 16, "muted")
    titles = [
        "Turn a task into a reusable agent",
        "Choose where the agent belongs",
        "Give the agent the tools it needs",
        "The skill writes the agent definition",
        "Review it, then start a new conversation",
    ]
    text(draw, (36, 67), titles[step], 33, bold=True)
    for i, label in enumerate(STEPS):
        x = 36 + i * 179
        color = "gold" if i == step else "cyan" if i < step else "border"
        draw.rounded_rectangle((x, 132, x + 166, 138), radius=3, fill=COLORS[color])
        text(draw, (x, 150), f"{i + 1}  {label}", 18, "text" if i == step else "muted")

    if step == 0:
        text(draw, (36, 202), "Skills  >  Built-in  >  agent-creator  >  Use skill", 22, "muted")
        card(draw, (36, 249, 924, 420), "YOUR REQUEST", [
            "Create an agent that reviews code changes,",
            "reports actionable bugs, and does not edit files.",
        ])
        text(draw, (36, 454), "Describe the job. The skill will write the instructions.", 24, "gold")
    elif step == 1:
        card(draw, (36, 206, 924, 320), "THE SKILL ASKS", ["Workspace or global?"])
        card(draw, (36, 342, 468, 486), "WORKSPACE  /  SELECTED", ["Keep it with this repository."], "gold")
        card(draw, (490, 342, 924, 486), "GLOBAL", ["Reuse it across workspaces."])
    elif step == 2:
        card(draw, (36, 206, 924, 316), "THE SKILL ASKS", ["All tools, selected tools, or no tools?"])
        card(draw, (36, 338, 924, 508), "YOUR CHOICE  /  SELECTED TOOLS", [
            "read_file, search_files, grep, get_errors, run_cli",
            "For run_cli: allow Git read access; deny Git write access.",
        ], "gold")
    elif step == 3:
        text(draw, (36, 203), ".github/agents/code-review.agent.md", 23, "cyan", mono=True)
        draw.rounded_rectangle((36, 246, 924, 518), radius=14, fill=COLORS["panel"], outline=COLORS["border"], width=2)
        code = [
            "---",
            "name: Code review",
            "description: Review changes and report actionable bugs.",
            "tools: [read_file, search_files, grep, get_errors, run_cli]",
            "integrations: { git: { read: true, write: false } }",
            "---",
            "Report concrete defects. Do not edit files.",
        ]
        for i, line in enumerate(code):
            text(draw, (60, 265 + i * 32), line, 23, "muted" if line == "---" else "text", mono=True)
    else:
        card(draw, (36, 206, 924, 324), "CREATED", ["Code review  /  Workspace agent"])
        card(draw, (36, 346, 924, 509), "YOUR NEXT STEP", [
            "Review the .agent.md file and select Code review.",
            "Start a new conversation: “Review my current changes.”",
        ], "gold")

    draw.line((36, 547, 924, 547), fill=COLORS["border"], width=1)
    text(draw, (36, 563), "Illustrative example · not a screen recording", 18, "muted")
    text(draw, (827, 563), f"{step + 1} / 5", 18, "muted")
    return im


if __name__ == "__main__":
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    PREVIEW.mkdir(parents=True, exist_ok=True)
    frames = [render(step) for step in range(5)]
    for i, frame in enumerate(frames):
        frame.save(PREVIEW / f"step-{i + 1}.png")
    frames[0].save(
        OUTPUT,
        save_all=True,
        append_images=frames[1:],
        duration=[5500, 4500, 6500, 7500, 5500],
        loop=0,
        optimize=True,
        disposal=2,
    )
    print(f"Created {OUTPUT} ({OUTPUT.stat().st_size:,} bytes)")
