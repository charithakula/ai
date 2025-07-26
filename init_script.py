import os

structure = [
    "AI/backend/models",
    "AI/backend/routes",
    "AI/backend/services",
    "AI/backend/utils",
    "AI/frontend/public",
    "AI/frontend/src/app",
    "AI/frontend/src/components",
    "AI/frontend/src/lib",
    "AI/frontend/src/styles",
    "AI/frontend/src/types"
]

files = [
    "AI/backend/app.py",
    "AI/backend/models/flow.py",
    "AI/backend/routes/flow_routes.py",
    "AI/backend/services/flow_service.py",
    "AI/backend/utils/__init__.py",
    "AI/backend/requirements.txt",
    "AI/frontend/src/app/page.tsx",
    "AI/frontend/src/components/Canvas.tsx",
    "AI/frontend/src/components/Sidebar.tsx",
    "AI/frontend/src/components/AgentNode.tsx",
    "AI/frontend/src/lib/sampleFlow.ts",
    "AI/frontend/src/lib/api.ts",
    "AI/frontend/src/styles/globals.css",
    "AI/frontend/src/types/flow.ts",
    "AI/frontend/tailwind.config.ts",
    "AI/frontend/postcss.config.js",
    "AI/frontend/tsconfig.json",
    "AI/frontend/next.config.js",
    "AI/frontend/package.json",
    "AI/frontend/.env.local",
    "AI/README.md"
]

for folder in structure:
    os.makedirs(folder, exist_ok=True)

for file in files:
    with open(file, "w") as f:
        f.write("")  # Creates empty files

print("✅ Folder structure created!")
